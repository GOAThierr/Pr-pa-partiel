from jeu import Jeu
from graphisme import Graphisme

if __name__ == "__main__":
    # Créer l'instance de Jeu et l'interface graphique
    jeu = Jeu()
    graphique = Graphisme(jeu)
    graphique.lancer()
