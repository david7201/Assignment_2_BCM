from django.urls import path
from .views import ListApi, DetailApi

urlpatterns = [
    path('<int:pk>/', DetailApi.as_view()),
    path('', ListApi.as_view()),
]
