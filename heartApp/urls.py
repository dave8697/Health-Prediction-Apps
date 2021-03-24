from django.urls import path
from . import views

app_name = 'heartApp'
urlpatterns = [
    path('health/', views.heartApp, name = 'heartApp'),
    path('health/result', views.result_view, name = 'result'),
    path('health/', views.result_view, name = 'result'),
]
