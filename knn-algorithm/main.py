from array import *
from math import *
import pandas as pan
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
    return sqrt(result)

url = "https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv"
data = pan.read_csv(url, header=None)
x = data.iloc[1:,0:4].values
y = data.iloc[:,4:5].values
result = [100]
result[12]=1
print(type(result[12]))
print(result)


      



   