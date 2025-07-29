import osmnx as ox
from road_graph import RoadGraph
from bfs import bfs

# Load map data
place_name = "Seoul"
ox_graph = ox.graph_from_place(place_name, network_type='drive')
road_graph = RoadGraph(ox_graph) #Converts the OpenStreetMap graph into a road graph.

# Choose two nodes for testing
nodes = list(road_graph.nodes.keys()) #Gets all the nodes in the graph.
source = nodes[0] #Chooses the first node as the source.
destination = nodes[10] #Chooses the 11th node as the destination.

print(f"Source: {source}, Destination: {destination}") #Prints the IDs of the chosen source and destination nodes.

# Run BFS
path = bfs(road_graph, source, destination) #Calls the bfs function to find a path from the source to the destination using Breadth-First Search.
print("Path found by BFS:")
print(path)
print("Number of steps:", len(path))

print("path coordinates (lat,lon):")
for node in path:
    print(road_graph.nodes[node]) 