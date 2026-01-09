"""
Fichier d'exécution principal pour le projet PERT
"""

from src.data import tasks
from src.graph import build_graph, topological_sort
from src.pert import (
    compute_earliest,
    compute_latest,
    compute_slack,
    critical_path
)

def main():
    # Construire le graphe du projet
    graph, in_degree = build_graph(tasks)

    # Effectuer le tri topologique
    topo = topological_sort(graph, in_degree)
    print(topo)

    # Calculer les dates au plus tôt
    earliest_start, earliest_finish = compute_earliest(tasks, graph, topo)

    # Durée du projet = temps de fin de la dernière tâche
    project_duration = earliest_finish[topo[-1]]

    # Calculer les dates au plus tard
    latest_start, latest_finish = compute_latest(
        tasks, topo, project_duration
    )

    # Calculer la marge pour chaque tâche
    slack = compute_slack(tasks, earliest_start, latest_start)

    # Identifier le chemin critique
    cp = critical_path(topo, slack)

    # Afficher les résultats
    print("=== EARLIEST DATES ===")
    for t in topo:
        print(f"Task {t}: Start={earliest_start[t]}, Finish={earliest_finish[t]}")

    print("\n=== LATEST DATES ===")
    for t in topo:
        print(f"Task {t}: Start={latest_start[t]}, Finish={latest_finish[t]}")

    print("\nMinimal project duration:", project_duration)
    print("Critical path:", " -> ".join(cp))


if __name__ == "__main__":
    main()
