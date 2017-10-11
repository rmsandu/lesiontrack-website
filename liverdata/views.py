from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
# Create your views here.

def index(request):
    all_patients = Patient.objects.all()
    html = ''
    for patient in all_patients:
        url = '/liverdata/' + str(patient.id) + '/'
        html += '<a href="' + url + '" >' + patient.patient_name + '</a><br>'
    return HttpResponse(html)

def detail(request,patient_id):
    return HttpResponse("<h2>Details for Patient_ID: " + str(patient_id) + "</h2>")
