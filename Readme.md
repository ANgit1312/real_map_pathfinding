# Real Map Pathfinding Visualiser

### 🚀 *Project Overview*
This project visualises *shortest paths on real city maps* using:
- *BFS* for unweighted shortest path
- *Dijkstra* for weighted shortest path
- *A\** for heuristic-based efficient pathfinding

It uses *OpenStreetMap data* to create realistic road networks and visualises computed paths interactively on maps.

---

### 🎯 *Objective*
✅ Fetch real city road data  
✅ Convert to a graph (nodes as intersections, edges as roads with distances)  
✅ Implement pathfinding algorithms to compute routes  
✅ Visualise the routes clearly for practical demonstration

---

### 🛠 *Technologies Used*
- *Python*
- *OSMnx:* Fetching and parsing OpenStreetMap data  
- *NetworkX:* Graph operations  
- *Folium:* Map visualisation  
- *Heapq:* For priority queues in Dijkstra and A\*

---

### 📚 *Algorithms Implemented*

| Algorithm | Description | Use Case |
|---|---|---|
| *BFS* | Finds shortest path in terms of *number of steps/hops*. Ignores edge weights. | Social networks (minimum connections). |
| *Dijkstra* | Finds shortest *physical distance* considering all edge weights equally. | Delivery routing, navigation apps. |
| *A\** | Uses a *heuristic (straight-line distance)* to guide search efficiently towards the goal. | Large-scale maps where speed is crucial. |

---

### 📝 *Implementation Highlights*
✅ Extracted *real map data* for Connaught Place, Delhi using OSMnx  
✅ Created a custom RoadGraph class to store nodes (lat, lon) and weighted edges  
✅ Implemented BFS, Dijkstra, and A* from scratch  
✅ Used *Haversine formula* for heuristic distance in A*  
✅ Visualised computed paths using Folium with:
- *Blue path line*
- *Green marker* for source
- *Red marker* for destination

---

### 💻 *How to Run*

1. *Clone the repository*
    bash
    git clone https://github.com/yourusername/real_map_pathfinding
    cd real_map_pathfinding
    

2. *Setup virtual environment*
    bash
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    

3. *Install requirements*
    bash
    pip install -r requirements.txt
    

4. *Run any test script*
    - For A* with visualisation:
        bash
        python day5_visualise.py
        

5. *Open output*
    - Open pathfinding_result.html in your browser to view the computed path.

---

### 🌐 *Screenshots*

![Map Screenshot](./screenshots/pathfinding_result.png)

(Add your generated screenshot here)

---

### 📈 *Complexities*

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| BFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) using heap | O(V) |
| A\* | O((V + E) log V), often faster than Dijkstra in practice | O(V) |

---

### 🎤 *Interview Explanation*
> “I built a pathfinding visualiser using real map data from OpenStreetMap. I implemented BFS, Dijkstra, and A* to demonstrate practical applications of graph algorithms. The visualisation with Folium clearly shows shortest paths, and the project highlights my understanding of data structures, priority queues, heuristics, and practical integration for real-world use cases like delivery routing or navigation systems.”

---

### ✅ *Future Enhancements*
- Support multiple destinations (TSP heuristic)  
- Integrate traffic data as dynamic edge weights  
- Deploy as a web app using *FastAPI + React + Leaflet.js*

---

### 🙌 *Credits*
- [OpenStreetMap](https://www.openstreetmap.org/) for map data  
- [OSMnx](https://github.com/gboeing/osmnx) for Python map processing tools

---

### 📌 *Author*
*Your Name* – [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

---