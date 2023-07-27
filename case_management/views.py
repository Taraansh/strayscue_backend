from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authorization.models import Profile
from case_management.serializers import CaseSerializer, ReportingDetailSerializer, AnimalDetailSerializer, MedicalDetailSerializer, OperationDetailSerializer, PostOperationDetailSerializer
from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail
from ngo_management.models import Ngo


@api_view(['GET'])
def get_cases_by_email(request, email):
    try:
        profile = Profile.objects.get(email=email)  # Retrieve the Profile object based on the provided email
        cases = Case.objects.filter(user_adding_this_case=profile)  # Filter the cases based on the Profile object
        serializer = CaseSerializer(cases, many=True)  # Serialize the filtered cases
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_case(request):
    case_data = {
        "type_of_case": request.data.get("type_of_case"),
        "status_of_case": request.data.get("status_of_case"),
        "mortality_of_case": request.data.get("mortality_of_case"),
        "cause_of_failure": request.data.get("cause_of_failure"),
        "user_adding_this_case": request.data.get("user_adding_this_case"),
    }

    serializer = CaseSerializer(data=case_data)
    if serializer.is_valid():
        serializer.save()
        case_instance = serializer.instance
        reporter_data = {
            "case_linked": case_instance.case_id,
            "reporterName": "",  # Provide the default or blank value here
            "reporterContact": "",
            "landmark": "",
            "location": "",
            "pincode": "",
            # Add other fields of the ReportingDetail model with default or blank values
        }
        reporter_serializer = ReportingDetailSerializer(data=reporter_data)
        if reporter_serializer.is_valid():
            reporter_serializer.save()
            # Verify that the reporter_serializer.data is printed in the console
            # print(reporter_serializer.data)
        else:
            # Print serializer errors to debug any issues
            print(reporter_serializer.errors)

        # Create blank instances for other related models
        animal_data = {"case_linked": case_instance.case_id}
        animal_serializer = AnimalDetailSerializer(data=animal_data)
        if animal_serializer.is_valid():
            animal_serializer.save()
            # print(animal_serializer.data)
        else:
            # Print serializer errors to debug any issues
            print(animal_serializer.errors)

        medical_data = {"case_linked": case_instance.case_id}
        medical_serializer = MedicalDetailSerializer(data=medical_data)
        if medical_serializer.is_valid():
            medical_serializer.save()
            # print(medical_serializer.data)
        else:
            # Print serializer errors to debug any issues
            print(medical_serializer.errors)

        operation_data = {"case_linked": case_instance.case_id}
        operation_serializer = OperationDetailSerializer(data=operation_data)
        if operation_serializer.is_valid():
            operation_serializer.save()
            # print(operation_serializer.data)
        else:
            # Print serializer errors to debug any issues
            print(operation_serializer.errors)

        post_operation_data = {"case_linked": case_instance.case_id}
        post_operation_serializer = PostOperationDetailSerializer(data=post_operation_data)
        if post_operation_serializer.is_valid():
            post_operation_serializer.save()
            # print(post_operation_serializer.data)
        else:
            # Print serializer errors to debug any issues
            print(post_operation_serializer.errors)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_case(request, case_id):
    try:
        case = Case.objects.get(case_id=case_id)
    except Case.DoesNotExist:
        return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

    case.type_of_case = request.data.get("type_of_case", case.type_of_case)
    case.status_of_case = request.data.get("status_of_case", case.status_of_case)
    case.mortality_of_case = request.data.get("mortality_of_case", case.mortality_of_case)
    case.cause_of_failure = request.data.get("cause_of_failure", case.cause_of_failure)

    case.save()
    serializer = CaseSerializer(case)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['DELETE'])
def delete_case(request, case_id):
    try:
        case = Case.objects.get(case_id=case_id)
    except Case.DoesNotExist:
        return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

    case.delete()
    return Response({"detail": "Case Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def get_cases_by_ngo(request, email):
#     try:
#         profile = Profile.objects.get(email=email)
#         ngo_id_linked = profile.ngo_linked_with_this_user.id
#         ngo = Ngo.objects.get(id=ngo_id_linked)
#         id_ngo = ngo.id
#         users_linked_with_ngo = Profile.objects.filter(ngo_linked_with_this_user=id_ngo)

#         cases_linked_with_users = Case.objects.filter(user_adding_this_case=users_linked_with_ngo )
#         serializer = CaseSerializer(cases_linked_with_users, many=True)  # Serialize the filtered cases
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Profile.DoesNotExist:
#         return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_cases_by_ngo(request, email):
    try:
        profile = Profile.objects.get(email=email)
        ngo = profile.ngo_linked_with_this_user  # Get the NGO associated with the user's profile

        # Retrieve all users associated with the NGO
        users_linked_with_ngo = Profile.objects.filter(ngo_linked_with_this_user=ngo)

        # Retrieve all cases associated with the users from the previous step
        cases_linked_with_users = Case.objects.filter(user_adding_this_case__in=users_linked_with_ngo)

        serializer = CaseSerializer(cases_linked_with_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_reporter(request, id):
    try:
        reporter = ReportingDetail.objects.get(id=id)
    except ReportingDetail.DoesNotExist:
        return Response({"error": "Reporter not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update the existing ReportingDetail object's fields based on the request data
    reporter.reporterName = request.data.get("reporterName", reporter.reporterName)
    reporter.reporterContact = request.data.get("reporterContact", reporter.reporterContact)
    reporter.reporterAltContact = request.data.get("reporterAltContact", reporter.reporterAltContact)
    reporter.reporterEmail = request.data.get("reporterEmail", reporter.reporterEmail)
    reporter.landmark = request.data.get("landmark", reporter.landmark)
    reporter.location = request.data.get("location", reporter.location)
    reporter.pincode = request.data.get("pincode", reporter.pincode)
    reporter.reportedDate = request.data.get("reportedDate", reporter.reportedDate)
    reporter.reportedTime = request.data.get("reportedTime", reporter.reportedTime)
    reporter.pickupDate = request.data.get("pickupDate", reporter.pickupDate)
    reporter.pickupTime = request.data.get("pickupTime", reporter.pickupTime)
    
    front_image_file = request.FILES.get("frontImage")
    if front_image_file is not None:
        reporter.frontImage = front_image_file
    elif "frontImage" in request.data and request.data["frontImage"] == "null":
        reporter.frontImage = None
    
    back_image_file = request.FILES.get("backImage")
    if back_image_file is not None:
        reporter.backImage = back_image_file
    elif "backImage" in request.data and request.data["backImage"] == "null":
        reporter.backImage = None
    
    consent_form_image_file = request.FILES.get("consentFormImage")
    if consent_form_image_file is not None:
        reporter.consentFormImage = consent_form_image_file
    elif "consentFormImage" in request.data and request.data["consentFormImage"] == "null":
        reporter.consentFormImage = None

    reporter.save()
    # Pass the existing case object to the serializer for response
    serializer = ReportingDetailSerializer(reporter)
    # print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_animal(request, id):
    try:
        animal = AnimalDetail.objects.get(id=id)
    except AnimalDetail.DoesNotExist:
        return Response({"error": "Animal Details not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update the existing AnimalDetail object's fields based on the request data
    animal.animalSpecies = request.data.get("animalSpecies", animal.animalSpecies)
    animal.animalBreed = request.data.get("animalBreed", animal.animalBreed)
    animal.animalAge = request.data.get("animalAge", animal.animalAge)
    animal.animalTemperament = request.data.get("animalTemperament", animal.animalTemperament)
    animal.animalGender = request.data.get("animalGender", animal.animalGender)
    animal.animalPregnant = request.data.get("animalPregnant", animal.animalPregnant)
    animal.animalMarking = request.data.get("animalMarking", animal.animalMarking)
    animal.animalColor = request.data.get("animalColor", animal.animalColor)
    animal.animalCatchable = request.data.get("animalCatchable", animal.animalCatchable)
    animal.animalWeight = request.data.get("animalWeight", animal.animalWeight)
    animal.admissionReason = request.data.get("admissionReason", animal.admissionReason)

    animal_pictures_file = request.FILES.get("animalPictures")
    if animal_pictures_file is not None:
        animal.animalPictures = animal_pictures_file
    elif "animalPictures" in request.data and request.data["animalPictures"] == "null":
        animal.animalPictures = None

    animal.save()
    
    # Pass the existing case object to the serializer for response
    serializer = AnimalDetailSerializer(animal)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_medical(request, id):
    try:
        medical = MedicalDetail.objects.get(id=id)
    except MedicalDetail.DoesNotExist:
        return Response({"error": "Medical Details not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update the existing MedicalDetail object's fields based on the request data
    medical.medicalHistory = request.data.get("medicalHistory", medical.medicalHistory)
    medical.vaccinationStatus = request.data.get("vaccinationStatus", medical.vaccinationStatus)
    medical.dewormed = request.data.get("dewormed", medical.dewormed)
    medical.fitForSurgery = request.data.get("fitForSurgery", medical.fitForSurgery)
    medical.otherDetails = request.data.get("otherDetails", medical.otherDetails)
    medical.admissionDate = request.data.get("admissionDate", medical.admissionDate)

    feeding_record_image_file = request.FILES.get("feedingRecordImage")
    if feeding_record_image_file is not None:
        medical.feedingRecordImage = feeding_record_image_file
    elif "feedingRecordImage" in request.data and request.data["feedingRecordImage"] == "null":
        medical.feedingRecordImage = None

    blood_report_image_file = request.FILES.get("bloodReportImage")
    if blood_report_image_file is not None:
        medical.bloodReportImage = blood_report_image_file
    elif "bloodReportImage" in request.data and request.data["bloodReportImage"] == "null":
        medical.bloodReportImage = None

    medical.save()
    
    # Pass the existing case object to the serializer for response
    serializer = MedicalDetailSerializer(medical)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_operation(request, id):
    try:
        operation = OperationDetail.objects.get(id=id)
    except OperationDetail.DoesNotExist:
        return Response({"error": "Operation Details not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Update the existing OperationDetail object's fields based on the request data
    operation.vetName = request.data.get("vetName", operation.vetName)
    operation.operationDate = request.data.get("operationDate", operation.operationDate)
    operation.operationStartTime = request.data.get("operationStartTime", operation.operationStartTime)
    operation.operationEndTime = request.data.get("operationEndTime", operation.operationEndTime)
    operation.operationOutcome = request.data.get("operationOutcome", operation.operationOutcome)

    medical_prescription_image_file = request.FILES.get("medicalPrescriptionImage")
    if medical_prescription_image_file is not None:
        operation.medicalPrescriptionImage = medical_prescription_image_file
    elif "medicalPrescriptionImage" in request.data and request.data["medicalPrescriptionImage"] == "null":
        operation.medicalPrescriptionImage = None

    treatment_record_image_file = request.FILES.get("treatmentRecordImage")
    if treatment_record_image_file is not None:
        operation.treatmentRecordImage = treatment_record_image_file
    elif "treatmentRecordImage" in request.data and request.data["treatmentRecordImage"] == "null":
        operation.treatmentRecordImage = None

    organ_image_file = request.FILES.get("organImage")
    if organ_image_file is not None:
        operation.organImage = organ_image_file
    elif "organImage" in request.data and request.data["organImage"] == "null":
        operation.organImage = None

    operation.save()
    
    # Pass the existing case object to the serializer for response
    serializer = OperationDetailSerializer(operation)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_post_operation(request, id):
    try:
        post_operation = PostOperationDetail.objects.get(id=id)
    except PostOperationDetail.DoesNotExist:
        return Response({"error": "Medical Details not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update the existing PostOperationDetail object's fields based on the request data
    post_operation.popComment = request.data.get("popComment", post_operation.popComment)
    post_operation.popFacility = request.data.get("popFacility", post_operation.popFacility)
    post_operation.popExpectedDays = request.data.get("popExpectedDays", post_operation.popExpectedDays)
    post_operation.popStartDate = request.data.get("popStartDate", post_operation.popStartDate)
    post_operation.popEndDate = request.data.get("popEndDate", post_operation.popEndDate)
    post_operation.releaseDate = request.data.get("releaseDate", post_operation.releaseDate)
    post_operation.euthanized = request.data.get("euthanized", post_operation.euthanized)
    post_operation.comments = request.data.get("comments", post_operation.comments)

    pop_pictures_file = request.FILES.get("popPictures")
    if pop_pictures_file is not None:
        post_operation.popPictures = pop_pictures_file
    elif "popPictures" in request.data and request.data["popPictures"] == "null":
        post_operation.popPictures = None

    release_pictures_image_file = request.FILES.get("releasePictures")
    if release_pictures_image_file is not None:
        post_operation.releasePictures = release_pictures_image_file
    elif "releasePictures" in request.data and request.data["releasePictures"] == "null":
        post_operation.releasePictures = None

    post_operation.save()
    
    # Pass the existing case object to the serializer for response
    serializer = PostOperationDetailSerializer(post_operation)
    return Response(serializer.data, status=status.HTTP_200_OK)
