# Custom Graph Library Implementation 🏗️📊

## 📖 Overview
This project represents the development of a lightweight, object-oriented graph library in Python, inspired by the architecture of `NetworkX`. The primary objective was to move beyond simply using a library and instead understand the underlying design patterns, interface-implementation separation, and internal data structures used in graph processing.

## 🏗️ Architectural Design
The project is built on clean software engineering principles:
* **Interface-Driven Development:** Using an Abstract Base Class (`BaseGraph`) to define a strict contract for all graph types. This ensures that any graph representation (e.g., Adjacency List, Adjacency Matrix) is interchangeable.
* **Separation of Concerns:** Clearly separated the public API (interface) from the internal data storage (e.g., dictionaries in `AdjacencyListGraph`), allowing for optimized implementations without breaking the client-side code.
* **Invariant Integrity:** Internal logic ensures graph consistency, such as maintaining symmetry in undirected graphs and enforcing constraints (loops/multigraph behavior).

## 📂 Repository Components
* `base_graph.py`: Defines the `BaseGraph` abstract interface. This serves as the "contract" for all future graph implementations, ensuring consistent method signatures.
* `adjacency_graph.py`: A concrete implementation of the interface using an adjacency list. It provides efficient neighbor lookups and edge management.
* `grader_helpers.py`: A custom-built testing/grading utility used to verify the correctness of the graph operations and edge cases during development.
* `Wprowadzenie.txt`: Documentation detailing the project requirements, design philosophy, and expected architectural goals.

## 🚀 Key Technical Highlights
* **Pythonic API:** Implemented magic methods (`__contains__`, `__iter__`, `__len__`) to allow natural syntax usage (e.g., `if node in graph:`, `for v in graph:`).
* **Exception Handling:** Robust management of edge cases (e.g., adding edges between non-existent nodes, removing non-existent edges).
* **Extensibility:** The design allows for seamless integration of new graph representations (like Adjacency Matrices or sparse matrices) simply by extending `BaseGraph`.

## 🛠️ Project Structure & Origin
The codebase is based on a provided academic framework (starter code) containing the base interface and helper utilities. My contribution focuses on the implementation of graph representation classes (`AdjacencyListGraph`, `AdjacencyMatrixGraph`) and core traversal algorithms (`BFS`, `DFS`).

* **Provided Framework:** `base_graph.py`, `grader_helpers.py`
* **My Implementation:** `adjacency_graph.py`, `adjacency_listdi_graph.py`, `adjacency_matrix_graph.py`, `adjacency_matrixdi_graph.py`, `bfs.py`, `dfs.py`