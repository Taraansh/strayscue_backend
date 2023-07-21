from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authorization.models import Profile
from authorization.serializers import ProfileSerializer
from case_management.serializers import CaseSerializer, ReportingDetailSerializer, AnimalDetailSerializer, MedicalDetailSerializer, OperationDetailSerializer, PostOperationDetailSerializer
from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail


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



@api_view(['POST'])
def create_case_reporter(request):
    if request.method == 'POST':
        case_id = request.data.get('case_linked')
        try:
            case= Case.objects.get(case_id=case_id)
            case_id = case.case_id
        except Case.DoesNotExist:
            return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

        # Extract the data from the request
        reporter_data = {
            "case_linked": case_id,
            "reporterName": request.data.get("reporterName"),
            "reporterContact": request.data.get("reporterContact"),
            "reporterAltContact": request.data.get("reporterAltContact"),
            "reporterEmail": request.data.get("reporterEmail"),
            "landmark": request.data.get("landmark"),
            "location": request.data.get("location"),
            "pincode": request.data.get("pincode"),
            "reportedDate": request.data.get("reportedDate"),
            "reportedTime": request.data.get("reportedTime"),
            "pickupDate": request.data.get("pickupDate"),
            "pickupTime": request.data.get("pickupTime"),
            "frontImage": request.FILES.get('frontImage'),
            "backImage": request.FILES.get('backImage'),
            "consentFormImage": request.FILES.get('consentFormImage')
        }
        # Pass the data dictionary to the serializer
        serializer = ReportingDetailSerializer(data=reporter_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_animal(request):
    if request.method == 'POST':
        case_id = request.data.get('case_linked')
        try:
            case= Case.objects.get(case_id=case_id)
            case_id = case.case_id
        except Case.DoesNotExist:
            return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

        # Extract the data from the request
        animal_data = {
            "case_linked": case_id,
            "animalSpecies": request.data.get("animalSpecies"),
            "animalBreed": request.data.get("animalBreed"),
            "animalAge": request.data.get("animalAge"),
            "animalTemperament": request.data.get("animalTemperament"),
            "animalGender": request.data.get("animalGender"),
            "animalPregnant": request.data.get("animalPregnant"),
            "animalMarking": request.data.get("animalMarking"),
            "animalColor": request.data.get("animalColor"),
            "animalCatchable": request.data.get("animalCatchable"),
            "animalWeight": request.data.get("animalWeight"),
            "admissionReason": request.data.get("admissionReason"),
            "animalPictures": request.FILES.get('animalPictures'),
        }

        # Pass the data dictionary to the serializer
        serializer = AnimalDetailSerializer(data=animal_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_medical_details(request):
    if request.method == 'POST':
        case_id = request.data.get('case_linked')
        try:
            case= Case.objects.get(case_id=case_id)
            case_id = case.case_id
        except Case.DoesNotExist:
            return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

        # Extract the data from the request
        medical_data = {
            "case_linked": case_id,
            "medicalHistory": request.data.get("medicalHistory"),
            "vaccinationStatus": request.data.get("vaccinationStatus"),
            "dewormed": request.data.get("dewormed"),
            "fitForSurgery": request.data.get("fitForSurgery"),
            "otherDetails": request.data.get("otherDetails"),
            "admissionDate": request.data.get("admissionDate"),
            "bloodReportImage": request.FILES.get('bloodReportImage'),
            "feedingRecordImage": request.FILES.get('feedingRecordImage'),
        }

        # Pass the data dictionary to the serializer
        serializer = MedicalDetailSerializer(data=medical_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_operation_details(request):
    if request.method == 'POST':
        case_id = request.data.get('case_linked')
        try:
            case= Case.objects.get(case_id=case_id)
            case_id = case.case_id
        except Case.DoesNotExist:
            return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

        # Extract the data from the request
        operation_data = {
            "case_linked": case_id,
            "vetName": request.data.get("vetName"),
            "operationDate": request.data.get("operationDate"),
            "operationStartTime": request.data.get("operationStartTime"),
            "operationEndTime": request.data.get("operationEndTime"),
            "operationOutcome": request.data.get("operationOutcome"),
            "medicalPrescriptionImage": request.FILES.get('medicalPrescriptionImage'),
            "treatmentRecordImage": request.FILES.get('treatmentRecordImage'),
            "organImage": request.FILES.get('organImage'),
        }
        
        # Pass the data dictionary to the serializer
        serializer = OperationDetailSerializer(data=operation_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_post_operation_details(request):
    if request.method == 'POST':
        case_id = request.data.get('case_linked')
        try:
            case= Case.objects.get(case_id=case_id)
            case_id = case.case_id
        except Case.DoesNotExist:
            return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

        # Extract the data from the request
        post_operation_data = {
            "case_linked": case_id,
            "popComment": request.data.get("popComment"),
            "popFacility": request.data.get("popFacility"),
            "popExpectedDays": request.data.get("popExpectedDays"),
            "popStartDate": request.data.get("popStartDate"),
            "popEndDate": request.data.get("popEndDate"),
            "releaseDate": request.data.get("releaseDate"),
            "euthanized": request.data.get("euthanized"),
            "comments": request.data.get("comments"),
            "popPictures": request.FILES.get('popPictures'),
            "releasePictures": request.FILES.get('releasePictures'),
        }

        # Pass the data dictionary to the serializer
        serializer = PostOperationDetailSerializer(data=post_operation_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    reporter.frontImage = request.FILES.get("frontImage", reporter.frontImage)
    reporter.backImage = request.FILES.get("backImage", reporter.backImage)
    reporter.consentFormImage = request.FILES.get("consentFormImage", reporter.consentFormImage)

    reporter.save()
    
    # Pass the existing case object to the serializer for response
    serializer = ReportingDetailSerializer(reporter)
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
    animal.animalPictures = request.FILES.get("animalPictures", animal.animalPictures)

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
    medical.feedingRecordImage = request.FILES.get("feedingRecordImage", medical.feedingRecordImage)
    medical.bloodReportImage = request.FILES.get("bloodReportImage", medical.bloodReportImage)

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
    operation.medicalPrescriptionImage = request.FILES.get("medicalPrescriptionImage", operation.medicalPrescriptionImage)
    operation.treatmentRecordImage = request.FILES.get("treatmentRecordImage", operation.treatmentRecordImage)
    operation.organImage = request.FILES.get("organImage", operation.organImage)

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
    post_operation.popPictures = request.FILES.get("popPictures", post_operation.popPictures)
    post_operation.releasePictures = request.FILES.get("releasePictures", post_operation.releasePictures)

    post_operation.save()
    
    # Pass the existing case object to the serializer for response
    serializer = PostOperationDetailSerializer(post_operation)
    return Response(serializer.data, status=status.HTTP_200_OK)
