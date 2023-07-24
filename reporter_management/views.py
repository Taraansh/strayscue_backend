from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authorization.models import Profile
from reporter_management.models import Reporter
from reporter_management.serializers import ReporterSerializer


@api_view(['GET'])
def get_all_reporters(request, email):
    try:
        profile = Profile.objects.get(email=email)
        sponsors = Reporter.objects.filter(reporter_profile_creator=profile)
        serializer = ReporterSerializer(sponsors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_reporter(request):
    reporter_data = {
        'reported_name': request.data.get('reported_name'),
        'phone_number': request.data.get('phone_number'),
        'alternate_phone_number': request.data.get('alternate_phone_number'),
        'email_id': request.data.get('email_id'),
        'reporter_profile_creator': request.data.get('reporter_profile_creator'),
        "verification_id" : request.FILES.get('verification_id')
    }

    serializer = ReporterSerializer(data=reporter_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_reporter(request, id):
    try:
        reporter = Reporter.objects.get(id=id)
    except Reporter.DoesNotExist:
        return Response({'status': 'error', 'message': 'Reporter not found'}, status=status.HTTP_404_NOT_FOUND)

    reporter.delete()
    return Response({'status': 'success'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_reporter(request, id):
    try:
        reporter = Reporter.objects.get(id=id)
    except Reporter.DoesNotExist:
        return Response({'message': 'Reporter not found'}, status=404)

    reporter.reported_name = request.data.get("reported_name", reporter.reported_name)
    reporter.phone_number = request.data.get("phone_number", reporter.phone_number)
    reporter.alternate_phone_number = request.data.get("alternate_phone_number", reporter.alternate_phone_number)
    reporter.email_id = request.data.get("email_id", reporter.email_id)
    reporter.verification_id = request.data.get("verification_id", reporter.verification_id)

    verification_id_file = request.FILES.get("verification_id")
    if verification_id_file is not None:
        reporter.verification_id = verification_id_file
    elif "verification_id" in request.data and request.data["verification_id"] == "null":
        reporter.verification_id = None

    reporter.save()
    serializer = ReporterSerializer(reporter)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)
