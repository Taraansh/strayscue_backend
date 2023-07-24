from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authorization.models import Profile
from ngo_management.models import Ngo
from ngo_management.serializers import NgoSerializer

# Create your views here.

@api_view(['GET'])
def get_all_ngos(request, email):
    try:
        profile = Profile.objects.get(email=email)
        ngo = Ngo.objects.filter(ngo_profile_creator=profile)
        serializer = NgoSerializer(ngo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_ngo(request):
    ngo_data = {
        'ngo_name': request.data.get('ngo_name'),
        'darpan_id': request.data.get('darpan_id'),
        'description': request.data.get('description'),
        'mission_statement': request.data.get('mission_statement'),
        'helpline_number': request.data.get('helpline_number'),
        'alternate_helpline_number': request.data.get('alternate_helpline_number'),
        'facebook_page': request.data.get('facebook_page'),
        'linkedin_page': request.data.get('linkedin_page'),
        'instagram_page': request.data.get('instagram_page'),
        'twitter_page': request.data.get('twitter_page'),
        'ngo_email': request.data.get('ngo_email'),
        'ngo_website': request.data.get('ngo_website'),
        "ngo_logo" : request.FILES.get('ngo_logo'),
        'ngo_profile_creator': request.data.get('ngo_profile_creator'),
    }

    serializer = NgoSerializer(data=ngo_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_ngo(request, id):
    try:
        ngo = Ngo.objects.get(id=id)
    except Ngo.DoesNotExist:
        return Response({'status': 'error', 'message': 'Ngo not found'}, status=status.HTTP_404_NOT_FOUND)

    ngo.delete()
    return Response({'status': 'success'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_ngo(request, id):
    try:
        ngo = Ngo.objects.get(id=id)
    except Ngo.DoesNotExist:
        return Response({'message': 'Ngo not found'}, status=status.HTTP_404_NOT_FOUND)

    ngo.ngo_name = request.data.get('ngo_name', ngo.ngo_name)
    ngo.darpan_id = request.data.get('darpan_id', ngo.darpan_id)
    ngo.description = request.data.get('description', ngo.description)
    ngo.mission_statement = request.data.get('mission_statement', ngo.mission_statement)
    ngo.helpline_number = request.data.get('helpline_number', ngo.helpline_number)
    ngo.alternate_helpline_number = request.data.get('alternate_helpline_number', ngo.alternate_helpline_number)
    ngo.facebook_page = request.data.get('facebook_page', ngo.facebook_page)
    ngo.linkedin_page = request.data.get('linkedin_page', ngo.linkedin_page)
    ngo.instagram_page = request.data.get('instagram_page', ngo.instagram_page)
    ngo.twitter_page = request.data.get('twitter_page', ngo.twitter_page)
    ngo.ngo_email = request.data.get('ngo_email', ngo.ngo_email)
    ngo.ngo_website = request.data.get('ngo_website', ngo.ngo_website)

    ngo_logo_file = request.FILES.get("ngo_logo")
    if ngo_logo_file is not None:
        ngo.ngo_logo = ngo_logo_file
    elif "ngo_logo" in request.data and request.data["ngo_logo"] == "null":
        ngo.ngo_logo = None

    ngo.save()
    serializer = NgoSerializer(ngo)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)
