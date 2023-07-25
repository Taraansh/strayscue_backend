from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authorization.models import Profile
from authorization.serializers import ProfileSerializer
from django.contrib.auth.hashers import check_password
from authorization.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(["POST"])
def login(request):
    if request.method == "POST":
        email = request.data.get('email')
        password = request.data.get('password')
        user = Profile.objects.filter(email=email).first()

        if user is not None and check_password(password, user.password):
            serializer = ProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(["PUT"])
def password_change(request, email):
    user = get_object_or_404(Profile, email=email)
    if request.method == "PUT":
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        # hashed_old_password = make_password(password)
        hashed_new_password = make_password(new_password)
        # if (hashed_old_password == user.password):
        if user.check_password(password):
            user.password = hashed_new_password
            user.save()
            return Response({"detail": "Password Changed Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid old password"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["PUT"])
def update_profile(request, email):
    try:
        user = Profile.objects.get(email=email)
    except Profile.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user.username = request.data.get("username", user.username)

    profile_photo_file = request.FILES.get("profilePhoto")
    if profile_photo_file is not None:
        user.profilePhoto = profile_photo_file
    elif "profilePhoto" in request.data and request.data["profilePhoto"] == "null":
        user.profilePhoto = None
    
    user.save()
    serializer = ProfileSerializer(user)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_profile(request, email):
    try:
        user = Profile.objects.get(email=email)
    except Profile.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_routes(request):
    """returns a view containing all the possible routes"""
    routes = [
        '/token',
        '/token/refresh'
    ]
    return Response(routes)