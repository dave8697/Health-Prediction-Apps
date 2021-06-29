from django.urls import path
from . import views

app_name = 'breastCancer'
urlpatterns = [
    path('health/', views.breastCancer, name = 'breastCancer'),
    path('health/breast_result', views.breast_result, name = 'breast_result')
]
