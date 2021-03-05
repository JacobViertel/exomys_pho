import csv
import pandas
import matplotlib.pyplot as plt


colum_names =[]
zugkraft_ar = []
drehmoment_ar = []
time_ar = []
datapoint_ar = []
drehwinkel_ar = []

with open('data/Thursday_long.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for i in row:
                colum_names.append(i)
                line_count +=1

print(colum_names)

with open('data/Thursday_long.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        zugkraft_ar.append(float(row[colum_names[2]]))
        drehmoment_ar.append(float(row[colum_names[3]]))
        drehwinkel_ar.append(float(row[colum_names[4]]))
        time_ar.append(i)

increment = 0
for i in zugkraft_ar:
    datapoint_ar.append(increment)
    increment = increment +1

plt.plot(datapoint_ar, zugkraft_ar, label = "Zugkraft")
plt.plot(datapoint_ar, drehmoment_ar, label = "Drehmoment")
plt.plot(datapoint_ar, drehwinkel_ar, label = "Drehwinkel")

plt.title('Kraftverlauf Teststand')
plt.xlabel('Datenpunkt')
plt.ylabel('Zugkraft/Drehmoment')

plt.legend()
plt.show()




