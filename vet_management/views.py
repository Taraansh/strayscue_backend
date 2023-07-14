from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vet_management.models import Vet
from vet_management.serializers import VetSerializer

@api_view(['POST'])
def upload_vet(request):
    vet_data = {
        'vet_name': request.data.get('vet_name'),
        'registration_id': request.data.get('registration_id'),
    }

    # Get the vet certification (image) from the request data
    vet_certification = request.FILES.get('vet_certification')
    if vet_certification:
        vet_data['vet_certification'] = vet_certification

    # Get the verification ID (image) from the request data
    verification_id = request.FILES.get('verification_id')
    if verification_id:
        vet_data['verification_id'] = verification_id

    serializer = VetSerializer(data=vet_data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_vets(request):
    vets = Vet.objects.all()
    serializer = VetSerializer(vets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_vet(request, vet_name):
    vets = Vet.objects.filter(vet_name__icontains=vet_name)
    serializer = VetSerializer(vets, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_vet(request, id):
    try:
        vet = Vet.objects.get(pk=id)
    except Vet.DoesNotExist:
        return Response({'status': 'error', 'message': 'Vet not found'}, status=404)

    serializer = VetSerializer(vet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_vet(request, id):
    try:
        vet = Vet.objects.get(pk=id)
    except Vet.DoesNotExist:
        return Response({'status': 'error', 'message': 'Vet not found'}, status=404)

    vet.delete()
    return Response({'status': 'success'})
