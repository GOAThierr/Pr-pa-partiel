from jeu import Jeu
from graphism import Graphique

def main():
    # Initialisation du jeu
    jeu = Jeu()

    # Initialisation de l'interface graphique
    graphique = Graphique(jeu)

    # Lancement de l'interface graphique
    graphique.lancer_interface()

if __name__ == "__main__":
    main()
