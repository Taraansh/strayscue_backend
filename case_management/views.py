from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authorization.models import Profile
from case_management.serializers import CaseSerializer, ReportingDetailSerializer, AnimalDetailSerializer, MedicalDetailSerializer, OperationDetailSerializer
from case_management.models import Case


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
    serializer = CaseSerializer(data=request.data)
    if serializer.is_valid():
        case = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_case(request, case_id):
    try:
        case = Case.objects.get(case_id=case_id)
    except Case.DoesNotExist:
        return Response({"error": "Case not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CaseSerializer(case, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializer = OperationDetailSerializer(data=post_operation_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
