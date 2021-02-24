from django.shortcuts import render

# Create your views here.

def breastCancer(request):
    return render(request, 'breast-cancer.html', {})