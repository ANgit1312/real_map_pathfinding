class RoadGraph:
    def __init__(self, ox_graph):
        self.nodes = {}  # node_id: (lat, lon)
        self.edges = {}  # node_id: list of (neighbor_id, distance)

        for node_id, data in ox_graph.nodes(data=True):
            self.nodes[node_id] = (data['y'], data['x'])  # lat, lon

        for u, v, data in ox_graph.edges(data=True):
            if u not in self.edges:
                self.edges[u] = []
            self.edges[u].append((v, data['length']))

            # Undirected graph (add reverse)
            if v not in self.edges:
                self.edges[v] = []
            self.edges[v].append((u, data['length']))