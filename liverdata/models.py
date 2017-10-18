from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=20)
    gender = models.CharField(choices=(('F','Female'), ('M','Male')), max_length=1, default='F')
    study_site = models.CharField(max_length=100, default='Bern')
    study_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.patient_name

class LesionType(models.Model):
    lesiontype_name = models.CharField(max_length=50)
    lesiontype_shortname = models.CharField(max_length=5)

    def __str__(self):
        return "{0} ({1})".format(self.lesiontype_name, self.lesiontype_shortname)

class Lesion(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    lesion_size = models.DecimalField(max_digits=10, decimal_places=2)
    lesion_biopsy = models.BooleanField(default=False) # choice field, y/n
    lesiontype = models.ForeignKey(LesionType, on_delete = models.PROTECT, null=True, blank=False)

    def __str__(self):
        return  'Patient Name: ' + str(self.patient) + '; Lesion: ' + str(self.lesiontype)

class TreatmentSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    treatmentsession_date = models.DateTimeField('Treatment Session Date:')
    treatment_nr = models.PositiveIntegerField()
    treatment_type = models.CharField(choices=(
        ('IR', 'Intervention'),
        ('LP', 'Laparoscopy'),
        ('Open', 'Surgery'),
        ('Resection', 'Resection'),
        ('Chemotherapy', 'Chemotherapy')
        ),
        max_length=10) # intervention, laparoscopy, open, Resection

    def __str__(self):
        return 'Patient:' + str(self.patient) + '; TreatmentSession: ' + str(self.treatment_nr)

class TreatmentName(models.Model):
    treatment_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.short_name

class Treatment(models.Model):
    treatmentsession = models.ForeignKey(TreatmentSession, on_delete = models.CASCADE)
    lesion = models.ForeignKey(Lesion, on_delete=models.CASCADE)
    treatmentname = models.ForeignKey(TreatmentName, on_delete = models.PROTECT, null=True)

    def __str__(self):
        return 'Lesion:' + str(self.lesion) + '; TreatmentSession: ' + str(self.treatmentsession)

class Device(models.Model):
    manufacturer = models.CharField(max_length=200)
    needle_name = models.CharField(max_length=200)
    others = models.TextField()

    def __str__(self):
        return 'Device Name: ' + self.manufacturer + 'Needle_Name:' + self.needle_name


class MWA(models.Model):
    treatment = models.ForeignKey(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'TreatmentName:' + MWA.__name__

    class Meta:
        verbose_name_plural = "MWA"

class RFA(models.Model):
    treatment = models.ForeignKey(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'Treamtent Name:' + RFA.__name__

    class Meta:
        verbose_name_plural = "RFA"

class IRE(models.Model):
    treatment = models.ForeignKey(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'TreatmentName:' +  IRE.__name__

    class Meta:
        verbose_name_plural = "IRE"
