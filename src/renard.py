from etrevivant import EtreVivant

class Renard(EtreVivant):
    def __init__(self, x, y):
        super().__init__(x, y, energie=15)
        self.faim = 0

    def chasser(self, lapin):
        if lapin.est_vivant():
            lapin.mourir()
            self.energie += 10
            #Si le renard mange un lapin alors son énergie s'incrémente de 10
            
            print(f"Le renard a mange un lapin.Energie : {self.energie}")
        else:
            self.faim += 1
            print("Pas de lapin a chasser !")
    def verifier_faim(self):
        if self.faim >=3: 

            self.mourir()

