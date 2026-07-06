# Production Scheduling & DAG Optimization 🏭🗓️

## 📖 Overview
This project solves a classic operations research and business optimization problem: **manufacturing task scheduling**. The objective is to allocate a series of interdependent tasks to limited resources (machines) in a way that minimizes the **makespan** (the total time required to complete all tasks).

The problem is modeled using a **Directed Acyclic Graph (DAG)**, where nodes represent tasks (with durations and resource requirements) and directed edges represent strict execution dependencies. 

## 🚀 Key Features & Algorithm Steps

### 1. Graph Modeling
* Parsed complex input data (JSON) containing task definitions, execution times, required machinery (M1, M2, M3), and prerequisites.
* Constructed a Directed Acyclic Graph using `NetworkX` to accurately map the production pipeline.

### 2. Topological Sorting
* Applied topological sorting to guarantee that no task is evaluated before all of its prerequisite tasks have been successfully sequenced.

### 3. Custom Scheduling Engine
* Developed a dynamic scheduling algorithm that determines the earliest possible start time for each task based on two strict constraints:
  * **Dependency Constraint:** A task can only start after its latest-finishing predecessor is completed.
  * **Resource Constraint:** A task can only start when all required machines are free and available.
* Successfully calculated the optimal execution timeline, achieving a final optimized **Makespan of 30 units**.

### 4. Automated Gantt Chart Generation
* Implemented a programmatic generator that translates the calculated schedule and machine availability logs into `Mermaid.js` syntax, allowing for dynamic and highly readable Gantt chart visualizations.

## 🛠️ Tech Stack
* **Language:** Python 3 (Google Colab)
* **Graph Processing:** `NetworkX`
* **Data Handling:** `json`, `pandas`
* **Visualization:** `matplotlib` (graph structure), `Mermaid.js` (Gantt charts)