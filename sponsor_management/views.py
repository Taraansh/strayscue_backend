from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sponsor_management.models import Sponsor
from sponsor_management.serializers import SponsorSerializer

@api_view(['POST'])
def upload_sponsor(request):
    sponsor_data = {
        'sponsor_name': request.data.get('sponsor_name'),
        'animal_fit_for_surgery': request.data.get('animal_fit_for_surgery'),
        'sponsor_amount': request.data.get('sponsor_amount'),
        'start_date': request.data.get('start_date'),
        'end_date': request.data.get('end_date'),
    }

    # Get the sponsor logo (image) from the request data
    sponsor_logo = request.FILES.get('sponsor_logo')
    if sponsor_logo:
        sponsor_data['sponsor_logo'] = sponsor_logo

    serializer = SponsorSerializer(data=sponsor_data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_sponsors(request):
    sponsors = Sponsor.objects.all()
    serializer = SponsorSerializer(sponsors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_sponsor(request, sponsor_name):
    sponsors = Sponsor.objects.filter(sponsor_name__icontains=sponsor_name)
    serializer = SponsorSerializer(sponsors, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_sponsor(request, id):
    try:
        sponsor = Sponsor.objects.get(id=id)
    except Sponsor.DoesNotExist:
        return Response({'status': 'error', 'message': 'Sponsor not found'}, status=404)

    serializer = SponsorSerializer(sponsor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_sponsor(request, id):
    try:
        sponsor = Sponsor.objects.get(id=id)
    except Sponsor.DoesNotExist:
        return Response({'status': 'error', 'message': 'Sponsor not found'}, status=404)

    sponsor.delete()
    return Response({'status': 'success'})