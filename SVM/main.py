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
from datetime import datetime, timedelta

style.use('ggplot')

df = read_csv('/../data/random_data.csv', header=0, index_col=0)

df = df[['zugkraft', 'drehwinkel']]
tot_work = []
sum_work = 0
for x in df['zugkraft']:
    sum_work += x*0.5
    tot_work.append(sum_work)

df['arbeit'] = (tot_work)
df['arbeit'].plot(label='Eingetreten')

forecast_col = 'arbeit'
df.fillna(-9999, inplace=True)
forecast_out = int(math.ceil(0.17*len(df)))

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

clf_SVM = svm.SVR(kernel='linear')
clf_SVM.fit(X_train, y_train)
accuracy_SVM= clf_SVM.score(X_test,y_test)
print('accuracy_SVM ' + str(accuracy_SVM))

forecast_set = clf_SVM.predict(X_lately)
#print(forecast_set , accuracy_LinReg, forecast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name

last_date_time = datetime.strptime(last_date, '%H:%M:%S')
next_unix = last_date_time + timedelta(seconds=30)

for i in forecast_set:
    next_date = next_unix
    next_unix += timedelta(seconds=30)
    df.loc[next_date.time()] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['arbeit'].plot()
df['Forecast'].plot(label='Vorhergesagt', color='green')
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Arbeitslast')
plt.show()