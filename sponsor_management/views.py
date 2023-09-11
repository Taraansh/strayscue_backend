from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authorization.models import Profile
from sponsor_management.models import Sponsor
from sponsor_management.serializers import SponsorSerializer


@api_view(['GET'])
def get_all_sponsors(request, email):
    try:
        profile = Profile.objects.get(email=email)
        sponsors = Sponsor.objects.filter(sponsor_profile_creator=profile)
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_sponsor(request):
    sponsor_data = {
        'sponsor_name': request.data.get('sponsor_name'),
        'animal_fit_for_surgery': request.data.get('animal_fit_for_surgery'),
        'sponsor_amount': request.data.get('sponsor_amount'),
        'start_date': request.data.get('start_date'),
        'end_date': request.data.get('end_date'),
        'sponsor_profile_creator': request.data.get('sponsor_profile_creator'),
        "sponsor_logo" : request.FILES.get('sponsor_logo')
    }

    serializer = SponsorSerializer(data=sponsor_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_sponsor(request, id):
    try:
        sponsor = Sponsor.objects.get(id=id)
    except Sponsor.DoesNotExist:
        return Response({'status': 'error', 'message': 'Sponsor not found'}, status=status.HTTP_404_NOT_FOUND)

    sponsor.delete()
    return Response({'status': 'success'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_sponsor(request, id):
    try:
        sponsor = Sponsor.objects.get(id=id)
    except Sponsor.DoesNotExist:
        return Response({'message': 'Sponsor not found'}, status=status.HTTP_404_NOT_FOUND)

    sponsor.sponsor_name = request.data.get("sponsor_name", sponsor.sponsor_name)
    sponsor.animal_fit_for_surgery = request.data.get("animal_fit_for_surgery", sponsor.animal_fit_for_surgery)
    sponsor.sponsor_amount = request.data.get("sponsor_amount", sponsor.sponsor_amount)
    sponsor.start_date = request.data.get("start_date", sponsor.start_date)
    sponsor.end_date = request.data.get("end_date", sponsor.end_date)

    sponsor_logo_file = request.FILES.get("sponsor_logo")
    if sponsor_logo_file is not None:
        sponsor.sponsor_logo = sponsor_logo_file
    elif "sponsor_logo" in request.data and request.data["sponsor_logo"] == "null":
        sponsor.sponsor_logo = None

    sponsor.save()
    serializer = SponsorSerializer(sponsor)
    return Response(serializer.data, status=status.HTTP_200_OK)
