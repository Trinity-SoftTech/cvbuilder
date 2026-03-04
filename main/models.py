from django.db import models

# Create your models here.
class Personal_Data(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Education(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='education')
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution_name}"
    
class Work_Experience(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='work_experience')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
class Skills(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.skill_name
    
class Projects(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    technologies_used = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.project_name
    
class Certifications(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='certifications')
    certification_name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.certification_name
    
class Languages(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.language_name
    
class References(models.Model):
    personal_data = models.ForeignKey(Personal_Data, on_delete=models.CASCADE, related_name='references')
    reference_name = models.CharField(max_length=255)
    contact_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.reference_name