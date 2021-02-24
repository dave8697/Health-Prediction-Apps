from django.urls import path
from . import views

app_name = 'heartApp'
urlpatterns = [
    path('health/', views.heartApp, name = 'heartApp')
]
