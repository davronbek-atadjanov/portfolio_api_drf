from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import PersonalInfo, Project
from portfolio.serializers import PersonalInfoSerializer, ProjectSerializer

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.personal_info = PersonalInfo.objects.create(
            full_name="Test User",
            title="Test Title",
            bio="Test Bio",
            email="test@example.com"
        )
        self.project = Project.objects.create(
            title="Test Project",
            category="Test Category",
            description="Test Description"
        )

    def test_personal_info_viewset(self):
        response = self.client.get(reverse('personalinfo-list'))
        personal_info = PersonalInfo.objects.first()
        serializer = PersonalInfoSerializer(personal_info)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_project_viewset(self):
        response = self.client.get(reverse('project-list'))
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200) 