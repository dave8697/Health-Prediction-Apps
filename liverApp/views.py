from django.shortcuts import render
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create your views here.

def liverApp(request):
    return render(request, 'liver-app.html', {})

def liverApp_result(request):
    context = {}
    df = {}
    input_data = []
    gender_array = [0, 0]
    if request.method == "POST":
        data = request.POST
        for key in data:
            if key == 'csrfmiddlewaretoken' or key == 'name' or key == 'gender':
                pass
            else:
                df[key] = data[key]
        
        gender = request.POST.get('gender')
        
        if gender == '0':
            gender_array[1] = 1
        else:
            gender_array[0] = 1

        gender_array = np.array(gender_array)
        input_data = list(df.values())
        input_data = np.array(input_data)
        input_data = input_data.astype(float)
        gender_array = gender_array.astype(float)
        #print(input_data)
        #print(gender_array)
        final = np.concatenate([input_data, gender_array])
        #print(final)
        final = final.reshape(1, len(final))
        #input_data = StandardScaler().fit_transform(input_data)
        #print(input_data)
        model = pickle.load(open('ML/Liver_disease/liver.sav', 'rb'))
        out = model.predict_proba(final)
        #print(out)
        
        if out[0][0] > out[0][1]:
            context['acc'] = round(out[0][0]*100, 2)
            context['out'] = "Normal"
        else:
            context['acc'] = round(out[0][1]*100, 2)
            context['out'] = "Infected"
    return render(request, 'liver_result.html', context)