from rest_framework import serializers
from .models import Personal_Data, Education, Work_Experience, \
    Skills, Projects, Certifications, Languages, References
    
class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Data
        fields = '__all__'
        
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Experience
        fields = '__all__'
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        
class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = '__all__'
        
class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'
        
class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = '__all__'
        
    