import random
from lapin import Lapin
from renard import Renard

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def afficher(self):
        print(f"\n===Grille {self.largeur}x{self.hauteur }===")
        print(f"Lapins : {len([a for a in self.animaux if isinstance(a,Lapin) and a.est_vivant()])}")
        print(f"Renards : {len([a for a in self.animaux if isinstance(a,Renard) and a.est_vivant()])}")

    def tour(self):
        nouveaux_animaux = []

        for animal in self.animaux:
            if animal.est_vivant():
                animal.viellir()

                if isinstance(animal, Lapin ):
                    bebe = animal.se_reproduire()
                    if bebe:
                        nouveaux_animaux.append(bebe)

                if isinstance(animal, Renard):
                    for proie in self.animaux:
                        if isinstance(proie, Lapin) and proie.est_vivant():
                            animal.chasser(proie)
                            break
                    animal.verifier_faim()

        self.animaux += nouveaux_animaux

        self.animaux = [a for a in self.animaux if a.est_vivant()]




