from rest_framework import serializers
from .models import PatientSyncRecord

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSyncRecord
        fields = ('id', 'title', 'body',)
