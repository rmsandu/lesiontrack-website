from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from django.views import generic
from .models import Patient, Lesion, Treatment


def index(request):
    return render(request, 'liverdata/index.html')

def patient_list(request):
    all_patients = Patient.objects.all()
    return render(request, 'liverdata/patient_list.html', {'all_patients' : all_patients})

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'liverdata/patient_detail.html', {'patient' : patient})

def lesion_detail(request, lesion_id):
    lesion = get_object_or_404(Lesion, pk=lesion_id)
    return render(request, 'liverdata/lesion_detail.html', {'lesion': lesion})
