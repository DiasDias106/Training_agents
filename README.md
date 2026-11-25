# AI Algorithms and Orange Data Mining

Work from the Artificial Intelligence course: machine learning workflows built in [Orange Data Mining](https://orangedatamining.com/) and classic AI algorithms written in Python (graph algorithms, search and genetic algorithms).

## `python_algorithms/`

| Folder | Algorithms |
|---|---|
| `graph_algorithms` | Dijkstra, Bellman-Ford (picked automatically when there are negative weights), Floyd-Warshall (step by step and animated matrix), Prim and Kruskal minimum spanning trees, on a road network of Portuguese cities |
| `search_algorithms` | A* on a weighted grid with Manhattan heuristic, BFS vs. A* (nodes explored), A* route to a hospital avoiding blocked roads |
| `genetic_algorithms` | Genetic algorithm (selection, crossover, mutation) that chooses which agricultural fields to treat, balancing cost, risk and priority |

The scripts in `graph_algorithms`, `genetic_algorithms` and `astar_hospital_route.py` were written for Orange's **Python Script** widget: they read the input table from `in_data` (see the matching workflow and dataset). `astar_grid.py` and `bfs_vs_astar_grid.py` are standalone:

```bash
python python_algorithms/search_algorithms/bfs_vs_astar_grid.py
```

## `orange_workflows/`

| Workflow | Topics |
|---|---|
| `lab01_iris_decision_tree.ows` | Data exploration and decision tree classification (Iris) |
| `lab04_iris_knn_classification.ows` | kNN classification, confusion matrix, linear projection |
| `lab05_wine_linear_regression_vs_decision_tree.ows` | Linear regression vs. decision tree, permutation plot |
| `lab06_heart_disease_knn_tree_regression.ows` | kNN, decision trees and linear regression on the Cleveland heart disease dataset |
| `lab07_graph_shortest_paths_and_mst_python.ows` | Graph algorithms in Python Script widgets, heat map of distances |
| `lab08_genetic_algorithm_field_selection_python.ows` | Genetic algorithm in a Python Script widget, scatter and bar plots of the result |
| `test1_student_performance_regression_and_classification.ows` | Regression and classification of student performance: linear regression, random forest, kNN, trees |
| `test2_hospital_route_astar_and_genetic_algorithm.ows` | A* route to a hospital and genetic algorithm |
| `test2_hospital_route_knn_tree_and_genetic_algorithm.ows` | kNN and decision tree on the hospital routes dataset, plus genetic algorithm |

The datasets used by the workflows are in `orange_workflows/datasets`. When opening a workflow, Orange may ask you to point the **CSV File Import** widget to the matching file in that folder.
