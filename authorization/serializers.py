from rest_framework import serializers
from authorization.models import Profile
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ["id", "username", "user_contact", "email"]
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            password = validated_data.pop('password')
            hashed_password = make_password(password)
            profile = Profile(**validated_data)
            profile.password = hashed_password
            profile.save()
            return profile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        return token