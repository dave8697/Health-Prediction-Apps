from django.shortcuts import render


# Create your views here.

def index(request):
    request.session.flush()
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def dashboard(request):
    x = request.session.get('logged', None)
    if x == 1:
        return render(request, 'dashboard.html', {})
    else:
        request.session['logged'] = 0
        return render(request, 'dashboard.html', {})

def logout(request):
    request.session.flush()
    return render(request, 'index.html')