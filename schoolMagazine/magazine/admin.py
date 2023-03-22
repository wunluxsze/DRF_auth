from django.contrib import admin
from .models import Students, SchoolSubj, SchoolClass
# Register your models here.

admin.site.register(Students)
admin.site.register(SchoolClass)
admin.site.register(SchoolSubj)