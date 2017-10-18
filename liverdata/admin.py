from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Lesion)
admin.site.register(Treatment)
admin.site.register(TreatmentSession)
admin.site.register(Device)
admin.site.register(RFA)
admin.site.register(IRE)
admin.site.register(MWA)
admin.site.register(TreatmentName)
admin.site.register(LesionType)
