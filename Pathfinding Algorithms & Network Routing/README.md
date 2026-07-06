# Pathfinding Algorithms & Network Routing 🗺️🕸️

## 📖 Overview
This project focuses on the implementation and modification of fundamental pathfinding algorithms in graphs. The primary goal of these exercises was to build a deep understanding of graph traversal and optimization by writing custom implementations of classic algorithms from scratch, bypassing the high-level pathfinding functions typically provided by libraries.

The code explores finding optimal routes under various constraints, handling negative weights, and identifying specific topological features of networks.

## 🚀 Key Algorithms Implemented

### 1. Custom Dijkstra's Algorithm (`dijkstra_with_path`)
* **Objective:** Find the shortest path between a source and a target node in a weighted graph with non-negative edge weights.
* **Implementation Details:** Written from scratch using custom logic to track distances and predecessors. Unlike standard implementations that only return the minimum cost, this function reconstructs and returns the exact sequence of nodes (the route) required to achieve the minimal cost.

### 2. Constrained Shortest Path (`dijkstra_with_limit`)
* **Objective:** Solve a practical logistics/routing problem: finding the shortest path between two cities with a strict limit on the maximum number of intermediate stops (hops).
* **Implementation Details:** An advanced modification of Dijkstra's algorithm utilizing a priority queue (`heapq`). The state space was expanded to track not only the accumulated distance but also the current node count, dynamically pruning paths that violate the constraint. 

### 3. Bellman-Ford Algorithm (`bellman_ford`)
* **Objective:** Compute shortest paths in directed graphs where edge weights can be negative (e.g., representing profit/loss or energy expenditure/recovery).
* **Implementation Details:** Custom implementation that iteratively relaxes edges and includes a robust mechanism for detecting **negative weight cycles**—a critical feature for preventing infinite loops in financial or routing models.

### 4. Network Topology Extraction
* **Objective:** A foundational exercise to algorithmically identify all "leaf" nodes (nodes with exactly one neighbor) within an undirected graph, useful for finding dead-ends or endpoints in a network.

## 🛠️ Tech Stack
* **Language:** Python 3 (Google Colab)
* **Data Structures:** `NetworkX` (strictly used for graph representation, not for solving), `heapq` (Priority Queues), `Sets`, `Dictionaries`.