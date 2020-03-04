# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:06:56 2020

@author: PhillipM
"""
import matplotlib.pyplot as plt
import math
import random
import numpy as np
import statistics
import scipy
import networkx as nx
import pandas as pd
from collections import Counter
import operator
import seaborn as sb
triangleDict= {'D1': 339, 'M1': 339, 'M2': 167, 'G1': 298, 'D2': 330, 'D3': 326, 'D4': 308, 'M3': 330, 'F2': 314, 'F3': 163, 'F1': 330, 'D5': 321, 'M4': 312, 'M5': 133, 'D6': 301, 'M6': 317, 'M7': 45, 'M8': 217, 'M9': 273, 'F4': 305, 'D7': 284, 'M10': 134, 'M11': 199, 'M12': 237, 'M13': 169, 'F5': 268, 'F6': 262, 'D8': 204, 'D9': 90, 'D10': 44, }
degreeDict = [('D1', 32), ('M1', 32), ('M2', 21), ('G1', 30), ('D2', 31), ('D3', 31), ('D4', 30), ('M3', 29), ('F2', 30), ('F3', 19), ('F1', 31), ('D5', 30), ('M4', 30), ('M5', 19), ('D6', 29), ('M6', 30), ('M7', 10), ('M8', 24), ('M9', 25), ('F4', 29), ('D7', 28), ('M10', 17), ('M11', 21), ('M12', 25), ('M13', 21), ('F5', 27), ('F6', 25), ('D8', 23), ('D9', 14), ('D10', 10)]
triangleValues = []
for k ,v in triangleDict.items():
    triangleValues.append(v)
for value in triangleValues:
    value = float(value)
degreeValues = []
for tup in degreeDict:
    degreeValues.append(float(tup[1]))
print(triangleValues)
#print("DegreeValues", (degreeValues))
plt.title("Triangles vs Degrees")
plt.scatter(x = triangleValues, y = degreeValues)

