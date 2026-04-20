# 🤖 AI202 — Artificial Intelligence | Semester 4 Lab Assignments

<div align="center">

![SVNIT](https://img.shields.io/badge/SVNIT-Surat-blue?style=for-the-badge)
![Branch](https://img.shields.io/badge/Branch-Artificial%20Intelligence-green?style=for-the-badge)
![Semester](https://img.shields.io/badge/Semester-4-orange?style=for-the-badge)
![Language](https://img.shields.io/badge/Languages-Python%20%7C%20C%2B%2B-purple?style=for-the-badge)

</div>

---

## 👤 About Me

**Name:** Param Rasiklal Kanada
**Enrollment No.:** U24AI047
**Institute:** Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat
**Branch:** Artificial Intelligence (AI)
**Semester:** 4th

---

## 📘 Course Details

| Field | Details |
|---|---|
| **Subject** | Artificial Intelligence |
| **Course Code** | AI202 |
| **Professor** | Dr. Prutwik Mishra |
| **Lab Assistants** | Nita Ma'am, Deergha Ma'am |

---

## 📋 About This Repository

This repository contains all my **lab assignment submissions** for the course **AI202 — Artificial Intelligence**, completed during Semester 4 at SVNIT. Each lab folder contains source code (Python / C++), compiled executables, assignment PDFs, and lab reports (`.docx` / `.pdf`).

The labs cover a wide range of foundational and advanced AI topics — from uninformed and informed search algorithms, local search and metaheuristics, adversarial game playing, constraint satisfaction, to propositional logic and knowledge-based reasoning.

---

## 📁 Table of Contents

| Lab | Topic | Concepts Covered | Language |
|-----|-------|-----------------|----------|
| [LAB-1](#lab-1--bfs--dfs-on-graphs) | BFS & DFS on Graphs | Breadth-First Search, Depth-First Search, Weighted Graph Traversal | C++ |
| [LAB-2](#lab-2--bfs--dfs-on-8-puzzle) | BFS & DFS on 8-Puzzle | State Space Search, 8-Puzzle Problem, BFS vs DFS Comparison | C++ |
| [LAB-3](#lab-3--intelligent-agents) | Intelligent Agents | Simple Reflex Agent (Vacuum Cleaner), Production Rule System (Railway Crossing) | Python |
| [LAB-4](#lab-4--best-first-search) | Best-First Search | Non-Heuristic Best-First Search, Graph Representation, Evacuation Path Planning | Python |
| [LAB-5](#lab-5--dls--ids) | DLS & IDS | Depth-Limited Search, Iterative Deepening Search, River Crossing Problem | Python |
| [LAB-6](#lab-6--gbfs--a-search) | GBFS & A* Search | Greedy Best-First Search, A* Search, Heuristic Functions, Reward Collection | Python |
| [LAB-7](#lab-7--hill-climbing--8-queens) | Hill Climbing — 8 Queens | Steepest Ascent HC, First Choice HC, Random Restart HC, Simulated Annealing | Python |
| [LAB-8](#lab-8--tsp--local-beam--genetic-algorithm) | TSP — Beam Search & GA | Local Beam Search, Genetic Algorithm, Single/Two-Point Crossover, TSP | Python |
| [LAB-9](#lab-9--minimax--alpha-beta-pruning) | Minimax & Alpha-Beta Pruning | Minimax Algorithm, Alpha-Beta Pruning, Tic-Tac-Toe Game Tree | Python |
| [LAB-10](#lab-10--k-means-clustering--and-or-graph) | K-Means & AND-OR Graph | K-Means Clustering (GD & NR), Erratic Vacuum Agent, AND-OR Graph Search | Python |
| [LAB-11](#lab-11--constraint-satisfaction-problems) | Constraint Satisfaction Problems | Graph Coloring (Backtracking), SEND + MORE = MONEY (Cryptarithmetic) | Python |
| [LAB-12](#lab-12--arc-consistency--ac-3) | Arc Consistency — AC-3 | AC-3 Algorithm, Room Scheduling CSP, Sudoku Puzzle Solving | Python |
| [LAB-13](#lab-13--propositional-logic--truth-tables) | Propositional Logic | Infix Expression Evaluation, Truth Table Generation, Logical Operators | Python |
| [LAB-14](#lab-14--knowledge-based-inference) | Knowledge-Based Inference | Forward Chaining, Backward Chaining, Resolution-Based Inference | Python |

---

## 🔬 Lab Details

---

### LAB-1 — BFS & DFS on Graphs

📂 **Files:** `q1.cpp`, `q2.cpp`

**Q1 — City Route Finding (Weighted Graph)**
Implements **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** on a weighted undirected graph of US cities (Chicago → New York). Tracks the path, total travel cost in miles, and prints the BFS spanning tree edges.

**Q2 — Social Network Traversal (Directed Graph)**
Models a directed social-network graph and applies BFS and DFS to traverse from a starting node. Demonstrates graph traversal on directed edges with sorted neighbors for deterministic output.

> **Key Concepts:** BFS (queue-based), DFS (stack-based), path reconstruction, step cost tracking, directed vs undirected graphs.

---

### LAB-2 — BFS & DFS on 8-Puzzle

📂 **Files:** `Q1.cpp`, `Q2.cpp`

**Q1 & Q2 — 8-Puzzle State Space Search**
Solves the classic **8-Puzzle problem** using BFS and DFS. Starts from a scrambled configuration `{7,2,4,5,0,6,8,3,1}` and searches for the goal state `{0,1,2,3,4,5,6,7,8}`. Counts the total number of states explored by each algorithm to compare efficiency.

> **Key Concepts:** State space representation, sliding puzzle, tile moves (Up/Down/Left/Right), visited set, BFS completeness vs DFS memory trade-off.

---

### LAB-3 — Intelligent Agents

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Simple Reflex Vacuum Cleaner Agent (3-Room)**
Simulates a **simple reflex agent** operating in a 3-room environment (A, B, C). Rooms are randomly assigned as dirty or clean. The agent follows production rules to suck dirt or navigate rooms. Tracks performance score over 10 steps.

**Q2 — Railway Level Crossing Control System**
Implements a **rule-based production system** for a railway crossing. Given sensor inputs (train presence, obstacle, emergency), the system decides signal color, gate position, and siren state. Supports both full truth-table simulation and manual input mode.

> **Key Concepts:** Simple reflex agents, PEAS model, production rules, performance measure, environment simulation.

---

### LAB-4 — Best-First Search

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Graph Representation (City Map)**
Defines the city-graph adjacency list in Python format (same Chicago-to-Portland map as LAB-1) as a foundation for informed search experiments.

**Q2 — Non-Heuristic Best-First Search (Building Evacuation)**
Implements **Best-First Search without a heuristic** (cost-only ordering) on a 2D grid maze representing a building floor plan. Finds an evacuation path from a start cell to an exit. Uses an open-list sorted by step cost.

> **Key Concepts:** Best-first search, open/reached list, grid-based pathfinding, cost-based ordering.

---

### LAB-5 — DLS & IDS

📂 **Files:** `g1.py`, `p1.py`

**River Crossing Problem — 3 Boys & 3 Girls**
Solves the classic **Missionaries & Cannibals** variant (3 boys, 3 girls, 1 boat) where girls must never be outnumbered by boys on either riverbank.

- **Depth-Limited Search (DLS):** Explores up to a fixed depth (limit = 3). Detects states beyond the limit.
- **Iterative Deepening Search (IDS):** Incrementally increases the depth limit until a solution is found. Guaranteed to find the optimal (shortest) solution.
- Calculates the effective **branching factor** from all valid states.
- Provides a comparative analysis of explored states and time complexity.

> **Key Concepts:** State validity constraints, DLS, IDS, branching factor, completeness, optimality.

---

### LAB-6 — GBFS & A* Search

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Greedy Best-First Search & A\* Search (City Route to Boston)**
Implements both **GBFS** (`f(n) = h(n)`) and **A\*** (`f(n) = g(n) + h(n)`) on the US city graph to find a path from Chicago to Boston. Uses pre-defined heuristic values (straight-line distance to Boston). Reports step-by-step `g`, `h`, and `f` values and compares algorithm efficiency.

**Q2 — A\* Search for Multi-Reward Collection**
Applies **A\*** on a 5×5 grid where an agent must collect all reward tiles. Uses **Manhattan distance to the farthest uncollected reward** as an admissible heuristic. Tracks collected rewards in the state signature to avoid revisiting equivalent states.

> **Key Concepts:** Admissibility, consistency, priority queue, heuristic design, state augmentation, informed search.

---

### LAB-7 — Hill Climbing — 8 Queens

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Steepest-Ascent Hill Climbing (8 Queens)**
Runs **steepest-ascent hill climbing** 50 times on random 8-Queens configurations. Counts attacking pairs as the heuristic. Demonstrates local minima (failed cases). Then applies **random-restart hill climbing** until a solution is found. Visualizes the solved board with `matplotlib`.

**Q2 — Variants Comparison (8 Queens)**
Compares three hill-climbing variants over 50 runs each:
- **First-Choice Hill Climbing:** Moves to the first random neighbor that improves the heuristic.
- **Random Restart:** Restarts from scratch until a zero-conflict solution is found.
- **Simulated Annealing:** Accepts worse states with a probability that decreases with temperature (`T × 0.99` decay).

> **Key Concepts:** Local search, heuristic landscape, local minima, escape strategies, temperature scheduling.

---

### LAB-8 — TSP — Local Beam Search & Genetic Algorithm

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Local Beam Search for TSP (8 Cities)**
Solves the **Travelling Salesperson Problem** on 8 cities (A–H) using **Local Beam Search** with beam widths `k = 3, 5, 10`. Uses 2-opt swaps to generate neighbors. Compares convergence and solution quality across beam widths.

**Q2 — Genetic Algorithm for TSP**
Solves the TSP using a **Genetic Algorithm** with:
- **Single-Point Crossover** and **Two-Point Crossover**
- Tournament selection and elitism (top 2 preserved)
- Random mutation (swap two cities, 20% probability)

Runs 5 trials per crossover type and compares average cost and convergence generation.

> **Key Concepts:** TSP, population-based search, 2-opt, selection pressure, crossover operators, mutation, convergence rate.

---

### LAB-9 — Minimax & Alpha-Beta Pruning

📂 **Files:** `001.py`, `002.py`

**001 — Minimax Algorithm (Tic-Tac-Toe)**
Implements the **Minimax algorithm** for a mid-game Tic-Tac-Toe board. Evaluates all future game states recursively (X = maximizer, O = minimizer). Prints the game tree up to depth 2. Reports the best move, nodes explored, and time taken.

**002 — Alpha-Beta Pruning (Tic-Tac-Toe)**
Extends the Minimax implementation with **Alpha-Beta Pruning**. Prunes branches where `beta ≤ alpha`. Reports pruned branch count alongside nodes explored, demonstrating the efficiency gain over pure Minimax.

> **Key Concepts:** Adversarial search, game tree, terminal evaluation, maximizer/minimizer, pruning efficiency.

---

### LAB-10 — K-Means Clustering & AND-OR Graph

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Airport Location Optimization (K-Means with GD & NR)**
Applies **K-Means Clustering** to find optimal locations for 3 airports serving cities in Surat district (`cities.csv`), using two centroid-update methods:
- **Gradient Descent:** Iteratively moves centroids by `lr × gradient`.
- **Newton-Raphson:** Uses second-order Hessian to converge faster (analytically equivalent to computing the mean).

Generates cluster visualizations and SSE convergence comparison plots (`airport_clusters.png`, `convergence_comparison.png`).

**Q2 — Erratic Vacuum Agent (AND-OR Graph Search)**
Implements **AND-OR Graph Search** for a non-deterministic environment. The erratic vacuum agent may clean a dirty room *or* clean both rooms when sucking. Uses recursive `or_search` / `and_search` to find a conditional plan for every possible initial state. Prints a full branching conditional plan.

> **Key Concepts:** Unsupervised learning, SSE minimization, numerical optimization, non-deterministic agents, contingency plans.

---

### LAB-11 — Constraint Satisfaction Problems

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Graph Coloring of Gujarat Districts (Backtracking)**
Models the adjacency map of all **25 districts of Gujarat** as a CSP. Uses standard **backtracking** to find the minimum number of colors needed such that no two neighboring districts share the same color (4-color theorem). Reports the coloring for each district.

**Q2 — SEND + MORE = MONEY (Cryptarithmetic)**
Solves the classic **SEND + MORE = MONEY** cryptarithmetic puzzle using brute-force enumeration with constraint filtering. Each letter maps to a unique digit (0–9), with M ≠ 0.

> **Key Concepts:** CSP formulation, backtracking search, constraint propagation, arc consistency, map coloring.

---

### LAB-12 — Arc Consistency — AC-3

📂 **Files:** `Q1.py`, `Q2.py`

**Q1 — Room Scheduling CSP (AC-3)**
Models a room-scheduling problem with 6 teams (P1–P6) and 3 rooms (R1–R3). Conflicting teams cannot be in the same room. Implements the **AC-3 algorithm** to enforce arc consistency. Demonstrates the step-by-step arc queue and shows remaining domains after fixing P1 to R1.

**Q2 — Sudoku Puzzle Solving (AC-3)**
Applies **AC-3** to a hard Sudoku puzzle. Generates all arcs from row, column, and 3×3 box neighbors. Reports the number of domain values removed and the resulting domain-size grid. Concludes whether AC-3 fully solved the puzzle or only reduced the search space.

> **Key Concepts:** Arc consistency, AC-3 algorithm, domain reduction, constraint propagation, Sudoku as CSP.

---

### LAB-13 — Propositional Logic & Truth Tables

📂 **Files:** `Q1.py`

**Infix Logical Expression Evaluator & Truth Table Generator**
Parses any user-input propositional logic expression (e.g., `(~P|Q)->R`) in infix form. Supports:
- `~` (NOT), `&` (AND), `|` (OR), `->` (IMPLIES), `<->` (BICONDITIONAL)
- Operator precedence and associativity (shunting-yard algorithm)
- Automatic variable extraction and combination generation

Prints the full **truth table** for all variable combinations.

> **Key Concepts:** Propositional logic, operator precedence, stack-based expression evaluation, truth table, tautology/contradiction detection.

---

### LAB-14 — Knowledge-Based Inference

📂 **Files:** `q1.py`, `q2.py`, `q3.py`

**q1 — Forward Chaining (`PL-FC-ENTAILS`)**
Implements the **forward chaining** algorithm for propositional logic. Starts from known facts, fires applicable rules whose premises are all satisfied, and propagates new derived facts until the query is proven or all options are exhausted.

**q2 — Backward Chaining (`PL-BC-ENTAILS`)**
Implements **backward chaining** (goal-driven reasoning). Recursively attempts to prove a query by working backwards through rules, checking known facts and detecting cycles to avoid infinite loops.

**q3 — Resolution-Based Theorem Proving**
Implements **resolution** for propositional logic. Converts the Knowledge Base and negated query into CNF clauses, then repeatedly resolves pairs of clauses. If the empty clause (contradiction) is generated, the query is **proven**; otherwise, it is **not entailed**.

> **Key Concepts:** Knowledge base, inference rules, modus ponens, forward/backward chaining, resolution refutation, CNF clauses.

---

## 🛠️ Tech Stack

| Language | Version | Usage |
|----------|---------|-------|
| Python | 3.x | LABs 3–14 |
| C++ | C++17 | LABs 1–2 |
| NumPy | Latest | LAB-10 (K-Means) |
| Matplotlib | Latest | LABs 7, 10 (Visualization) |

---

## 📊 Topics Progression

```
Uninformed Search   →   Intelligent Agents   →   Informed Search
(BFS, DFS)              (Reflex, Rule-based)      (A*, GBFS, BEFS)

Local Search        →   Adversarial Search   →   Probabilistic/Population
(HC, SA, IDS)           (Minimax, Alpha-Beta)     (Beam, GA, K-Means)

Constraint Satisfaction  →  Logic & Reasoning
(Backtracking, AC-3)        (Truth Tables, FC, BC, Resolution)
```

---

## 📌 Notes

- All lab submissions are original implementations by **Param Rasiklal Kanada (U24AI047)**.
- Assignment PDFs and lab reports are included in each folder where applicable.
- Some folders may contain intermediate/exploratory files (`Try.cpp`, `better.py`, etc.) from the development process.

---

<div align="center">

*Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat — AI Branch | Semester 4 | 2025–26*

</div>