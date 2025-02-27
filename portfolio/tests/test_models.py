from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from portfolio.models import PersonalInfo, Education, Experience, Tool, Project, SocialLink, Contact
from django.core.exceptions import ValidationError

class PersonalInfoModelTest(TestCase):
    def setUp(self):
        self.personal_info = PersonalInfo.objects.create(
            full_name="Test User",
            title="Test Title",
            bio="Test Bio",
            email="test@example.com"
        )

    def test_personal_info_creation(self):
        self.assertEqual(self.personal_info.full_name, "Test User")
        self.assertEqual(self.personal_info.title, "Test Title")

    def test_single_instance(self):
        # setUp da bitta PersonalInfo yaratilgan, 
        # shuning uchun yangi yaratishda xato bo'lishi kerak
        with self.assertRaises(ValidationError):
            PersonalInfo.objects.create(
                full_name="Second User",
                title="Second Title",
                bio="Second Bio",
                email="second@example.com"
            )

class EducationModelTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Test University",
            degree="Test Degree",
            year_start="2020",
            year_end="2024"
        )

    def test_education_creation(self):
        self.assertEqual(self.education.institution, "Test University")
        self.assertEqual(self.education.year_start, "2020")

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            address="Andijan, Uzbekistan",
            email="test@example.com",
            phone="88 972 10 03",
            birth_date="1999-08-02"
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.address, "Andijan, Uzbekistan")
        self.assertEqual(self.contact.phone, "88 972 10 03")

    def test_single_instance(self):
        with self.assertRaises(ValidationError):
            Contact.objects.create(
                address="Test Address",
                email="another@example.com",
                phone="99 999 99 99",
                birth_date="1999-08-02"
            ) 