from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authorization.models import Profile
from case_management.serializers import CaseSerializer, ReportingDetailSerializer, AnimalDetailSerializer, MedicalDetailSerializer, OperationDetailSerializer, PostOperationDetailSerializer
from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail, AnimalPictures, FeedingRecordImage, TreatmentRecordImage, OrganImage, PopPictures, ReleasePictures


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
            # animal_detail_instance = animal_serializer
            # animal_picture_serializer = AnimalPicturesSerializer(animal_linked = animal_detail_instance)
            # if animal_picture_serializer.is_valid():
            #     animal_picture_serializer.save()
            # else:
            #     print(animal_picture_serializer.errors)
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
    print(serializer.data)
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
    # animal.animalPictures = request.FILES.getlist("animalPictures")

    animal_pictures_files = request.FILES.getlist("animalPictures")
    if animal_pictures_files:
        for image_file in animal_pictures_files:
            AnimalPictures.objects.create(animal_linked=animal, animalPictures = image_file)
    
    animal.save()
    
    # Pass the existing case object to the serializer for response
    serializer = AnimalDetailSerializer(animal)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_animal_picture(request, id):
    try:
        animal_picture = AnimalPictures.objects.get(id=id)
    except AnimalPictures.DoesNotExist:
        return Response({"error": "Animal Pictures not found"}, status=status.HTTP_404_NOT_FOUND)

    animal_picture.delete()
    return Response({"detail": "Animal Pictures Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)


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

    feeding_record_image_file = request.FILES.getlist("feedingRecordImage")
    if feeding_record_image_file:
        for image_file in feeding_record_image_file:
            FeedingRecordImage.objects.create(medical_linked = medical, feedingRecordImage=image_file)

    blood_report_image_file = request.FILES.get("bloodReportImage")
    if blood_report_image_file is not None:
        medical.bloodReportImage = blood_report_image_file
    elif "bloodReportImage" in request.data and request.data["bloodReportImage"] == "null":
        medical.bloodReportImage = None

    medical.save()
    
    # Pass the existing case object to the serializer for response
    serializer = MedicalDetailSerializer(medical)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_feeding_record_image(request, id):
    try:
        feeding_record_image = FeedingRecordImage.objects.get(id=id)
    except FeedingRecordImage.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    feeding_record_image.delete()
    return Response({"detail": "Record Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)


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

    treatment_record_image_file = request.FILES.getlist("treatmentRecordImage")
    if treatment_record_image_file:
        for image_file in treatment_record_image_file:
            TreatmentRecordImage.objects.create(operation_linked = operation, treatmentRecordImage=image_file)

    organ_image_file = request.FILES.getlist("organImage")
    if organ_image_file:
        for image_file in organ_image_file:
            OrganImage.objects.create(operation_linked = operation, organImage=image_file)

    operation.save()
    
    # Pass the existing case object to the serializer for response
    serializer = OperationDetailSerializer(operation)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_treatment_record_image(request, id):
    try:
        treatment_record_image = TreatmentRecordImage.objects.get(id=id)
    except TreatmentRecordImage.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

    treatment_record_image.delete()
    return Response({"detail": "Record Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_organ_image(request, id):
    try:
        organ_image = OrganImage.objects.get(id=id)
    except OrganImage.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

    organ_image.delete()
    return Response({"detail": "Image Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)


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

    pop_pictures_file = request.FILES.getlist("popPictures")
    if pop_pictures_file:
        for image_file in pop_pictures_file:
            PopPictures.objects.create(post_operation_linked = post_operation, popPictures=image_file)

    release_pictures_file = request.FILES.getlist("releasePictures")
    if release_pictures_file:
        for image_file in release_pictures_file:
            ReleasePictures.objects.create(post_operation_linked = post_operation, releasePictures=image_file)

    post_operation.save()
    
    # Pass the existing case object to the serializer for response
    serializer = PostOperationDetailSerializer(post_operation)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_pop_pictures(request, id):
    try:
        pop_pictures = PopPictures.objects.get(id=id)
    except PopPictures.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

    pop_pictures.delete()
    return Response({"detail": "Image Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_release_pictures(request, id):
    try:
        release_pictures = ReleasePictures.objects.get(id=id)
    except ReleasePictures.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

    release_pictures.delete()
    return Response({"detail": "Image Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)