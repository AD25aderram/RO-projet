"""
Ce fichier contient les données du projet.
Chaque tâche est représentée par :
- duration: temps nécessaire pour terminer la tâche
- pred: liste des tâches prédécesseurs qui doivent finir avant que cette tâche commence
"""

# Dictionnaire des tâches
tasks = {
    "A": {"duration": 2,  "pred": []},           # La tâche A n'a pas de prédécesseurs
    "B": {"duration": 15, "pred": ["A"]},        # B commence après A
    "C": {"duration": 10, "pred": ["A"]},        # C commence après A
    "D": {"duration": 8,  "pred": ["B"]},        # D commence après B
    "E": {"duration": 5,  "pred": ["C"]},        # E commence après C
    "F": {"duration": 12, "pred": ["B", "C"]},   # F commence après B et C
    "G": {"duration": 20, "pred": ["A"]},        # G commence après A
    "H": {"duration": 25, "pred": ["D", "E", "F"]}, # H commence après D, E, F
    "I": {"duration": 10, "pred": ["G", "H"]}    # task final
}
