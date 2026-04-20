from rest_framework import serializers
from .models import PatientSyncRecord

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSyncRecord
        fields = ['id', 'patient_reference', 'clinic_name', 'sync_status', 'last_updated', 'notes',]
