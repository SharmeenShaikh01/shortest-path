import sys
graph={'A':{'B':10,'C':43,'D':17,'E':7},'B':{'C':23}, 'E':{'D':2}, 'D':{'C':8}}  ##the given graph
graph={
    'A':{'B':4,'C':5,'D':8},  #graph that I assummed
    'B':{'C':2,'F':6},
    'C':{'F':7,'D':3},
    'D':{'E':4,'G':7},
    'E':{'G':4,'H':5},
    'F':{'E':2,'H':9},
    'G':{'H':3},
    'H':{'G':3}
}
def dij_algo(graph,start,goal):
    infinity=sys.maxsize    #the max number(infinity) which is assigned to the nodes except the start node
    shortest_distance={}    #set used to store shortest distance
    trace_path=[]           #list which will be used to trace the path of the shortest distance found
    track_pred={}           #Set used to store the predecessor of the current node
    unvisited_nodes=graph   #assumed that every vertex in the graph is unvisited here
    
    for node in unvisited_nodes:
        shortest_distance[node]=infinity    #assign infinity to all unvisited nodes
    shortest_distance[start]=0              #except the start node and set start node=0
    
    while unvisited_nodes:              
        minimum_dist = None             #initially no minimum distance 
        for nodes in unvisited_nodes:
            if minimum_dist is None: #if so
                minimum_dist=nodes  #swap them
            elif shortest_distance[nodes]< shortest_distance[minimum_dist]: #move the pointer if shortest distance is less
                minimum_dist=nodes  #swap them
        path_options=graph[minimum_dist].items() #possible paths that we will take from cost/minimum distance
        for child_node, weight in path_options:
            if weight+shortest_distance[minimum_dist]<shortest_distance[child_node]:    #if cost/minimum distance is > weight + shortest distance
                shortest_distance[child_node]=weight+shortest_distance[minimum_dist]    #assign cost+ summation of weight+ shortest distance    
                track_pred[child_node]=minimum_dist # trace the path which has led to minimum distance node
        unvisited_nodes.pop(minimum_dist) #pop all the nodes which have been traced
    currentNode=goal #assign goal to currentNode
    while currentNode!=start: #when current node is not start node
        try:                #for graphs which are not fully interconnected 
            trace_path.insert(0,currentNode) #insert current node
            currentNode=track_pred[currentNode] #track predecessor of current node
        except KeyError:
            print("Path unreachable")
            break
    trace_path.insert(0,start)
    if shortest_distance[goal]!=infinity: #check if all the nodes are covered or not
        print("shortest distance is" + str(shortest_distance[goal])) # print shortest path cost
        print("optimal path is " + str(trace_path))  #print the shortest path
#graph={'A':{'B':10,'C':43,'D':17,'E':7},'B':{'C':23}, 'D':{'C':8},'E':{'D':2}}
dij_algo(graph,'A','C')  
