from os import terminal_size
import numpy as np
import pandas as pd

df = pd.read_csv('Training.csv')
df.head()
l1=[]
disease = []
for i in df.keys():
    if i!='prognosis':
        l1.append(i)
print(l1)
for i in df['prognosis'].unique():
    disease.append(i)
print(disease)
l2=[]
for x in range(0,len(l1)):
    l2.append(0)
print(l2)
for i, idx in enumerate(df['prognosis'].unique()):
    print(i)
    print(idx)
for i in disease:
    df['prognosis']=df['prognosis'].replace({i:disease.index(i)})
df['prognosis']

X= df[l1]
y = df[["prognosis"]]
np.ravel(y)

tr = pd.read_csv("Testing.csv")
for i in disease:
    tr['prognosis']=tr['prognosis'].replace({i:disease.index(i)})
tr['prognosis']
X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)


from sklearn.ensemble import RandomForestClassifier
clf4 = RandomForestClassifier()
clf4 = clf4.fit(X,np.ravel(y))
from sklearn.metrics import accuracy_score
y_pred=clf4.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(accuracy_score(y_test, y_pred,normalize=False))
import pickle as pk
pk.dump(clf4, open('disease_predict.pkl', 'wb'))