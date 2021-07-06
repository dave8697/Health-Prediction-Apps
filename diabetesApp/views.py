from django.shortcuts import render
from keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create your views here.
def diabetesApp(request):
    return render(request, 'diabetes.html')

def diabetes_result(request):
    context = {}
    if request.method == 'POST':
        input_data = [request.POST.get('Pregnancies'), request.POST.get('Glucose'), request.POST.get('BloodPressure'), request.POST.get('SkinThickness'), request.POST.get('Insulin'), request.POST.get('BMI'), request.POST.get('age')]
        input_data = np.asarray(input_data)
        input_data = input_data.astype(float)
        input_data = input_data.reshape(1, len(input_data))
        #print(input_data)
        scaler = MinMaxScaler()
        input_data_scaled = scaler.fit_transform(input_data)
        model = load_model('ML/Diabetes_prediction/diabetes.h5')
        result = model.predict(input_data)
        #print(result[0][0])
        context['result'] = round(result[0][0]*100, 2)
    return render(request, 'diabetes_result.html', context)