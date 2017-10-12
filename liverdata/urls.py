from django.conf.urls import url
from . import views

urlpatterns = [
    # /liverdata/
    url(r'^$', views.index, name='index'),
    # /liverdata/713/
    url(r'^(?P<patient_id>[0-9]+)/$', views.detail, name='patientdetail'),
    # /liverdata/patientxyx/lesionxyz/
    url(r'^(?P<patient_id>[0-9]+)/(?P<lesion_id>[0-9]+)/$', views.detail1, name='lesiondetail')
]
