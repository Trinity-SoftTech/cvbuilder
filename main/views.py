from django.shortcuts import render

from rest_framework import viewsets

from .models import Personal_Data, Education, Work_Experience, \
    Skills, Projects, Certifications, Languages, References
from .serializers import PersonalDataSerializer, EducationSerializer, \
    WorkExperienceSerializer, SkillsSerializer, ProjectsSerializer, \
    CertificationsSerializer, LanguagesSerializer, ReferencesSerializer
    
    
# Create your views here.
class PersonalDataViewSet(viewsets.ModelViewSet):
    queryset = Personal_Data.objects.all()
    serializer_class = PersonalDataSerializer
    
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = Work_Experience.objects.all()
    serializer_class = WorkExperienceSerializer
    
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    
class CertificationsViewSet(viewsets.ModelViewSet):
    queryset = Certifications.objects.all()
    serializer_class = CertificationsSerializer
    
class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
    
class ReferencesViewSet(viewsets.ModelViewSet):
    queryset = References.objects.all()
    serializer_class = ReferencesSerializer
    

