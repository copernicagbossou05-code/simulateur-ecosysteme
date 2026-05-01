import random
from lapin import Lapin
from renard import Renard
from persistance import sauvegarder

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.animaux = []
        self.tour_actuel = 0

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def afficher(self):
        print(f"\n=== Grille {self.largeur}x{self.hauteur} ===")
        print(f"Lapins : {len([a for a in self.animaux if isinstance(a, Lapin) and a.est_vivant()])}")
        print(f"Renards : {len([a for a in self.animaux if isinstance(a, Renard) and a.est_vivant()])}")

    def tour(self):
        nouveaux_animaux = []
        nb_lapins = len([a for a in self.animaux if isinstance(a, Lapin) and a.est_vivant()])
        nb_renards_nes_ce_tour = 0  # limite de naissance par tour

        for animal in self.animaux:
            if animal.est_vivant():
                animal.vieillir()

                if not animal.est_vivant():
                    continue

                # Mort naturelle
                if isinstance(animal, Lapin):
                    if random.random() < 0.05:
                        print("Un lapin est mort de maladie ou de l'environnement !")
                        animal.mourir()
                        continue

                if isinstance(animal, Renard):
                    if random.random() < 0.01:
                        print("Un renard est mort de maladie ou de l'environnement !")
                        animal.mourir()
                        continue

                # Actions des lapins
                if isinstance(animal, Lapin) and animal.est_vivant():
                    animal.manger()
                    bebes = animal.se_reproduire()
                    if bebes:
                        nouveaux_animaux.extend(bebes)

                # Actions des renards
                if isinstance(animal, Renard) and animal.est_vivant():
                    lapins_disponibles = [
                        a for a in self.animaux
                        if isinstance(a, Lapin) and a.est_vivant()
                    ]
                    animal.chasser(lapins_disponibles)
                    animal.verifier_faim()
                    if animal.est_vivant() and nb_renards_nes_ce_tour < 2:
                        bebe_renard = animal.se_reproduire(nb_lapins)
                        if bebe_renard:
                            nouveaux_animaux.append(bebe_renard)
                            nb_renards_nes_ce_tour += 1

        self.animaux += nouveaux_animaux
        self.animaux = [a for a in self.animaux if a.est_vivant()]

        nb_lapins = len([a for a in self.animaux if isinstance(a, Lapin)])
        nb_renards = len([a for a in self.animaux if isinstance(a, Renard)])
        self.tour_actuel += 1
        sauvegarder(self.tour_actuel, nb_lapins, nb_renards)