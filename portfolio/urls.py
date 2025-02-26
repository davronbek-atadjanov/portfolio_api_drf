from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('personal-info', PersonalInfoViewSet)
router.register('education', EducationViewSet)
router.register('experience', ExperienceViewSet)
router.register('projects', ProjectViewSet)
router.register('tools', ToolViewSet)
router.register('social-links', SocialLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 