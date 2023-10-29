from rest_framework import serializers
from ngo_management.models import Ngo
from case_management.serializers import CaseSerializer


class NgoSerializer(serializers.ModelSerializer):
    # Use SerializerMethodField for custom serialization
    cases = serializers.SerializerMethodField()

    def get_cases(self, obj):
        # Retrieve the first 15 cases for the NGO
        first_15_cases = obj.cases.all()[:15]

        # Serialize the cases using CaseSerializer
        case_serializer = CaseSerializer(first_15_cases, many=True)

        return {
            'count': obj.cases.count(),  # Total count of cases
            'cases': case_serializer.data  # Serialized case data
        }

    class Meta:
        model = Ngo
        fields = ["id", "ngo_name", "darpan_id", "description", "mission_statement", "ngo_address", 'offline_cases', "helpline_number",
                  "alternate_helpline_number", "facebook_page", "linkedin_page", "instagram_page", "twitter_page",
                  "ngo_email", "ngo_website", "ngo_logo", "ngo_profile_creator", "cases"]
