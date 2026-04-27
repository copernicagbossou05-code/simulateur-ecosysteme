import json
import os

def sauvegarder(tour, nb_lapins, nb_renards):
    #chargement des donnees existantes maintenant
    if os.path.exists("stats.json"):
        with open("stats.json","r" ) as f:
            stats = json.load(f)
    else:
        stats = []

        #Ajout des nouvelles donnees
    stats.append({
        "tour": tour,
        "nb_lapins": nb_lapins,
        "nb_renards": nb_renards
        })

        #sauvegardes dans le fichier
    with open("stats.json", "w") as f:
        json.dump(stats, f,indent=4)
    print(f"Tour {tour} sauvegarde: {nb_lapins} lapins, {nb_renards} renards")

def charger():
    if os.path.exists("stats.json"):
        with open("stats.json","r") as f:
            return json.load(f)
    return []