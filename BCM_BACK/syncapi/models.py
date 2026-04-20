from django.db import models

# Create your models here.

class PatientSyncRecord(models.Model):
    patient_reference = models.CharField(max_length=20)
    clinic_name = models.CharField(max_length=100)
    sync_status = models.CharField(max_length=20)
    last_updated = models.DateTimeField()
    notes = models.TextField()
    
    def __str__(self):
        return self.patient_reference