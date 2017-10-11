from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Patient
# Create your views here.

def index(request):
    all_patients = Patient.objects.all()
    template = loader.get_template('liverdata/index.html')
    # create dictionary for template
    context = {
        'all_patients' : all_patients,
    }
    return HttpResponse(template.render(context,request))

def detail(request,patient_id):
    return HttpResponse("<h2>Details for Patient_ID: " + str(patient_id) + "</h2>")
