from rest_framework import generics
from .models import PatientSyncRecord
from .serializers import ApiSerializer

class ListApi(generics.ListAPIView):
    queryset = PatientSyncRecord.objects.all()
    serializer_class = ApiSerializer

class DetailApi(generics.RetrieveAPIView):
    queryset = PatientSyncRecord.objects.all()
    serializer_class = ApiSerializer

