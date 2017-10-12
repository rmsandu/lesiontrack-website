from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=20)
    #birth_date = models.DateTimeField('birthdate')

    def __str__(self):
        return self.patient_name


class Lesion(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    lesion_name = models.CharField(max_length=250) # change to Choice Field
    lesion_size = models.IntegerField(default=0)
    lesion_biopsy = models.CharField(max_length=1) # choice field, y/n

    def __str__(self):
        return self.lesion_name

class Treatment(models.Model):
    lesion = models.ForeignKey(Lesion, on_delete=models.CASCADE)
    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_name = models.CharField(max_length=10) # Change to Choice Field rfa, mwa
    treatment_type = models.CharField(max_length=10) # intervention, laparoscopy, open
    treatment_date = models.DateTimeField('treatment date')

    def __str__(self):
        return self.treatment_name
