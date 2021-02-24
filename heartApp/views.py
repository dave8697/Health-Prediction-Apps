from django.shortcuts import render


# Create your views here.

def heartApp(request):
    return render(request, 'heart-app.html', {})