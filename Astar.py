import heapq
import math

def haversine(coord1, coord2):
    # Calculate the great-circle distance between two points on the Earth
    R = 6371e3  # Earth radius in meters
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1]) 
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    
    dlat = lat2 - lat1 
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)*2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)*2 #haversine formula
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) #great-circle distance
    
    return R * c #returns the distance in meters

def astar(graph, start, goal): #A* algorithm
    visited = set() #nodes that have been visited
    g_score = {node: float('inf') for node in graph.nodes} #distance from the start node to the current node
    f_score = {node: float('inf') for node in graph.nodes} #total cost of the path from the start node to the current node
    parent = {node: None for node in graph.nodes} #parent of each node
    
    g_score[start] = 0 #distance from the start node to the start node
    f_score[start] = haversine(graph.nodes[start], graph.nodes[goal]) #total cost of the path from the start node to the goal node
    
    heap = [(f_score[start], start)] #priority queue
    
    while heap:
        current_f, current_node = heapq.heappop(heap) #removes the node with the smallest f_score from the heap
        
        if current_node == goal: #if the current node is the goal, break the loop
            break
        
        if current_node in visited: #if the current node has been visited, skip it
            continue
        
        visited.add(current_node) #marks the current node as visited
        
        for neighbor, weight in graph.edges.get(current_node, []): #iterates over the neighbors of the current node
            tentative_g = g_score[current_node] + weight #distance from the start node to the neighbor node
            if tentative_g < g_score[neighbor]: #if the tentative g_score is less than the current g_score, update the g_score and f_score
                g_score[neighbor] = tentative_g #updates the g_score of the neighbor node
                f_score[neighbor] = tentative_g + haversine(graph.nodes[neighbor], graph.nodes[goal]) #updates the f_score of the neighbor node
                parent[neighbor] = current_node #updates the parent of the neighbor node
                heapq.heappush(heap, (f_score[neighbor], neighbor)) #adds the neighbor node to the heap
    
    # Reconstruct path
    path = [] #path to the goal
    if g_score[goal] != float('inf'): #if the goal has been visited, reconstruct the path
        node = goal #starts from the goal
        while node is not None: #while the node is not the start node
            path.append(node) #adds the node to the path
            node = parent[node] #sets the node to the parent of the current node
        path.reverse() #reverses the path to get the correct order
    
    return path, g_score[goal] #returns the path and the distance to the goal