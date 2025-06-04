# hospital_app/serializers.py

from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'district', 'total_beds', 'vacant_beds']
