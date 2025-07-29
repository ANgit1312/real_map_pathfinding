import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

place_name = "Seoul"

graph = ox.graph_from_place(place_name, network_type = "drive")

ox.plot_graph(graph)


print("number of nodes:",len(graph.nodes))
print("numnber of edges:", len(graph.edges))

for node_id, data in list(graph.nodes(data = True))[:5]:
  print(f"node {node_id} : {data}")

for u ,v , data in list(graph.edges(data = True))[:5]:
  print(f"edge from {u} to {v} : distance =  {data['length']}")

from road_graph import RoadGraph
road_graph = RoadGraph(graph)
print(f"number of nodes: {len(road_graph.nodes)}")
print(f"number of edges: {len(road_graph.edges)}")