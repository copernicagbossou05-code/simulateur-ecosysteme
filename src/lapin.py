from etrevivant import EtreVivant

class Lapin(EtreVivant):
    def __init__(self,x,y):
        super ().__init__(x,y,energie=10)
        self.age_reproduction = 0

    def manger(self): 
        self.energie +=5
        print(f"Le lapin mange de l'herbe. Energie : {self.energie}")
 
    def se_reproduire(self):
        if self.energie > 15 and self.age > 2:
            print("Un nouveau lapin est ne !")
            self.energie -= 5
            return Lapin(self.x, self.y)
        return None 