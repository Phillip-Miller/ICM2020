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
import seaborn as sb

fullevents = open(r"2020_Problem_D_DATA\fullevents.csv", "r")
matches = open(r"2020_Problem_D_DATA\matches.csv", "r")
passingevents = open(r"2020_Problem_D_DATA\passingevents.csv", "r")
coachWinLoss = {"Coach1":0,"Coach2":0,"Coach3":0}
"""
Plot heatmap of where players spend time

Do a whole bunch of plots, and stick code and graph in google docs
"""


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
        
        plt.figure(figsize=(10*1.7, 10))
        
        #nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
        posdict = analyzeData.calcAvgPostion()
        #assigning colors
        colormap = []
        for name in node_no_dup:
            if "_G" in name:
                colormap.append("Gray")
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

    
    def findTriangles():
        passingevent = open(r"2020_Problem_D_DATA\passingevents.csv", "r")
        passinglist= []
        passingevent.readline()
        passingtriangle = []
        passingtrianglecenter = []
        for line in passingevent:
            line = line.split(",")
            Player1 = Player(line[7],line[8],line[2])
            Player2 = Player(line[9],line[10],line[3])
            if ("Huskies" in line[2] and "Huskies" in line[3]):
               passinglist.append(Player1)
               passinglist.append(Player2)
        for i in range(len(passinglist)):
            try:
                if passinglist[i].returnName() == passinglist[i+2].returnName():
                    passingtriangle.append([passinglist[i],passinglist[i+1],passinglist[i+2]])
            except Exception:
                pass
        writeFile = open("Triangles.csv","w")

        for triangle in passingtriangle:
            
            meanX = statistics.mean([triangle[0].returnX(),triangle[1].returnX(),triangle[2].returnX()])
            meanY = statistics.mean([triangle[0].returnY(),triangle[1].returnY(),triangle[2].returnY()])
#            meanPoint = Point(meanX,meanY)
#            passingtrianglecenter.append(meanPoint)
            stringPoint = str(round(meanX,2)) + "," + str(round(meanY,2))
            writeFile.write(stringPoint + "\n")
        writeFile.close()
        
    def triangleHeatMap():
        xcords = []
        ycords = []
        
        inTriangle = open("Triangles.csv","r")
        for line in inTriangle:
            line = line.split(",")
            #Scaling to get 120 by 70 field
            xcords.append(float(line[0])*1.3)
            #Making 0,0 top left
            ycords.append(80 - float(line[1])*.8)
        fig2 = plt.figure()
        plt.hist2d(xcords, ycords, bins=25)
        plt.xlabel('X Position (defense on left)')
        plt.ylabel('Y Position (facing foward from defense)')
        cbar = plt.colorbar()
        cbar.ax.set_ylabel('Triangle Occurences') 
#        plt.hexbin(xcords, ycords, gridsize=20, cmap='Blues')
#        cb = plt.colorbar(label='# Triangle Occurences')

            
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(18.5, 10.5)
#        fig.savefig('test2png.png', dpi=200)
    def trackInOut():
        letterList = ["A","B","C","D","E","F"]
        F = nx.Graph()
        F.add_nodes_from(["A","B","C","D","E","F"])
        positions = {"A":(27,56),"B":(38,12.5),"C":(38.5,31),"D":(44.6,81.25),"E":(30,18.75),"F":(63.85,87.5)}
        inf = open(r"2020_Problem_D_DATA\passingevents.csv", "r")
        Tedgelist = []
        for line in passingevents:
            line = line.split(",")
            if "Huskies" in line[2] and "Huskies" in line[3]:
                oPt = Point(line[7],line[8])
                rPt = Point(line[9],line[10])
                Tedgelist.append([oPt,rPt])
        validTedgelist = []
        validTriangleList = [[26.923076923076923, 56.25], [38.46153846153846, 12.5], [38.46153846153846, 31.25], [44.61538461538461, 81.25], [26.923076923076923, 18.75], [63.84615384615385, 87.5]]
        validTriangleXlist = [26.923076923076923,38.46153846153846,38.46153846153846,44.61538461538461,26.923076923076923,63.84615384615385]
        validTriangleYlist = [56.25,12.5,31.25,81.25,18.75,87.5]
        for Points in Tedgelist:
            #TEdgelist like [pointobj0,[pointobj1]]
            p1closeX = False
            p2closeX = False
            p1closeY= False
            p2closeY = False
            letter_of_passer = ""
            letter_of_reciver= ""
            for i in range(6):
                if not p1closeX and not p1closeY:
                    if abs(Points[0].returnX()-validTriangleXlist[i]) < 5:
                        p1closeX = True
                    if abs(Points[0].returnY()-validTriangleYlist[i]) < 5:
                        p1closeY = True
                    if p1closeX and p1closeY:
                        letter_of_passer = letterList[i]
                        continue
                if not p2closeX and not p2closeY:
                    if abs(Points[1].returnX()-validTriangleXlist[i]) < 5:
                        p2closeX = True
                    if abs(Points[1].returnY()-validTriangleYlist[i]) < 5:
                        p2closeY = True
                    if p2closeX and p2closeY:
                        letter_of_reciver = letterList[i]
                        continue
            if  p1closeX and p2closeX and p1closeY and p2closeY:
                #Youve found a pass between triangles
                validTedgelist.append([letter_of_passer,letter_of_reciver])
        print("Length", len(validTedgelist))
        #Valid edge list now has a list of passes between the triangles
        F.add_edges_from(validTedgelist)
        #Make the x and y axis 100 instead of whatever it is now
        nx.draw_networkx(F, pos = positions)
        print(validTedgelist)
        
                        
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
    def __init__(self,x,y,name):
        self.x = float(x)
        self.y = float(y)
        self.name = name
    def returnName(self):
        return self.name
if __name__ == "__main__":
     #analyzeData.mainM()
     #analyzeData.findTriangles()
     #analyzeData.triangleHeatMap()
     analyzeData.trackInOut()
     
    
    

