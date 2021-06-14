from django.urls import path
from . import views

app_name = 'database'
urlpatterns = [
    path('', views.database, name = 'database'),
    path('health/login_check', views.login_check, name = 'login_check'),
    path('login/new_user', views.newUser, name = 'newUser'),
]
