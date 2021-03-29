from django.shortcuts import render
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create your views here.

def heartApp(request):
    return render(request, 'heart-app.html', {})

def result_view(request):
    context = {}
    quantitative = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    qualitative = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
    order1 = []
    list1 = []
    order2 = []
    sex = [0]*2
    cp = [0]*4
    fbs = [0]*2
    restecg = [0]*3
    exang = [0]*2
    slope = [0]*3
    ca = [0]*5
    thal = [0]*4
    #dummy{'sex_0': 0, 'sex_1': 0, 'cp_0': 0, 'cp_1':0, 'cp_2': 0, 'cp_3': 0, 'fbs_0': 0, 'fbs_1': 0, 'restecg_0': 0, 'restecg_1': 0, 'restecg_2': 0, 'exang_0': 0, 'exang_1': 0, 'slope_0': 0, 'slope_1': 0, 'slope_2': 0, 'ca_0': 0, 'ca_1': 0, 'ca_2': 0, 'ca_3': 0, 'ca_4': 0, 'thal_0': 0, 'thal_1': 0, 'thal_2': 0, 'thal_3': 0}
    if request.method == "POST":
        for i in quantitative:
            order1.append(request.POST.get(i))
        for i in qualitative:
            order2.append(request.POST.get(i))
        name = request.POST.get('name')
        #print(order1)
        #print(order2)
        #print(name)

        #order1 = list(map(float, order1))
        #order2 = list(map(int, order2))

        if order2[0]=='1':
            sex[1]='1'
        else:
            sex[0]='1'

        
        if order2[1]=='1':
            cp[1]='1'
        elif order2[1]=='2':
            cp[2]='1'
        elif order2[1]=='3':
            cp[3]='1'
        else:
            cp[0]='1'

        
        if order2[2]=='1':
            fbs[1]='1'
        else:
            fbs[0]='1'

        
        if order2[3]=='1':
            restecg[1]='1'
        elif order2[3]=='2':
            restecg[2]='1'
        else:
            restecg[0]='1'
        

        if order2[4]=='1':
            exang[1]='1'
        else:
            exang[0]='1'
        

        if order2[5]=='1':
            slope[1]='1'
        elif order2[5]=='2':
            slope[2]='1'
        else:
            slope[0]='1'


        if order2[6]=='1':
            ca[1]='1'
        elif order2[6]=='2':
            ca[2]='1'
        elif order2[6]=='3':
            ca[3]='1'
        elif order2[6]=='4':
            ca[4]='1'
        else:
            ca[0]='1'


        if order2[7]=='1':
            thal[1]='1'
        elif order2[7]=='2':
            thal[2]='1'
        elif order2[7]=='3':
            thal[3]='1'
        else:
            thal[0]='1'

        sex = np.asarray(sex)
        sex = sex.reshape(len(sex), 1)


        cp = np.asarray(cp)
        cp = cp. reshape(len(cp), 1)


        fbs = np.asarray(fbs)
        fbs = fbs.reshape(len(fbs), 1)


        restecg = np.asarray(restecg)
        restecg = restecg.reshape(len(restecg), 1)


        exang = np.asarray(exang)
        exang = exang.reshape(len(exang), 1)


        slope = np.asarray(slope)
        slope = slope.reshape(len(slope), 1)


        ca = np.asarray(ca)
        ca = ca.reshape(len(ca), 1)


        thal = np.asarray(thal)
        thal = thal.reshape(len(thal), 1)
        
        order1 = np.array(order1)
        order1 = order1.reshape(len(order1), 1)
        order1 = StandardScaler().fit_transform(order1)
        #print(order1)
        dummy = np.concatenate([sex, cp, fbs, restecg, exang, slope, ca, thal])
        dummy = np.array(dummy.astype(float))
        #print(dummy)
        final_data = np.concatenate([order1, dummy])
        final_data = final_data.transpose()
        #print(final_data.shape)

        model = load_model('ML/Heart_disease/heart-predict.h5')
        result = model.predict(final_data)
        print(result[0][0])
        context['result'] = round(result[0][0]*100, 2)
    return render(request, 'result.html', context)