# Statistical Analysis of Graphs: Zachary's Karate Club 🥋🕸️

## 📖 Overview
This project presents a comprehensive statistical and topological analysis of the famous **Zachary's Karate Club** social network. The study explores the dynamics of a real-world social group that eventually fractured into two separate factions due to an internal conflict. 

This project was developed as part of an academic laboratory exercise. It applies advanced graph theory concepts and statistical network analysis methodologies to investigate network resilience, node roles, and community detection algorithms.

*Note: The original assignment and dataset introduction can be found in the `nx_lab_02_karate_klub.ipynb` notebook.*

## 🚀 Key Tasks & Analysis

### Task 1: Node Roles in a Network
Identification of key actors within the club using multiple centrality measures:
* **Measures calculated:** Degree Centrality, Betweenness Centrality, Closeness Centrality, PageRank, and Eigenvector Centrality.
* **Role Classification:** Nodes were classified into specific social roles: *Leaders* (red), *Brokers* (green), *Local Organizers* (blue), and *Peripheral nodes* (yellow).

### Task 2: Network Resilience to Failures
Simulating targeted attacks on the network to test its structural integrity:
* **Methodology:** Sequentially removing top nodes based on two different strategies: **Highest Degree** vs. **Highest Betweenness Centrality**.
* **Metrics tracked:** Number of connected components, largest connected component size, average path length, clustering coefficient, and network diameter.
* **Conclusion:** Removing the most popular nodes yields the same catastrophic fragmentation as removing the main brokers, effectively "beheading" the social structure.

### Task 3: Community Detection & Real-world Split
Applying various clustering algorithms to predict the historical fracture of the club:
* **Algorithms tested:** Girvan-Newman, Louvain Method, Label Propagation, and Asynchronous Fluid Communities.
* **Evaluation:** Results were evaluated using **Modularity** and visualized via **Confusion Matrices**.
* **Conclusion:** The algorithm with the highest mathematical modularity (Louvain: 0.43) incorrectly predicted 4 groups. The **Girvan-Newman** algorithm proved to be the most accurate in reflecting the real-world bipolar split.

### Task 4: Is the Karate Club an "Atypical" Graph?
Statistical hypothesis testing against random graph models:
* **Methodology:** Generating 500 **Erdős–Rényi random graphs** with the same number of nodes and probability of edge creation (p ≈ 0.14).
* **Results:** The Karate Club's Average Clustering Coefficient (0.57) is extraordinarily high compared to random graphs (~0.14), proving the network possesses a highly non-trivial, distinct social structure.

## 🛠️ Tech Stack
* **Language:** Python 3 (Jupyter / Google Colab)
* **Graph Processing:** `NetworkX`
* **Data Analysis:** `pandas`, `NumPy`
* **Visualization:** `matplotlib`, `seaborn`

## 📚 Literature & References
This analysis is grounded in established statistical network analysis methodologies:
1. **Sengupta, S. (2023).** *Statistical Network Analysis: Past, Present, and Future*. [arXiv:2311.00122](https://arxiv.org/abs/2311.00122) - Used as a theoretical reference for the evolution and application of statistical models in complex networks.
2. **Zachary, W. W. (1977).** *An Information Flow Model for Conflict and Fission in Small Groups*. Journal of Anthropological Research, 33(4), 452–473.