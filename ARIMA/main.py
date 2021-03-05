# Importing required libraries 
import numpy as np 
import pandas as pd 
import matplotlib as plt 
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose 
  
# Read the AirPassengers dataset 
df = pd.read_csv('../data/random_data.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

df = df[['zugkraft', 'drehwinkel']]
tot_work = []
sum_work = 0
for x in df['zugkraft']:
    sum_work += x*0.5
    tot_work.append(sum_work)

df['arbeit'] = (tot_work)
df.drop(['zugkraft', 'drehwinkel'], inplace=True, axis=1)
  
# Print the first five rows of the dataset 
print(df.head())

# Split data into train / test sets 
train = df.iloc[:len(df)-12] 
test = df.iloc[len(df)-12:] # set one year(12 months) for testing 
  
# Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) on the training set 
from statsmodels.tsa.statespace.sarimax import SARIMAX 
  
model = SARIMAX(train['arbeit'],  
                order = (0, 1, 1),  
                seasonal_order =(2, 1, 1, 12)) 
  
result = model.fit() 
result.summary() 

start = len(train) 
end = len(train) + len(test) - 1
  
# Predictions for one-year against the test set 
predictions = result.predict(start, end, typ = 'levels').rename("Predictions") 
  
# plot predictions and actual values 
predictions.plot(legend = True) 
test['arbeit'].plot(legend = True) 
pyplot.show()



# Load specific evaluation tools 
from sklearn.metrics import mean_squared_error 
from statsmodels.tools.eval_measures import rmse 
  
# Calculate root mean squared error 
rmse(test["arbeit"], predictions) 
  
# Calculate mean squared error 
mean_squared_error(test["arbeit"], predictions) 

# Train the model on the full dataset 
model = model = SARIMAX(df['arbeit'],  
                        order = (0, 1, 1),  
                        seasonal_order =(2, 1, 1, 12)) 
result = model.fit() 
  
# Forecast for the next 3 years 
forecast = result.predict(start = len(df), end = (len(df)-1) + 8 * 12, typ = 'levels').rename('Forecast') 
  
# Plot the forecast values 
df['arbeit'].plot(figsize = (12, 5), legend = True) 
forecast.plot(legend = True) 
pyplot.show()