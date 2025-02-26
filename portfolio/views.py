from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

class PersonalInfoViewSet(ReadOnlyModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({})

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
