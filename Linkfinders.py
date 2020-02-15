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
        passer = []
        reciver = []
        for line in passingevents:
            if not "Opponent" in line:
                line = line.split(",")
                passer.append(line[3])
                reciver.append(line[4])
                
        
        passerNode = []
#        for item in passer:
#            passerNode.append(item.number_of_edges)
        edge = []
        for i in range(len(passer)):
            edge.append([passer[i],reciver[i]])
        node_no_dup = [] 
        for i in passer: 
            if i not in passer: 
                node_no_dup.append(i)
        G = nx.Graph() # Initialize a Graph object                                                        
        G.add_nodes_from(node_no_dup) # Add nodes to the Graph                             
        G.add_edges_from(edge) # Add edges to the Graph  
        print(nx.info(G)) # Print information about the Graph 
        
        mapping = {0: 'a', 1: 'b', 2: 'c'}
        H = nx.relabel_nodes(G, mapping)
        plt.figure(figsize=(10, 10))
        
        #nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
        nx.draw(G)
        for i in range(20):
            print(passer[i])
        plt.title('Soccer Players', size=15)
        plt.show()
        pass
    def calcAvgPostion(file):
        """
        Given a file returns a dict with (player,average postion)
        """
        avgPlayerPosition  = {}
        totalX = 0
        totalY = 0
        DividingFactor = 0 
        for line in file:
            line = line.split(",")
            #Origin
            if "Huskies" in line[2]:
                #point1 = Point(int(line[7]),int(line[8])
                
                point1 = Point.Point(5,6)

                if not line[2] in avgPlayerPosition:
                    avgPlayerPosition[line[2]] = []
                avgPlayerPosition[line[2]].append(point1)
            #Destination
            if "Huskies" in line[3]:
                point1 = Point(line[9],line[10])
                if not line[3] in avgPlayerPosition:
                    avgPlayerPosition[line[3]] = []
                avgPlayerPosition[line[3]].append(point1)
        for k, v in avgPlayerPosition.items():
        
            DividingFactor = len(v)
            for Point in v:
                totalX += Point.returnX()
                totalY += Point.returnY()
            avgPlayerPosition[k] = (totalX/DividingFactor, totalY/DividingFactor)
        return avgPlayerPosition
    def calcNodeSize():
        pass
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
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def returnX(self):
        return self.x
    def returnY(self):
        return self.y
    
    
if __name__ == "__main__":
     #analyzeData.mainM()
     print(analyzeData.calcAvgPostion(passingevents))
#     point1 = Point(5,6)
#     print(point1.returnX())
    
    
    

