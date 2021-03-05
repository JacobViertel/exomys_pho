from pandas import read_csv
from numpy import mean
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
series = read_csv('data/prepared_results.csv', header=0, index_col=0)
# prepare situation
X = series.values
window = 3
history = [X[i] for i in range(window)]
test = [X[i] for i in range(window, len(X))]
predictions = list()
# walk forward over time steps in test
for t in range(len(test)):
 length = len(history)
 yhat = mean([history[i] for i in range(length-window,length)])
 obs = test[t]
 predictions.append(yhat)
 history.append(obs)
 print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test, color='blue', label='test')
pyplot.plot(predictions, color='red', label='prediction')
pyplot.legend()
pyplot.show()
# zoom plot
pyplot.plot(test[0:100], color='blue', label='test')
pyplot.plot(predictions[0:100], color='red', label='prediction')
pyplot.legend()
pyplot.show()