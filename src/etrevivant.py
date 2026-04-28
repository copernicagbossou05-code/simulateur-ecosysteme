#classe mere 
class EtreVivant:
    def __init__(self, x, y , energie):
        self.x = x
        self.y = y
        self.energie = energie
        self.age = 0
        self.vivant = True
        
    def vieillir(self):
        self.age += 1
        self.energie -= 1

    def est_vivant(self): 
        return self.vivant
    
    def mourir(self):
        self.vivant = False
        print(f"Un etre vivant est mort a l'age de {self.age}")


    
    def __str__(self) :
        return f"Animal en ({self.x},{self.y}) | energie : {self.energie} | age : {self.age}"
    
  