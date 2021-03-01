from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import lag_plot, autocorrelation_plot
from pandas import DataFrame, concat
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

series = read_csv('data/daily-min-temperatures.csv', header=0, index_col=0)
values = DataFrame(series.values)

#print data head  -----------------------------------------!
print(series.head())

#plot the data on a graph  -----------------------------------------!
#series.plot()

#quick check of lag behavior -----------------------------------------!
#lag_plot(series)

#quick check of correlation -----------------------------------------!
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t-1', 't+1']
result = dataframe.corr()
print(result)

#quick check of correlation -----------------------------------------!
#autocorrelation_plot(series)
#pyplot.show()
#plot_acf(series, lags=31)
#pyplot.show()


# split into train and test sets
X = dataframe.values
train, test = X[1:len(X)-7], X[len(X)-7:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

# persistence model
def model_persistence(x):
	return x

# walk-forward validation
predictions = list()
for x in test_X:
	yhat = model_persistence(x)
	predictions.append(yhat)
test_score = mean_squared_error(test_y, predictions)
print('Test MSE: %.3f' % test_score)
# plot predictions vs expected
pyplot.plot(test_y, color='blue', label='test data')
pyplot.plot(predictions, color='red', label='predictions')
pyplot.title('Without AutoReg')
pyplot.legend()
pyplot.show()