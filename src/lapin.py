from etrevivant import EtreVivant

class Lapin(EtreVivant):
    def __init__(self, x, y):
        super().__init__(x, y, energie=20)
        self.tours_depuis_reproduction = 0
        self.nb_reproductions = 0
        self.tours_menopause = 0

    def manger(self):
        self.energie += 5

    def se_reproduire(self):
        if self.nb_reproductions >= 3:
            self.tours_menopause += 1
            print(f"Un lapin est en menopause (tour {self.tours_menopause}/3)")
            if self.tours_menopause >= 3:
                print("Un lapin est mort de vieillesse apres menopause !")
                self.mourir()
            return []

        self.tours_depuis_reproduction += 1
        if self.tours_depuis_reproduction >= 4 and self.age > 1:
            self.tours_depuis_reproduction = 0
            self.nb_reproductions += 1
            self.energie -= 3
            print(f"1 lapin vient de naitre ! (reproduction {self.nb_reproductions}/3)")
            return [Lapin(self.x, self.y)]
        return []