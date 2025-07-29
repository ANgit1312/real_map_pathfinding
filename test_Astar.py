import osmnx as ox 
from road_graph import RoadGraph
from Astar import astar

# Load map data
place_name = "seoul"      #Specifies the location of the map data.
ox_graph = ox.graph_from_place(place_name, network_type='drive') #Loads the map data from OpenStreetMap.
road_graph = RoadGraph(ox_graph) #Converts the OpenStreetMap graph into a road graph.

# Choose two nodes for testing
nodes = list(road_graph.nodes.keys()) #Gets all the nodes in the graph.
source = nodes[0] #Chooses the first node as the source.
destination = nodes[10] #Chooses the 11th node as the destination.

print(f"Source: {source}, Destination: {destination}") #Prints the IDs of the chosen source and destination nodes.

path, total_distance = astar(road_graph, source, destination) #Calls the Astar function to find a path from the source to the destination using Dijkstra's algorithm.
print("Path found by Astar:")
print(path)
print("Total distance (meters):", total_distance)
print("Steps:", len(path))

print("path coordinates (lat,lon):")
for node in path:
    print(road_graph.nodes[node]) 
