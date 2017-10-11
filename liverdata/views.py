from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Patient
# Create your views here.

def index(request):
    all_patients = Patient.objects.all()
    #context = {'all_patients' : all_patients}
    return render(request, 'liverdata/index.html', {'all_patients' : all_patients})

def detail(request,patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return render(request, 'liverdata/detail.html', {'patient' : patient})
