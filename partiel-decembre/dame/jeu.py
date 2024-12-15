from plateau import Plateau

class Jeu:
    def __init__(self):
        self.plateau = Plateau()
        self.joueur_actuel = 1  # 1 pour le joueur 1 (noir), -1 pour le joueur 2 (blanc)

    def changer_joueur(self):
        """Changer de joueur après un déplacement"""
        self.joueur_actuel = -self.joueur_actuel

    def effectuer_deplacement(self, x1, y1, x2, y2):
        """Effectuer un déplacement sur le plateau"""
        if self.plateau.valider_deplacement(x1, y1, x2, y2, self.joueur_actuel):
            self.plateau.deplacer(x1, y1, x2, y2)
            self.changer_joueur()
            return True
        return False

    def get_plateau(self):
        """Obtenir l'état actuel du plateau"""
        return self.plateau

    def obtenir_joueur_actuel(self):
        """Retourner le joueur actuel"""
        return self.joueur_actuel
