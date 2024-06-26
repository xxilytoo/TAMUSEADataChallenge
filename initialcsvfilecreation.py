# -*- coding: utf-8 -*-
"""SeaDataChallenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VhS_c82JpUAZauEpXdmCWLQ_sX2ZUCU3
"""

from google.colab import drive
drive.mount('/content/drive')

from google.colab import files
uploaded = files.upload()

from google.colab import drive
import pandas as pd
from scipy.io import loadmat

data = loadmat(r"Budget_TimeSeries.mat")

print(data.keys())

L = data["L"]

newL = pd.DataFrame(L, columns=["lon", "lat"])
newL.to_csv(r"L.csv");

L = data["t"]
newL = pd.DataFrame(L)
newL.to_csv(r"t.csv");

L = data["Mfilc"]
newL = pd.DataFrame(L)
newL.to_csv(r"Mfilc.csv");

L = data["MBSL"]
newL = pd.DataFrame(L)
newL.to_csv(r"MBSL.csv");

L = data["MIBE"]
newL = pd.DataFrame(L)
newL.to_csv(r"MIBE.csv");

L = data["MGRD"]
newL = pd.DataFrame(L)
newL.to_csv(r"MGRD.csv");

L = data["MRes"]
newL = pd.DataFrame(L)
newL.to_csv(r"MRes.csv");

from matplotlib import pyplot as plt
y = (pd.read_csv('Mfilc.csv'))['0']
x = (pd.read_csv('t.csv'))['0']

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
