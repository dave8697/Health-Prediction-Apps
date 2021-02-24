from django.shortcuts import render

# Create your views here.

def liverApp(request):
    return render(request, 'liver-app.html', {})