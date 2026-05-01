from etrevivant import EtreVivant
import random

class Renard(EtreVivant):
    def __init__(self, x, y):
        super().__init__(x, y, energie=15)
        self.faim = 0
        self.tours_depuis_reproduction = 0
        self.nb_reproductions = 0
        self.tours_menopause = 0

    def chasser(self, lapins_disponibles):
        # Le renard ne chasse que s'il a besoin
        if self.energie > 20:
            print(f"Un renard est rassasie et ne chasse pas.")
            return

        if not lapins_disponibles:
            self.faim += 1
            print("Un renard n'a trouve aucune proie !")
            return

        chance = random.random()

        if chance < 0.25:
            self.faim += 1
            print("Un renard vient de rater sa proie ! Le lapin s'est echappe !")
        elif chance < 0.65:
            lapin = lapins_disponibles[0]
            lapin.mourir()
            self.energie += 8
            self.faim = 0
            print(f"Un renard a capture 1 lapin ! Energie : {self.energie}")
        else:
            if len(lapins_disponibles) >= 2:
                for lapin in lapins_disponibles[:2]:
                    lapin.mourir()
                self.energie += 16
                self.faim = 0
                print(f"Un renard a capture 2 lapins ! Energie : {self.energie}")
            else:
                lapins_disponibles[0].mourir()
                self.energie += 8
                self.faim = 0
                print(f"Un renard a capture 1 lapin ! Energie : {self.energie}")

    def se_reproduire(self, nb_lapins):
        if self.nb_reproductions >= 5:
            self.tours_menopause += 1
            print(f"Un renard est en menopause (tour {self.tours_menopause}/5)")
            if self.tours_menopause >= 5:
                print("Un renard est mort de vieillesse apres menopause !")
                self.mourir()
            return None

        if nb_lapins < 10:
            return None

        self.tours_depuis_reproduction += 1
        if self.tours_depuis_reproduction >= 3 and self.age > 2:
            self.tours_depuis_reproduction = 0
            self.nb_reproductions += 1
            self.energie -= 10
            print(f"Un nouveau renard est ne ! (reproduction {self.nb_reproductions}/5)")
            return Renard(self.x, self.y)
        return None

    def verifier_faim(self):
        if self.faim >= 4:
            print("Un renard est mort de faim !")
            self.mourir()

    def vieillir(self):
        self.age += 1
        self.energie -= 1
        if self.age > 20:
            print("Un renard est mort de vieillesse !")
            self.mourir()