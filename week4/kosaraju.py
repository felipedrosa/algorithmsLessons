# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 01:17:06 2016

@author: felipedrosa
"""
import sys

#open the file passed as argument to the call
f = open("SCC.txt")

def first_pass(graph):
    ordering = []
    ordering_set = set()
    explored = set()
    
    print "Started first pass..."  
  
    for vertex in range(max(graph.keys()), 0, -1):
        if vertex not in explored:
            stack = [vertex]
            while stack:
                u = stack.pop()
                if u not in explored:
                    explored.add(u)
                    stack.append(u)  #append it back for backtracking purpose
                    if u in graph:
                        for v in graph[u]:
                            if v not in explored:
                                stack.append(v)
                else:
                    if u not in ordering_set:
                        ordering.append(u)
                        ordering_set.add(u)
    return ordering

def second_pass(graph, ordering):
    explored = set()
    leader = {}
    
    print "Started second pass..." 
    
    for u in reversed(ordering):
        if u not in explored:
            explored.add(u)
            stack = [u]
            leader[u] = []
            while stack:
                vertex = stack.pop()
                if vertex in graph:
                    for v in graph[vertex]:
                        if v not in explored:
                            explored.add(v)
                            stack.append(v)
                    leader[u].append(vertex)
                else:
                    leader[u] = [u]
    return leader

#input file contains the arcs, but in string format
arcs = []
for line in f:
    # get a list of nodes as string
    line = line.split()
    if line:
        # convert them to int
        line = [int(i) for i in line]
        arcs.append(line)  #contains a list of edges [u,v]
        
#convert list of edges into graph adjacency list format
G = {}
G_rev = {}
for arc in arcs:
    # if the first node of arc isn't a key in G, add it
    if arc[0] not in G:
        G[arc[0]] = [arc[1]] #create entry in dict
    else:
        G[arc[0]].append(arc[1]) #append to existing entry
    if arc[1] not in G_rev:
        G_rev[arc[1]] = [arc[0]]
    else:
        G_rev[arc[1]].append(arc[0])
print "Finished reading G and G_rev"

SCC = second_pass(G, first_pass(G_rev))
#print SCC
size_scc = [len(SCC[i]) for i in SCC]
solution = sorted(size_scc, reverse=True)
print solution[0:5]
