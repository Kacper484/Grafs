# Academic Curriculum Optimizer 🎓📅

## 📖 Overview
This project focuses on automated scheduling and constraint satisfaction. The objective is to design an optimal, 7-semester study plan for an Applied Computer Science degree program. 

The courses are treated as nodes in a **Directed Acyclic Graph (DAG)**, where edges represent prerequisites. The algorithm must successfully navigate these dependencies while strictly adhering to ECTS (European Credit Transfer and Accumulation System) workload constraints per semester.

## 🚀 Problem Statement & Constraints
The algorithm ingests a dataset of university courses (`przedmioty-inf.json`), containing course codes, ECTS points, categories (mandatory/elective), and prerequisite lists. It must generate a valid semester-by-semester schedule satisfying the following rules:

1. **Dependency Resolution:** A course can only be taken if all its prerequisite courses have been completed in prior semesters.
2. **Workload Balancing:** Each semester must contain between **25 and 32 ECTS** points.
3. **Degree Requirement:** The final schedule must sum up to exactly **210 ECTS** points across all 7 semesters.
4. **Early Completion:** Courses must be scheduled as early as possible without violating the above constraints.

## 🧠 Algorithmic Approach
* **Graph Construction:** Represented the curriculum as a dependency graph.
* **Topological Sorting & Heuristics:** Evaluated nodes based on their in-degree (prerequisites) and out-degree (how many future courses depend on them) to prioritize critical path subjects (e.g., Math I -> Math II).
* **Constraint Satisfaction:** Implemented dynamic capacity checking to ensure the ECTS load remains within the valid bounds for each bucket (semester), rolling over courses to subsequent semesters when capacity is reached.

## 🛠️ Tech Stack
* **Language:** Python 3 (Google Colab / Jupyter Notebook)
* **Data Format:** JSON
* **Concepts:** Graph Theory, DAGs, Topological Sort, Constraint Satisfaction Programming (CSP).

## 📂 Files in this directory
* `Planowanie kierunku studiów_Kacper_Kaszuba.ipynb` - The main notebook containing the logic, data processing, and scheduling algorithm.
* `przedmioty-inf.json` - The input dataset containing the curriculum structure and constraints.
* `images` - Shows the png images of set graphs in project