from django.urls import path
from . import views

app_name = 'diabetesApp'
urlpatterns = [
    path('health/', views.diabetesApp, name = 'diabetesApp'),
    path('health/diabetes_result', views.diabetes_result, name = 'diabetes_result'),
]