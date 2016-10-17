# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 01:05:32 2016

@author: felipedrosa
"""

import sys
from heapq import heappush, heappop
        
def make_graph(filename):
    """
    Construct a graph from text input file and return it.
    Graph in format G = {vertex_v: list of tuples (vertex_w,weight_vw)}, where
        vertex_v = vertex of G (1 to 200)
        vertex_w = vertex of G connected to vertex_v
        weight_vw = weight of the edge connecting vertex_v and vertex_w
        
    Each line is in format 
      vertex_v list of tuples separated by commas and spaces
    """

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()
    
    G = {  int(line.split()[0]): [  (int(tup.split(",")[0]), 
                                     int(tup.split(",")[1])) 
                                     for tup in line.split()[1:]  ] 
                                        for line in line_list if line  }
    
    f.close()
    return G

def dijkstra(Graph, source):
    queue = []
    D = {}      #dictionary of final distances
    
    queue = [(0,source)]
    while queue:
        cost, vertex = heappop(queue)
        if vertex not in D:
            D[vertex] = cost
            
            for w,c in Graph.get(vertex, ()):
                if w not in D:
                    heappush(queue,(cost+c, w))
    
    return D
    
    
    

G = make_graph("dijkstraData.txt")
dist = dijkstra(G,1)
solution = ""
for v in [7,37,59,82,99,115,133,165,188,197]:
    solution = solution + str(dist[v]) + ","
    
print solution[:-1]
