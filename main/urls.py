from django.urls import path, include
from .views import PersonalDataViewSet, EducationViewSet, WorkExperienceViewSet, \
    SkillsViewSet, ProjectsViewSet, CertificationsViewSet, LanguagesViewSet, ReferencesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'personal-data', PersonalDataViewSet)
router.register(r'education', EducationViewSet)
router.register(r'work-experience', WorkExperienceViewSet)      
router.register(r'skills', SkillsViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'certifications', CertificationsViewSet)
router.register(r'languages', LanguagesViewSet)
router.register(r'references', ReferencesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]