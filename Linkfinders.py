# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:13:46 2020

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
fullevents = open(r"2020_Problem_D_DATA\fullevents.csv", "r")
matches = open(r"2020_Problem_D_DATA\matches.csv", "r")
passingevents = open(r"2020_Problem_D_DATA\passingevents.csv", "r")
coachWinLoss = {"Coach1":0,"Coach2":0,"Coach3":0}
"""
Plot heatmap of where players spend time

Do a whole bunch of plots, and stick code and graph in google docs
"""
class Player:
    def __init__(self,):
        """
        Games, Passes, Goals, etc
        """
        pass
class triangle(Player):
    pass

class analyzeData:
    def mainM():
        data = pd.read_csv(r"2020_Problem_D_DATA\passingevents.csv")
        print(data.head())
        
        df = nx.from_pandas_edgelist(data, source='OriginPlayerID', target='DestinationPlayerID', edge_attr=True)
        plt.figure(figsize=(50,50))
        nx.draw_networkx(df, with_labels=True)
    def plotCoaches():
        global coachWinLoss
        for line in matches:
            tokens = line.strip().split(",")
            if tokens[2] == "win":
                coachWinLoss[tokens[6]] += 1
        print (coachWinLoss)
        plt.bar(range(len(coachWinLoss)), list(coachWinLoss.values()), align='center')
        plt.xticks(range(len(coachWinLoss)), list(coachWinLoss.keys()))
        plt.show()
            
if __name__ == "__main__":
     analyzeData.mainM()
    
    
    

