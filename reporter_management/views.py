from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reporter_management.models import Reporter
from reporter_management.serializers import ReporterSerializer

@api_view(['POST'])
def upload_reporter(request):
    reporter_data = {
        'reported_name': request.data.get('reported_name'),
        'phone_number': request.data.get('phone_number'),
        'alternate_phone_number': request.data.get('alternate_phone_number'),
        'email_id': request.data.get('email_id'),
    }

    # Get the reporter logo (image) from the request data
    verification_id = request.FILES.get('verification_id')
    if verification_id:
        reporter_data['verification_id'] = verification_id

    serializer = ReporterSerializer(data=reporter_data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_reporters(request):
    reporters = Reporter.objects.all()
    serializer = ReporterSerializer(reporters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_reporter(request, reported_name):
    reporter = Reporter.objects.filter(reported_name__icontains=reported_name)
    serializer = ReporterSerializer(reporter, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_reporter(request, id):
    try:
        reporter = Reporter.objects.get(id=id)
    except Reporter.DoesNotExist:
        return Response({'status': 'error', 'message': 'Reporter not found'}, status=404)

    serializer = ReporterSerializer(reporter, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_reporter(request, id):
    try:
        reporter = Reporter.objects.get(id=id)
    except Reporter.DoesNotExist:
        return Response({'status': 'error', 'message': 'Reporter not found'}, status=404)

    reporter.delete()
    return Response({'status': 'success'})