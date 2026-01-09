"""
Tests unitaires pour l'implémentation PERT
"""

import unittest
from src.data import tasks
from src.graph import build_graph, topological_sort
from src.pert import compute_earliest, compute_latest, compute_slack, critical_path

class TestPERT(unittest.TestCase):

    def setUp(self):
        # Préparer les données de test communes
        self.graph, self.in_degree = build_graph(tasks)
        self.topo = topological_sort(self.graph, self.in_degree)

        self.es, self.ef = compute_earliest(tasks, self.graph, self.topo)
        self.project_duration = self.ef[self.topo[-1]]

        self.ls, self.lf = compute_latest(
            tasks, self.topo, self.project_duration
        )

        self.slack = compute_slack(tasks, self.es, self.ls)

    def test_project_duration(self):
        # Vérifier si la durée du projet est correcte
        self.assertEqual(self.project_duration, 62)

    def test_slack_non_negative(self):
        # La marge ne devrait jamais être négative
        for task in self.slack:
            self.assertGreaterEqual(self.slack[task], 0)

    def test_critical_path_exists(self):
        # Vérifier la présence des tâches critiques connues
        cp = critical_path(self.topo, self.slack)
        for task in ["A", "B", "D", "H", "I"]:
            self.assertIn(task, cp)

if __name__ == "__main__":
    unittest.main()
