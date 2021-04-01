from django.urls import path
from . import views

app_name = 'liverApp'
urlpatterns = [
    path('health/', views.liverApp, name = 'liverApp'),
    path('health/liver_result', views.liverApp_result, name = 'liver_result'),
]
