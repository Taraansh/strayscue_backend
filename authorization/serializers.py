from rest_framework import serializers
from authorization.models import Profile
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProfileSerializer(serializers.ModelSerializer):
    ngo_name = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        # fields = ["id", "username", "user_contact", "email", "groups", "is_active", "is_superuser", "ngo_linked_with_this_user", "ngo_name", "profilePhoto", "type_of_user_in_ngo", "user_contact"]
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
        
    def get_ngo_name(self, obj):
        return f"{obj.ngo_linked_with_this_user}"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['type_of_user_in_ngo'] = user.type_of_user_in_ngo
        return token