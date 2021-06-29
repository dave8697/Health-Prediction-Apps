from django.shortcuts import render
import pickle
import numpy as np
from werkzeug import exceptions
from sklearn.linear_model import LogisticRegression
from keras.models import load_model

# Create your views here.

def breastCancer(request):
    return render(request, 'breast-cancer.html', {})

def breast_result(request):
    df = {}
    if request.method == 'POST':
        inputs = request.POST
        for key in inputs:
            if key == 'csrfmiddlewaretoken' or key == 'name' or key == 'age':
                pass
            else:
                df[key] = inputs[key]
        float_features = [[float(x) for x in df.values()]]
        final = [np.array(float_features)]
        model = load_model("ML/BreastCancer/breast_cancer.h5")
        prediction = model.predict(final)
        output = '{0:.{1}f}'.format((prediction[0][0]*100), 2)
        parameter = {}
        if(prediction[0][0] >= 0.5):
            parameter['Condition'] = "Malignant"
        else:
            parameter['Condition'] = "Benign"
        parameter['Probability'] = output
        return render(request, 'breast_result.html', parameter)