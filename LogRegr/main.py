from pandas import read_csv
import pandas as pd
import math, datetime 
import numpy as np
import sklearn
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style 

style.use('ggplot')


df = read_csv('random_data.csv', header=0, index_col=0)

df = df[['zugkraft', 'drehwinkel']]
tot_work = []
sum_work = 0
for x in df['zugkraft']:
    sum_work += x*0.5
    tot_work.append(sum_work)

df['arbeit'] = (tot_work)

forecast_col = 'arbeit'
df.fillna(-9999, inplace=True)
forecast_out = int(math.ceil(0.3*len(df)))
#the forecast entities
print('forecast_out in minutes ' + str(forecast_out/2))

df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

clf_LinReg = LinearRegression()
clf_LinReg.fit(X_train, y_train)
accuracy_LinReg = clf_LinReg.score(X_test,y_test)
print('accuracy_LinReg ' + str(accuracy_LinReg))

clf_SVM = svm.SVR(kernel='linear')
clf_SVM.fit(X_train, y_train)
accuracy_SVM= clf_SVM.score(X_test,y_test)
print('accuracy_SVM ' + str(accuracy_SVM))

forecast_set = clf_LinReg.predict(X_lately)
#print(forecast_set , accuracy_LinReg, forecast_out)
df['Forecast'] = np.nan
print(df.head())
print(df.tail())

last_date = 1
# = datetime.datetime.strptime(element,"%H:%M:%S") 
one_entitie = 30
next_unix = last_date + one_entitie

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_entitie
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.head())
print(df.tail())

df['arbeit'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()