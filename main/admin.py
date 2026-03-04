from django.contrib import admin
from .models import Personal_Data, Education, Work_Experience, \
    Skills, Projects, Certifications, Languages, References
    
# Register your models here.
admin.site.register(Personal_Data)
admin.site.register(Education)
admin.site.register(Work_Experience)
admin.site.register(Skills)
admin.site.register(Projects)   
admin.site.register(Certifications)
admin.site.register(Languages)
admin.site.register(References)