import pandas as pan
import numpy as np
import matplotlib.pyplot as mplt

url = "https://raw.githubusercontent.com/ameenmanna8824/DATASETS/main/IRIS.csv"
data = pan.read_csv(url, header=None)
x = data.iloc[:,0:4].values
y = data.iloc[:,4:5].values
print(x)
print(y)

   