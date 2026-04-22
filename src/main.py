# Types de donnees complexes - Bloc 2

# 1. Liste : tous les animaux de la grille 

animaux = ["lapin","renard","lapin","lapin","renard"]

# 2.Dictionnaire : caracteristique d'un animal

lapin = {

"nom": "Lapin",
"energie" :10,
"age":0,
"position": (3,5)


}

renard = {


"nom": "Renard",
"energie" :15,
"age":0,
"position": (1,2)

}
# 3. Tuple : position sur la grille (x,y)
position_lapin = (3,5)
position_renard = (1,2)

#Affichage
print("=== SIMULATEUR D'ECOSYSTEME ===")
print("Animaux presents :", animaux)
print("Details lapin :", lapin)
print("position  lapin:", position_lapin)
print("Position renard :", position_renard )