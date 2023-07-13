from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authorization.models import Profile
from authorization.serializers import ProfileSerializer
from django.contrib.auth.hashers import check_password
from authorization.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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
        

@api_view(['GET'])
def get_routes(request):
    """returns a view containing all the possible routes"""
    routes = [
        '/token',
        '/token/refresh'
    ]
    return Response(routes)