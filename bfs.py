from collections import deque

def bfs(graph, start, goal):
    visited = set() # nodes that have been visited
    queue = deque() # nodes to be visited (order in which nodes are added to the queue)
    parent = {} # parent of each node (used to reconstruct the path)

    queue.append(start) #adds the start node to the queue
    visited.add(start) #marks the start node as visited
    parent[start] = None #sets the parent of the start node to None

    while queue: # loops as long as there are nodes to be explored
        current = queue.popleft() # removes the first node from the queue , assign it to current

        if current == goal: # if the current node is the goal, break the loop
            break

        for neighbor, _ in graph.edges.get(current, []): # iterates over the neighbors of the current node
            if neighbor not in visited: # if the neighbor has not been visited, add it to the queue
                visited.add(neighbor) # marks the neighbor as visited
                parent[neighbor] = current # sets the parent of the neighbor to the current node
                queue.append(neighbor) # adds the neighbor to the queue(future nodes to be explored)

    # Reconstruct path
    path = [] # path to the goal
    if goal in visited: # if the goal has been visited, reconstruct the path
        node = goal
        while node is not None: # while the node is not the start node
            path.append(node) # adds the node to the path
            node = parent[node] # sets the node to the parent of the current node
        path.reverse() # reverses the path to get the correct order
    
    return path # returns the path as a list of nodes, empty if no path is found