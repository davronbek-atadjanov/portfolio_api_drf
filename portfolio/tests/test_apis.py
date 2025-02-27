from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from portfolio.models import PersonalInfo, Education, Experience, Tool, Project, SocialLink

class PersonalInfoAPITest(APITestCase):
    def setUp(self):
        self.personal_info = PersonalInfo.objects.create(
            full_name="Test User",
            title="Test Title",
            bio="Test Bio",
            email="test@example.com"
        )
        self.url = reverse('personalinfo-list')

    def test_get_personal_info(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], "Test User")

class ProjectAPITest(APITestCase):
    def setUp(self):
        self.tool = Tool.objects.create(
            name="Test Tool"
        )
        self.project = Project.objects.create(
            title="Test Project",
            category="Test Category",
            description="Test Description"
        )
        self.project.tools.add(self.tool)
        self.url = reverse('project-list')

    def test_get_projects(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Project")
