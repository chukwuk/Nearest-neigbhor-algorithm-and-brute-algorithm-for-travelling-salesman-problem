import os
import time
import random
import numpy as np
import sys
#import math 
from cmath import sqrt
from itertools import permutations

## This is a class for the brute-force algorithm
class Graph_perm():

    def __init__(self, x_co,y_co,z):
        self.x = x_co
        self.y = y_co
        self.z = z
        self.vertex_ind = []
        self.total_distance = 0
        self.min_dist = 1000000000000
        self.min_vert = []

    def perm (self):
        p = permutations(self.z)
        return p

    # This calculates the distance between two vertices
    def distance_cal(self, indx,indy):
        y2 = (self.y[indx] - self.y[indy])**2
        x2 = (self.x[indx] - self.x[indy])**2
        zz = x2 + y2
        zz = (zz)**(1/2)
        zz = round(zz)
        return zz
    # This returns the optimized total distance
    def return_dist(self):
       return self.min_dist

    # This returns the vertices in order of the tour
    def return_edges(self):
       return self.min_vert
     # Function to find the minimum distance and tour
    def min_d_edges(self):
        t = self.perm()

        for i in list(t):
            dist = 0
            tu = list(i)
            for j in range(len(tu)-1):
                d = self.distance_cal(int(tu[j]),int(tu[j+1]))
                #d  = self.distance_cal(0,1)
                #print(d)
                dist+=d

            if  self.min_dist > dist:
                self.min_dist = dist
                self.min_vert = tu

        tt = self.return_dist()
        return tt
 
     


## This is a class for the nearest neigbhor algorithm
class Graph(): 
  
    def __init__(self, x_co,y_co): 
        self.x = x_co 
        self.y = y_co
        self.vertex_ind = [] 
        self.total_distance = 0 
    # A utility function to return the parent
    def printMST(self, parent):  
        return parent
  
 
    # This returns the vertices in order of the tour
    def return_vert(self):
        return self.vertex_ind    

    # This returns the optimized total distance 
    def return_dist(self):
        return self.total_distance

    # This calculates the distance between two vertices
    def distance_cal(self, indx,indy): 
        y2 = (self.y[indx] - self.y[indy])**2
        x2 = (self.x[indx] - self.x[indy])**2
        zz = x2 + y2
        zz = (zz)**(1/2)
        zz = round(zz)
       

        return zz 
     # Function to find the minimum distance and tour
    
    def primMST(self): 
  
        # Key values used to pick minimum weight edge in cut 
        key = [10000000000] * len(self.x) 
        parent = [None] * len(self.x) # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        #key[0] = 0 
        mstSet = [False] * len(self.x) 
  
        parent[0] = -1 # First node is always the root of
        #vertex_ind = [] 
        #u = random.randint(0,(self.V-1))
        u = 0        
        self.vertex_ind.append(u)
        for cout in range(len(self.x)): 
  
            # Pick the minimum distance vertex from  the vertex to its adjacent vertices
           
  
            # Set the vertex visited to true 
            mstSet[u] = True
  
            
            min_dist = sys.maxsize
            min_index = 0 
            for v in range(len(self.x)): 
          
                if self.distance_cal(u,v) > 0 and mstSet[v] == False and  min_dist > self.distance_cal(u,v):
                        min_dist = self.distance_cal(u,v)
                        min_index = v                        
       
            parent[min_index] = u 
            u = min_index
            if not u in self.vertex_ind:
               self.vertex_ind.append(u)
               self.total_distance+=min_dist
            
        r = self.printMST(parent) 
        return r










applic = input('\nname of the textfile: ') # This reads in the graph.txt file
f = open(applic, 'r')   #opens the graph.txt file


list_data = []
lengh = 0
x_c = []
y_c = []
num = []
# reads in the file into an array
for (i,line) in enumerate(f):
    list_data.append(line.strip()) 
    lengh = i 

lengh = i+1   
count = 0
#gets the number of veertices in the file
vertices = len(list_data)
#append the co-ordinates of the edges to an array
for i in range(vertices):
    z,x,y= list_data[i].split()
    x_c.append(int(x))
    y_c.append(int(y))
    num.append(int(z))

# This uses brute force if the number of vertices are  less than or equal to 10
if int(vertices) > 10:

# passes the array of vertices into the object
   g = Graph(x_c,y_c)  
   starttime = time.clock()
   # finds the minimum route
   parent = g.primMST()
   finishtime = time.clock()
   time_length =  finishtime-starttime
   print("The time length for the algorithm is:",time_length)
   total_distance = 0   
   total_distance = g.return_dist()
   vert = g.return_vert()
else:
   gr = Graph_perm(x_c,y_c,num)
   starttime = time.clock()
   # finds the minimum route
   total_distance = gr.min_d_edges()
   vert = gr.return_edges()
   finishtime = time.clock()
   time_length =  finishtime-starttime
   print("The time length for the algorithm is:",time_length)

# Print the TSP solution to the file
writefile = str(applic) + '.tour'
uu = open(writefile, 'w')
uu.write("%s\n" %str(total_distance))
for lin in vert:
   uu.write("%s\n" %str(lin))

uu.close




