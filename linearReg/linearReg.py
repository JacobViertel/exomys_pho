import pandas as pd 
from pandas import read_csv
import math

df = read_csv('data/Thursday_long.csv', header=0, index_col=5)

columns = ['koerpergroesse', 'alter','zugkraft', 'drehmoment', 'drehwinkel']
df['NewCol1'] = (df['zugkraft'] + df['drehmoment'])/ df['alter']*100
sum = 0
df['NewCol2'] = (sum + df['zugkraft'] + df['drehwinkel'])/ df['drehmoment']


df = df[['zugkraft', 'drehmoment', 'drehwinkel','NewCol2']]

forecast_col = 'NewCol2'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.05*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())