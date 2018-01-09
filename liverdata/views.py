from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from django.views import generic
from .models import Patient, Lesion, Treatment, MWA, RFA, IRE, Trajectory, TPErrors,TreatmentSession


def index(request):
    num_patients = Patient.objects.all().count()
    num_lesions = Lesion.objects.all().count()
    num_rfa_ablations = RFA.objects.all().count()
    num_ir = TreatmentSession.objects.filter(treatment_type__exact='IR').count()
    return render(request, 'liverdata/index.html', context = {'num_patients':num_patients, 'num_lesions': num_lesions, 'num_rfa_ablations': num_rfa_ablations, 'num_ir':num_ir})

def patient_list(request):
    all_patients = Patient.objects.all()
    return render(request, 'liverdata/patient_list.html', {'all_patients' : all_patients})

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'liverdata/patient_detail.html', {'patient' : patient})

def lesion_detail(request, lesion_id):
    lesion = get_object_or_404(Lesion, pk=lesion_id)
    return render(request, 'liverdata/lesion_detail.html', {'lesion': lesion})
