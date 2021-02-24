from django.shortcuts import render

# Create your views here.

def bmi(request):
    return render(request, 'bmi.html', {})