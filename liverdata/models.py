from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=20)
    gender = models.CharField(choices=(('F','Female'), ('M','Male')), max_length=1, default='F')
    study_site = models.CharField(max_length=100, default='Bern')
    study_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.patient_name


class Lesion(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    lesion_name = models.CharField(max_length=250) # change to Choice Field
    lesion_size = models.DecimalField(max_digits=10, decimal_places=2)
    lesion_biopsy = models.BooleanField(default=False) # choice field, y/n

    def __str__(self):
        return  'Patient Name: ' + str(self.patient) + '; Lesion: ' + self.lesion_name

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
        return 'Patient:' + str(self.patient) + '; TreatmentSession: ' + self.treatment_nr

class Treatment(models.Model):
    lesion = models.ForeignKey(Lesion, on_delete=models.CASCADE)
    treatmentsession = models.ForeignKey(TreatmentSession, on_delete = models.CASCADE)
    treatment_name = models.CharField(max_length=100) # Chemotherapy,resection,embolization

    def __str__(self):
        return 'Patient:' + str(self.patient) + '; TreatmentSession: ' + self.treatmentsession

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

class RFA(models.Model):
    treatment = models.ForeignKey(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'Treamtent Name:' + RFA.__name__

class IRE(models.Model):
    treatment = models.ForeignKey(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'TreatmentName:' +  IRE.__name__
