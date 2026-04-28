import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from grille import Grille
from lapin import Lapin
from renard import Renard

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulateur d'Ecosysteme")
        self.grille = Grille(10, 10)
        self.grille.ajouter_animal(Lapin(1, 1))
        self.grille.ajouter_animal(Lapin(2, 3))
        self.grille.ajouter_animal(Lapin(4, 4))
        self.grille.ajouter_animal(Renard(5, 5))

        # Titre
        self.titre = tk.Label(root, text="Simulateur d'Ecosysteme", font=("Arial", 16))
        self.titre.pack(pady=10)

        # Affichage lapins
        self.label_lapins = tk.Label(root, text="Lapins : 3", font=("Arial", 12))
        self.label_lapins.pack(pady=5)

        # Affichage renards
        self.label_renards = tk.Label(root, text="Renards : 1", font=("Arial", 12))
        self.label_renards.pack(pady=5)

        # Affichage tour
        self.label_tour = tk.Label(root, text="Tour : 0", font=("Arial", 12))
        self.label_tour.pack(pady=5)

        # Bouton tour suivant
        self.bouton = tk.Button(root, text="Tour Suivant", command=self.tour_suivant, font=("Arial", 12))
        self.bouton.pack(pady=20)

    def tour_suivant(self):
        self.grille.tour()
        nb_lapins = len([a for a in self.grille.animaux if isinstance(a, Lapin)])
        nb_renards = len([a for a in self.grille.animaux if isinstance(a, Renard)])
        self.label_lapins.config(text=f"Lapins : {nb_lapins}")
        self.label_renards.config(text=f"Renards : {nb_renards}")
        self.label_tour.config(text=f"Tour : {self.grille.tour_actuel}")

# Lancement
root = tk.Tk()
app = Interface(root)
root.mainloop()