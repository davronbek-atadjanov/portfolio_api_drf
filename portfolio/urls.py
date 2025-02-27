from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('education', EducationViewSet)
router.register('experience', ExperienceViewSet)
router.register('projects', ProjectViewSet)
router.register('tools', ToolViewSet)
router.register('social-links', SocialLinkViewSet)
router.register('skill-categories', SkillCategoryViewSet)
router.register('technical-skills', TechnicalSkillViewSet)
router.register('hobbies', HobbyViewSet)
router.register('languages', LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('personal-info/', PersonalInfoView.as_view(), name='personal-info'),
    path('contact/', ContactView.as_view(), name='contact'),
] 