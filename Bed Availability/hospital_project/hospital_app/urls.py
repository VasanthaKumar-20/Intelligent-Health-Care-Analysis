# hospital_app/urls.py

from django.urls import path
from .views import HospitalListView, HospitalDetailView

urlpatterns = [
    path('api/hospitals/', HospitalListView.as_view(), name='hospital-list'),
    path('api/hospitals/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
]
