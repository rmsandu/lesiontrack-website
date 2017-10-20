from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=20)
    # gender = models.CharField(choices=(('F','Female'), ('M','Male')), max_length=1, blank=True)
    yearofbirth = models.PositiveIntegerField(null= True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    study_institution = models.CharField(max_length=100, default='Bern', blank=True) #optional field
    study_name = models.CharField(max_length=100, default='ClinicalStudyBern', blank=True) # optional field


    def __str__(self):
        return self.patient_name

class LesionType(models.Model):
    lesiontype_name = models.CharField(max_length=50)
    lesiontype_shortname = models.CharField(max_length=5)

    def __str__(self):
        return "{0}".format(self.lesiontype_shortname)

class Lesion(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    lesiontype = models.ForeignKey(LesionType, on_delete = models.PROTECT, null=True, blank=False) # can be non-existent, but not blank
    lesion_volume_ml = models.DecimalField(max_digits=10, decimal_places=2, blank=True) #optional field
    lesion_biopsy = models.BooleanField(default=False) # choice field, y/n


    def __str__(self):
        return "{0} - {1} - {2}".format(self.patient, self.lesiontype, self.id)


class TreatmentSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.PROTECT, blank=True, null=True)
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
        return "{0} - {1} - {2}".format(self.patient, self.treatment_nr, self.treatment_type)


class TreatmentName(models.Model):
    treatment_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = "TreatmentName"


class Treatment(models.Model):
    treatmentsession = models.ForeignKey(TreatmentSession, on_delete = models.CASCADE)
    treatmentname = models.ForeignKey(TreatmentName, on_delete = models.PROTECT, null=True, blank=False)
    lesion = models.ForeignKey(Lesion, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - ({1}) : {2}".format(self.treatmentsession.patient.patient_name, self.treatmentsession.treatmentsession_date, self.treatmentname)



class Device(models.Model):
    manufacturer = models.CharField(max_length=200)
    needle_name = models.CharField(max_length=200)
    others = models.TextField()

    def __str__(self):
        return "{0} ({1})".format(self.manufacturer, self.needle_name)

    class Meta:
        verbose_name_plural = "Device"



class MWA(models.Model):
    treatment = models.OneToOneField(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'TreatmentName:' + MWA.__name__

    class Meta:
        verbose_name_plural = "MWA"

class RFA(models.Model):
    treatment = models.OneToOneField(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'Treamment Name:' + RFA.__name__

    class Meta:
        verbose_name_plural = "RFA"

class IRE(models.Model):
    treatment = models.OneToOneField(Treatment, blank=True, null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    power = models.PositiveIntegerField() # power or temperature applied
    time_duration = models.DurationField()

    def __str__(self):
        return 'TreatmentName:' +  IRE.__name__

    class Meta:
        verbose_name_plural = "IRE"
