import random, copy

def choose_random_key(G):
    #choose uniformly one of the keys
    v1 = random.choice(list(G.keys()))
    #choose uniformly one of the vertices connected to that key (an edge)
    v2 = random.choice(list(G[v1]))
    #return that edge
    return v1, v2

def karger(G):
    length = []
    #while there are more than 2 vertices
    while len(G) > 2:
        #get a random edge
        v1, v2 = choose_random_key(G)
        #idea here is merge the two nodes, v1 remains but v2 will vanish
        G[v1].extend(G[v2])  #make the nodes v2 knows, connected to v1
        #for each node v2 as connected to        
        for x in G[v2]:
            G[x].remove(v2) #make that node forget v2
            G[x].append(v1) #now it knows v1
        #remove self loops
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]    #finally deletes v2 from graph
    #get the number of edges getting out of one of the vertices
    for key in G.keys():
        length.append(len(G[key]))
    #since there are only two, they have the same number of edges    
    return length[0]

def operation(n):
    """
    This method perform the karger contraction algorithm n times
    to a graph and returns the smallest number found. Run it
    enough times and you're statistically confident to find the min cut
    """
    #keeps track of number of times algorithm ran
    i = 0 
    #count has to start as big as the number of edges in the graph
    count = 10000   
    while i < n:
        #make a copy of tge graph
        data = copy.deepcopy(G)
        #pass the copied graph to the algorithm
        min_cut = karger(data)
        #check if that is the min cut so far
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count


data = open("kargerMinCut.txt","r")
G = {}
for line in data:
    # read the line in the file and store it in a list
    lst = [int(s) for s in line.split()]
    #first element, lst[0] is the key and rest of list is the data that
    #key points to, which is a list type
    G[lst[0]] = lst[1:]   

print operation(100)