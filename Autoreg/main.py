# create and evaluate an updated autoregressive model
from pandas import read_csv
from matplotlib import pyplot
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

# load dataset
df = read_csv('../data/random_data.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

df = df[['zugkraft', 'drehwinkel']]
tot_work = []
sum_work = 0
for x in df['zugkraft']:
    sum_work += x*0.5
    tot_work.append(sum_work)

df['arbeit'] = (tot_work)
df.drop(['zugkraft', 'drehwinkel'], inplace=True, axis=1)

# split dataset
X = df.values
train, test = X[1:len(X)-20], X[len(X)-20:]
# split dataset
X = df.values
train, test = X[1:len(X)-20], X[len(X)-20:]
# train autoregression
window = 40
model = AutoReg(train, lags=40)
model_fit = model.fit()
coef = model_fit.params
# walk forward over time steps in test
history = train[len(train)-window:]
history = [history[i] for i in range(len(history))]
predictions = list()
for t in range(len(test)):
	length = len(history)
	lag = [history[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	obs = test[t]
	predictions.append(yhat)
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot
pyplot.plot(test, color='green', label='Test')
pyplot.plot(predictions, color='red', label='Vorhersage')
plt.xlabel('Zeit')
plt.ylabel('Arbeitslast')
plt.legend()
pyplot.show()