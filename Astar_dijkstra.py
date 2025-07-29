import osmnx as ox
from road_graph import RoadGraph 
from dijkstra import dijkstra
from Astar import astar

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
Astar_path = astar(road_graph, source, destination) 
print("\nAstar path (unweighted):") #Prints the Astar path.
print(Astar_path)
print("Steps:", len(Astar_path))

# Dijkstra
dijkstra_path, total_distance = dijkstra(road_graph, source, destination)
print("\nDijkstra path (weighted):") #Prints the Dijkstra path.
print(dijkstra_path)
print("Total distance (meters):", total_distance)
print("Steps:", len(dijkstra_path))