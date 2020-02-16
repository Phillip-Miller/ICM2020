# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:13:46 2020

@author: PhillipM
Shots are orange
Goals are red
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
            line = line.split(",")
            #Assuming you cant have a apposing reciver?
            if "Huskies" in line[2] and "Huskies" in line[3]:
                passer.append(line[2])
                reciver.append(line[3])
    
        edge1 = []
        edge_no_dup = []
        edge_width = []
        #@FIXME CALL SHOTS HERE
        shooter = analyzeData.calcShots()
        for i in range(len(passer)):
            edge1.append(passer[i]+ " " + reciver[i])
#        for i in range(20):
#            print (shooter[i])
        for edge in shooter:
            edge1.append(edge[0]+ " " + edge[1])

        for edge in edge1:
            if edge not in edge_no_dup:
                edge_no_dup.append(edge)
        z = Counter(edge1)
        maxEdge = 0
        for k,v in z.items():
            if v > maxEdge:
                maxEdge = v
            
        edge_width_dict ={}
        edge_no_dup_split = []
        for edge in edge_no_dup:
            value = z[edge]/maxEdge*6
            edge_width.append(value)
            edge_width_dict[edge] = value
            x = edge.split(" ")
            edge_no_dup_split.append((x[0],x[1]))
        edge_no_dup = edge_no_dup_split

        
        node_no_dup = [] 
        for i in passer: 
            if i not in node_no_dup: 
                node_no_dup.append(i)
        labels = {}
        for node in node_no_dup:
            labels[node] = (node[7:])
        labels["Goal"] = "Goal"
        node_no_dup.append("Goal")
        G = nx.Graph() # Initialize a Graph object                                                        
        G.add_nodes_from(node_no_dup) # Add nodes to the Graph                             
        G.add_edges_from(edge_no_dup) # Add edges to the Graph  
        #print(nx.info(G)) # Print information about the Graph 
        
        
        
        
        plt.figure(figsize=(10, 10))
        
        #nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
        posdict = analyzeData.calcAvgPostion()
        #assigning colors
        colormap = []
        for name in node_no_dup:
            if "_G" in name:
                colormap.append("Yellow")
            if  "_D" in name:
                colormap.append("Green")
            if  "_M" in name:
                colormap.append("Blue")
            if "_F" in name:
                colormap.append("Orange")
            if "Goal" in name:
                colormap.append("Red")
        
        
        nx.draw_networkx(G, pos = posdict,node_color=colormap,width = edge_width, labels = labels,
                         font_color = "White")
        
        plt.title('Soccer Players', size=15)
        plt.show()
       # print(nx.pagerank_numpy(G))
        pass
    def calcShots(team = "Huskies"):
        """
        Returns an edgelist of the shots"
        """
        fullevents = open(r"2020_Problem_D_DATA\fullevents.csv", "r")
        edgelist = []
        for line in fullevents:
            tokens = line.split(",")
            if "Shot" in tokens[6] and team in tokens[2]:
                edgelist.append((tokens[2],"Goal"))
        return edgelist
                

    def calcAvgPostion():
        """
        Given a file returns a dict with (player,average postion)
        Sums up all the originID and the Destination ID
        """
        file = open(r"2020_Problem_D_DATA\passingevents.csv", "r")
        avgPlayerPosition  = {}
        DividingFactor = 0 
        for line in file:
            line = line.split(",")
            #Origin
            if "Huskies" in line[2]:
                point = Point(float(line[7]),float(line[8]))
#Checking if the entry exists in the dict yet
                if not line[2] in avgPlayerPosition:
                    avgPlayerPosition[line[2]] = []
                avgPlayerPosition[line[2]].append(point)
            #Destination
            if "Huskies" in line[3]:
                point = Point(float(line[9]),float(line[10]))
                if not line[3] in avgPlayerPosition:
                    avgPlayerPosition[line[3]] = []
                avgPlayerPosition[line[3]].append(point)
                
        for k, v in avgPlayerPosition.items():
            totalX = 0
            totalY = 0
            DividingFactor = len(v)
            for point in v:
                totalX += point.returnX()
                totalY += point.returnY()
                #Scaling factor longer field then wide
            avgPlayerPosition[k] = ((totalX/DividingFactor)*1.3, totalY/DividingFactor*.9)

        avgPlayerPosition["Goal"] = (100,50)
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
        pass
    
class Point:
    """
    Point class to hold XY coordinates
    """
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def returnX(self):
        return self.x
    def returnY(self):
        return self.y
class Player(Point):
    def __init__(self,x,y,name,degree = 0):
        self.x = float(x)
        self.y = float(y)
        self.name = name
        self.degree = degree
    def returnDegree(self):
        return self.degree
    def returnName(self):
        return self.name
if __name__ == "__main__":
     analyzeData.mainM()
     #print(analyzeData.calcAvgPostion())
     #print(analyzeData.calcAvgPostion(passingevents))
     
    
    

