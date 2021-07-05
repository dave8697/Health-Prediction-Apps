from django.urls import path
from . import views

app_name = 'diseasePrediction'
urlpatterns = [
    path('health/', views.diseasePrediction, name = 'diseasePrediction'),
    path('health/disease_result', views.disease_result, name = 'disease_result'),
]