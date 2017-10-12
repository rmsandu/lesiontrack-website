from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Patient, Lesion, Treatment
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
    return render(request, 'liverdata/lesion_detail.html', {'patient' : patient})

def detail1(request, lesion_id):
        try:
            lesion = Lesion.objects.get(pk=lesion_id)
            patient = Patient.objects.get(pk=patient_id)
        except Lesion.DoesNotExist:
            raise Http404("Treatment does not exist")
        return render(request, 'liverdata/treatment_detail.html', {'lesion' : lesion})
