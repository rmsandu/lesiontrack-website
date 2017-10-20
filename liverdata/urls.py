from django.conf.urls import url
from . import views

app_name = 'liverdata'

urlpatterns = [
    # /liverdata/
    url(r'^$', views.index, name='index'),
    # /liverdata/713/
    url(r'patient_list', views.patient_list, name='patient_list'),
    url(r'patient/(?P<patient_id>[0-9]+)/$', views.patient_detail, name='patient_detail'),

    # /liverdata/patientxyx/lesionxyz/
    url(r'lesion/(?P<lesion_id>[0-9]+)/$', views.lesion_detail, name='lesion_detail')
]
