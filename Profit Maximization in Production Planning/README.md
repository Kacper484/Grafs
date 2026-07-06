# Profit Maximization in Production Planning 📈🪵

## 📖 Overview
This project tackles a complex operations research problem: optimizing a multi-week production plan for a furniture factory to maximize total profit. The problem is modeled dynamically, accounting for fluctuating raw material and energy costs over time, as well as strict resource limitations (e.g., a limited wood budget).

Instead of traditional linear programming, this solution utilizes an innovative **State-Space Graph** approach and a custom modification of the **Bellman-Ford algorithm**.

## 🚀 Key Features & Methodology

### 1. State-Space Graph Modeling
* **Nodes** represent specific production states at a given week (e.g., current inventory, week number).
* **Edges** represent production decisions (e.g., manufacturing chairs, table legs, or halting production).
* **Edge Weights** are dynamic and represent the net profit of a transition, factoring in the variable costs of energy and raw materials for that specific week.

### 2. Modified Bellman-Ford Algorithm
* The classic Bellman-Ford shortest-path algorithm was heavily customized to find the **Longest Path (Maximum Profit)** in a Directed Acyclic Graph (DAG).
* **Feasibility Check (Relaxation limits):** The relaxation step was modified to dynamically check resource constraints. If a path exceeds the global wood budget, the transition is blocked or penalized, ensuring only mathematically viable production plans are evaluated.

### 3. Scenario Analysis
The model was tested against multiple business scenarios:
* **Unconstrained Production:** Finding the absolute maximum profit when resources are unlimited.
* **Budget-Constrained Production (Scenario C):** Demonstrating how the algorithm intelligently adapts by dropping less profitable intermediate steps (e.g., halting production in week 4) to stay within a strict 6-unit wood budget while still maximizing the overall outcome.

## 🛠️ Tech Stack
* **Language:** Python 3 (Google Colab)
* **Graph Modeling:** `NetworkX`
* **Data Visualization:** (Insert libraries if used for charts, e.g., `matplotlib`, `seaborn`)

## 📊 Visualizations
* All plots and graphs are in folder 'images'