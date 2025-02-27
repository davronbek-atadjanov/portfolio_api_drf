from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response


class PersonalInfoView(RetrieveAPIView):
    serializer_class = PersonalInfoSerializer
    def get_object(self):
        return PersonalInfo.objects.first()

class ContactView(RetrieveAPIView):
    serializer_class = ContactSerializer
    
    def get_object(self):
        return Contact.objects.first()

class EducationViewSet(ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ToolViewSet(ReadOnlyModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class SocialLinkViewSet(ReadOnlyModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

class SkillCategoryViewSet(ReadOnlyModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer

class TechnicalSkillViewSet(ReadOnlyModelViewSet):
    queryset = TechnicalSkill.objects.all()
    serializer_class = TechnicalSkillSerializer
    
    def get_queryset(self):
        queryset = TechnicalSkill.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset

class HobbyViewSet(ReadOnlyModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
