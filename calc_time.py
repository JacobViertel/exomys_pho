import os
import csv
import pandas
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

entries = os.listdir('data/')

colum_names =[]
zugkraft_ar = []
drehmoment_ar = []
time_ar = []
data_point_ar = []
datapoint_ar = []
drehwinkel_ar = []

with open('data/'+entries[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for i in row:
                colum_names.append(i)
                line_count +=1

print(colum_names)

with open('data/'+entries[0], newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        zugkraft_ar.append(float(row[colum_names[2]]))
        drehmoment_ar.append(float(row[colum_names[3]]))
        drehwinkel_ar.append(float(row[colum_names[4]]))
        time_ar.append(row[colum_names[5]])


#loop through time_ar and calculate difference
duration_ar = []
i = 0
for x in time_ar:
    if i < len(time_ar)-1:
        date_time_obj1 = datetime.strptime(time_ar[i], '%H:%M:%S')
        date_time_obj2 = datetime.strptime(time_ar[i+1], '%H:%M:%S')
        date_time_obj3 = date_time_obj2 - date_time_obj1
        duration_ar.append(int(date_time_obj3.seconds))
        i +=1

work_sum_ar = []
i = 0
sum=0
for x in duration_ar:
    sum += duration_ar[i]*zugkraft_ar[i]
    work_sum_ar.append(sum)
    datapoint_ar.append(i)
    i +=1


plt.plot(datapoint_ar, work_sum_ar)

plt.title('Arbeitsverlauf')
plt.xlabel('Datenpunkt')
plt.ylabel('Arbei in W')

plt.show()
