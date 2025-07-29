import osmnx as ox
from road_graph import RoadGraph 
from bfs import bfs
from dijkstra import dijkstra

# Load map data
place_name = "Seoul"
ox_graph = ox.graph_from_place(place_name, network_type='drive') 
road_graph = RoadGraph(ox_graph)

# Choose source and destination
nodes = list(road_graph.nodes.keys()) #Gets all the nodes in the graph.
source = nodes[0]
destination = nodes[10]

print(f"Source: {source}, Destination: {destination}")

# BFS
bfs_path = bfs(road_graph, source, destination) 
print("\nBFS path (unweighted):") #Prints the BFS path. #unweighted means that all edges have the same weight
print(bfs_path)
print("Steps:", len(bfs_path))

# Dijkstra
dijkstra_path, total_distance = dijkstra(road_graph, source, destination)
print("\nDijkstra path (weighted):") #Prints the Dijkstra path. #weighted means that each edge has a different weight
print(dijkstra_path) 
print("Total distance (meters):", total_distance)
print("Steps:", len(dijkstra_path))