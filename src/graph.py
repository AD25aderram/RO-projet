"""
Ce fichier gère :
- Construction du graphe
- Tri topologique utilisant l'algorithme de Kahn
"""

def build_graph(tasks):
    """
    Construit :
    - graph: représentation en liste d'adjacence
    - in_degree: nombre d'arêtes entrantes pour chaque tâche
    """

    # Initialiser la liste d'adjacence vide
    graph = {t: [] for t in tasks}

    # Initialiser tous les degrés entrants à zéro
    in_degree = {t: 0 for t in tasks}

    # Remplir le graphe et les degrés entrants
    for task in tasks:
        for predecessor in tasks[task]["pred"]:
            graph[predecessor].append(task)  # Arête prédécesseur → tâche
            in_degree[task] += 1              # Augmenter le degré entrant de la tâche

    return graph, in_degree


def topological_sort(graph, in_degree):
    """
    Effectue le tri topologique en utilisant l'algorithme de Kahn.
    Assure que les tâches sont ordonnées en respectant les dépendances.
    """

    # Commencer avec les tâches qui n'ont pas de prédécesseurs
    queue = [t for t in in_degree if in_degree[t] == 0]

    topo_order = []

    while queue:
        # Retirer la première tâche de la file
        current = queue.pop(0)
        topo_order.append(current)

        # Réduire le degré entrant des successeurs
        for successor in graph[current]:
            in_degree[successor] -= 1

            # S'il ne reste aucun prédécesseur, ajouter à la file d'attente
            if in_degree[successor] == 0:
                queue.append(successor)

    return topo_order
