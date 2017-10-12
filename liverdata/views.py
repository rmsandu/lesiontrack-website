from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from .models import Patient, Lesion, Treatment
# Create your views here.

def index(request):
    all_patients = Patient.objects.all()
    return render(request, 'liverdata/index.html', {'all_patients' : all_patients})

def detail(request,patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'liverdata/lesion_detail.html', {'patient' : patient})

def detail1(request,patient_id, lesion_id):
        try:
            lesion = Lesion.objects.get(pk=lesion_id)
            patient = Patient.objects.get(pk=patient_id)
        except Lesion.DoesNotExist:
            raise Http404("Treatment does not exist")
        return render(request, 'liverdata/treatment_detail.html', {'patient' : patient, 'lesion': lesion})
