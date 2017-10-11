from django.contrib import admin
from .models import Patient, Treatment, Lesion

# Register your models here.
admin.site.register(Patient)
admin.site.register(Lesion)
admin.site.register(Treatment)
