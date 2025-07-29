print("number of nodes:",len(graph.nodes))
print("numnber of edges:", len(graph.edges))

for node_id, data in list(graph.nodes(data = True))[:5]:
  print(f"node {node_id} : {data}")

for u ,v , data in list(graph.edges(data = True))[:5]:
  print(f"edge from {u} to {v} : distance =  {data['length']}")