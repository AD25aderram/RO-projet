"""
Ce fichier implémente les calculs PERT :
- Temps de début / fin au plus tôt
- Temps de début / fin au plus tard
- Marge (float)
- Chemin critique
"""

def compute_earliest(tasks, graph, topo):
    """
    Calcule les temps de début au plus tôt (ES) et de fin au plus tôt (EF)
    """

    # Initialiser les temps de début au plus tôt à zéro
    earliest_start = {t: 0 for t in tasks}
    earliest_finish = {}

    for task in topo:
        # EF = ES + durée
        earliest_finish[task] = (
            earliest_start[task] + tasks[task]["duration"]
        )

        # Mettre à jour les temps de début au plus tôt des successeurs
        for successor in graph[task]:
            if earliest_start[successor] < earliest_finish[task]:
                earliest_start[successor] = earliest_finish[task]

    return earliest_start, earliest_finish


def compute_latest(tasks, topo, project_duration):
    """
    Calcule les temps de début au plus tard (LS) et de fin au plus tard (LF)
    """

    # Initialiser les temps de fin au plus tard à la durée du projet
    latest_finish = {t: project_duration for t in tasks}
    latest_start = {}

    # Parcourir les tâches dans l'ordre topologique inverse
    for task in reversed(topo):
        # LS = LF - durée
        latest_start[task] = (
            latest_finish[task] - tasks[task]["duration"]
        )

        # Mettre à jour les temps de fin au plus tard des prédécesseurs
        for predecessor in tasks[task]["pred"]:
            if latest_finish[predecessor] > latest_start[task]:
                latest_finish[predecessor] = latest_start[task]

    return latest_start, latest_finish


def compute_slack(tasks, earliest_start, latest_start):
    """
    Calcule la marge pour chaque tâche :
    Marge = LS - ES
    """

    slack = {}
    for task in tasks:
        slack[task] = latest_start[task] - earliest_start[task]

    return slack


def critical_path(topo, slack):
    """
    Extrait le chemin critique :
    tâches avec une marge nulle
    """

    return [task for task in topo if slack[task] == 0]
