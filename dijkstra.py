import heapq

def dijkstra(graph, start, goal):
    visited = set() # nodes that have been visited
    distance = {node: float('inf') for node in graph.nodes} # distance to each node
    parent = {node: None for node in graph.nodes} # parent of each node
    
    distance[start] = 0
    heap = [(0, start)]  # (distance, node) - priority queue
    
    while heap:
        current_dist, current_node = heapq.heappop(heap) # removes the node with the smallest distance from the heap
        
        if current_node in visited: # if the node has been visited, skip it
            continue
        
        visited.add(current_node) # marks the node as visited
        
        if current_node == goal: # if the node is the goal, break the loop
            break
        
        for neighbor, weight in graph.edges.get(current_node, []): # iterates over the neighbors of the current node
            if neighbor not in visited: # if the neighbor has not been visited, update the distance and parent
                new_dist = current_dist + weight # calculates the new distance to the neighbor
                if new_dist < distance[neighbor]: # if the new distance is less than the current distance, update the distance and parent
                    distance[neighbor] = new_dist # updates the distance to the neighbor
                    parent[neighbor] = current_node # updates the parent of the neighbor
                    heapq.heappush(heap, (new_dist, neighbor)) # adds the neighbor to the heap
    
    # Reconstruct path
    path = [] # path to the goal
    if distance[goal] != float('inf'): # if the goal has been visited, reconstruct the path
        node = goal # starts from the goal
        while node is not None: # while the node is not the start node
            path.append(node) # adds the node to the path
            node = parent[node] # sets the node to the parent of the current node
        path.reverse() # reverses the path to get the correct order
    
    return path, distance[goal] # returns the path and the distance to the goal