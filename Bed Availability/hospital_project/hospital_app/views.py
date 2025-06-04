# hospital_app/views.py

from rest_framework import generics
from .models import Hospital
from .serializers import HospitalSerializer

class HospitalListView(generics.ListAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        district = self.request.query_params.get('district')
        if district:
            return Hospital.objects.filter(district=district)
        return Hospital.objects.all()

class HospitalDetailView(generics.RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
