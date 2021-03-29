from django.shortcuts import render

# Create your views here.

def bmi(request):
    return render(request, 'bmi.html', {})

def mass(request):
    context = {}
    if request.method == "POST":
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        weight = request.POST.get('Weight')
        feet = request.POST.get('Feet')
        inches = request.POST.get('Inches')
        weight=float(weight)
        feet = int(feet)
        inches = int(inches)
        height = (feet*0.3048)+(inches*0.0254)
        bmi = round(weight/(height*height), 2)
        context['bmi'] = bmi
    return render(request, 'bmi_result.html', context)