from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=20)
    # study_name = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name


class Lesion(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    lesion_name = models.CharField(max_length=250) # change to Choice Field
    lesion_size = models.DecimalField(max_digits=10, decimal_places=2)
    lesion_biopsy = models.BooleanField(default=False) # choice field, y/n

    def __str__(self):
        return  'Patient Name: ' + str(self.patient) + '; Lesion: ' + self.lesion_name

class Treatment(models.Model):
    lesion = models.ForeignKey(Lesion, on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_type = models.CharField(max_length=10) # intervention, laparoscopy, open
    treatment_date = models.DateTimeField('treatment date')
    treatment_name = models.CharField(choices=(
                ('RFA', "Radio-frequency Ablation"),
                ('MWA', "Microwave Ablation"),
                ('IRE', "Irreversible electroporration"),
                ('R', "Resection"),
                ('T',"TACE"),
                ('C', "Chemotherapy")
            ),
            max_length=3)

    def __str__(self):
        return self.treatment_name
