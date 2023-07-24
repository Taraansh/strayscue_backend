from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authorization.models import Profile
from vet_management.models import Vet
from vet_management.serializers import VetSerializer


@api_view(['GET'])
def get_all_vets(request, email):
    try:
        profile = Profile.objects.get(email=email)
        vets = Vet.objects.filter(vet_profile_creator = profile)
        serializer = VetSerializer(vets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_vet(request):
    vet_data = {
        'vet_name': request.data.get('vet_name'),
        'registration_id': request.data.get('registration_id'),
        'vet_profile_creator' : request.data.get('vet_profile_creator'),
        'vet_certification' : request.FILES.get('vet_certification'),
        'verification_id' : request.FILES.get('verification_id'),
    }

    serializer = VetSerializer(data=vet_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_vet(request, id):
    try:
        vet = Vet.objects.get(id=id)
    except Vet.DoesNotExist:
        return Response({'status': 'error', 'message': 'Vet not found'}, status=404)

    vet.delete()
    return Response({'status': 'success'})


@api_view(['PUT'])
def update_vet(request, id):
    try:
        vet = Vet.objects.get(id=id)
    except Vet.DoesNotExist:
        return Response({'status': 'error', 'message': 'Vet not found'}, status=status.HTTP_404_NOT_FOUND)

    vet.vet_name = request.data.get('vet_name', vet.vet_name)
    vet.registration_id = request.data.get('registration_id', vet.registration_id)

    vet_certification_file = request.FILES.get("vet_certification")
    if vet_certification_file is not None:
        vet.vet_certification = vet_certification_file
    elif "vet_certification" in request.data and request.data["vet_certification"] == "null":
        vet.vet_certification = None

    verification_id_file = request.FILES.get("verification_id")
    if verification_id_file is not None:
        vet.verification_id = verification_id_file
    elif "verification_id" in request.data and request.data["verification_id"] == "null":
        vet.verification_id = None

    vet.save()
    serializer = VetSerializer(vet)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)
