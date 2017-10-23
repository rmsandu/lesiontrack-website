from django.contrib import admin
from .models import *

# Register your models here.

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

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'needle_name')
admin.site.register(Device, DeviceAdmin)

class MWAAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'device', 'power', 'time_duration')
admin.site.register(MWA, MWAAdmin)

class RFAAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'device', 'power', 'time_duration')
admin.site.register(RFA, RFAAdmin)

class IREAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'device', 'power', 'time_duration')
admin.site.register(IRE, MWAAdmin)

class TrajectoryAdmin(admin.ModelAdmin):
    list_display = ('parent_trajectory', 'entrypoint_planned','targetpoint_planned', 'entrypoint_measured', 'targetpoint_measured','trajectory_nr')
admin.site.register(Trajectory, TrajectoryAdmin)

class TPErrorsAdmin(admin.ModelAdmin):
    list_display = ('trajectory', 'lateralerror', 'longerror', 'angularerror', 'residualerror')
admin.site.register(TPErrors,TPErrorsAdmin)


admin.site.register(TreatmentName)
admin.site.register(LesionType)
