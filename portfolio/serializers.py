from rest_framework import serializers
from .models import *

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tools = ToolSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

# Boshqa modellar uchun ham shunga o'xshash serializer lar... 