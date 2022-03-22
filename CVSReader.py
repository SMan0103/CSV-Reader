import csv
import matplotlib.pyplot as plt
import numpy as np

file = open("data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
x = []
y = []

def sortFunc(e):
    return e[0]

for row in csvreader:
    rows.append(row)

rows.sort(key=sortFunc)

# for at printe hvad der står i en matrix. 
for row in rows:
    cols = row[0].split(";")
    x.append(float(cols[0]))
    y.append(float(cols[1]))

# Her for at plotte det dataen.  

#plt.scatter(x, y)
plt.plot(x, y, 'o')
m, b = np.polyfit(x, y, 1)
m = int(m)
plt.plot(x, m*x+b)

plt.show()

file.close()

