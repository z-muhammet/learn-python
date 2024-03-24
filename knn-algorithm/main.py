from array import *
from math import *
import pandas as pan
from collections import Counter
import numpy as np
import matplotlib.pyplot as mplt
def oklid (x:float,y:float):
    return (float(x)-float(y))**2

def oklid1 (x:list,y:list):
    result = 0
    i = 0
    while i < len(x):
        result+=(oklid(float(x[i]),float(y[i])))
        i += 1
    return float(sqrt(result))

url = "https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv"
data = pan.read_csv(url, header=None)
x = data.iloc[1:,0:4].values
y = data.iloc[:,4:5].values
k=[[0,1,2,3],[4,5,6,7]]
i=0
result = np.arange(0.0,150.0,1.0)
find = [4.9,2.5,5,1]
while i<len(x):
    result[i] = oklid1(x[i],find)
    i += 1
j=0
while j<4:
    i=0
    while i<150:
        if result[i] == min(result):
            k[0][j] = i
            k[1][j] = result[i] 
            result[i] = 1000
            break
        i += 1
    j += 1

etiket = ["","","",""]
for i in range(4):
    print("En yakın",i+1,". elemanın indexi:",k[0][i],"ve uzaklığı:",k[1][i],"etiket ise : ",y[k[0][i]])
    etiket[i] = y[k[0][i]]

tekrarlar = {}
i = 0
while i < 4:
    tekrarlar[etiket[i][0]] = etiket.count(etiket[i])
    i += 1 

print("verilen veri setine göre aranan verinin etiketi:",max(tekrarlar,key=tekrarlar.get))

   