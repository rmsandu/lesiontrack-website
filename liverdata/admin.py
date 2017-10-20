from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Patient)
#admin.site.register(Lesion)
# admin.site.register(TreatmentSession)
# admin.site.register(Treatment)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'yearofbirth', 'date_of_death', 'study_institution', 'study_name')
admin.site.register(Patient, PatientAdmin)

class LesionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'lesiontype', 'lesion_nr' ,'lesion_volume_ml','lesion_biopsy')
admin.site.register(Lesion, LesionAdmin)

class TreatmentSessionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'treatment_nr','treatment_type', 'treatmentsession_date')
admin.site.register(TreatmentSession, TreatmentSessionAdmin)

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatmentname','treatmentsession','lesion')
admin.site.register(Treatment, TreatmentAdmin)


admin.site.register(Device)
admin.site.register(RFA)
admin.site.register(IRE)
admin.site.register(MWA)
admin.site.register(TreatmentName)
admin.site.register(LesionType)
admin.site.register(Trajectory)
