from django.shortcuts import redirect, render
from .models import userlist

# Create your views here.
def database():
    return ()

def login_check(request):
    if request.method == "POST":
        uid = request.POST.get('email')
        passwd = request.POST.get('pass')
        context = {}
        ulist = userlist.objects.filter(email = uid, password = passwd).values()
        if (len(ulist)==0):
            return redirect('http://127.0.0.1:8000/login')
        else:
            for key in ulist:
                request.session['name'] = key['name'].split(" ")[0]
            return redirect('http://127.0.0.1:8000/dashboard')

def newUser(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        ugender = request.POST.get('gender')
        udob = request.POST.get('dob')
        ucontact = request.POST.get('contact')
        ucountry = request.POST.get('Country')
        uemail = request.POST.get('email')
        npass = request.POST.get('npass')
        ulist = userlist.objects.create(name = uname, gender = ugender, dob = udob, contact = ucontact, country = ucountry, email = uemail, password = npass)
        ulist.save()
        request.session['name'] = ulist.name.split(" ")[0]
        print(request.session['name'])
    return redirect('http://127.0.0.1:8000/dashboard')