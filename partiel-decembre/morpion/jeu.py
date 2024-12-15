from grille import Grille
from joueur import Joueur

class Jeu:
    def __init__(self):
        self.grille = Grille()
        self.joueurs = [Joueur("X"), Joueur("O")]
        self.joueur_actuel = 0
        self.partie_terminee = False

    def jouer_coup(self, ligne, colonne):
        if self.partie_terminee:
            return "La partie est terminée."

        joueur = self.joueurs[self.joueur_actuel]

        if self.grille.placer_pion(ligne, colonne, joueur.symbole):
            if self.grille.verifier_victoire(joueur.symbole):
                self.partie_terminee = True
                return f"Le joueur {joueur.symbole} a gagné !"
            elif self.grille.est_pleine():
                self.partie_terminee = True
                return "Match nul !"
            else:
                self.joueur_actuel = (self.joueur_actuel + 1) % 2
                return "Coup joué."
        else:
            return "Case invalide."

    def etat_grille(self):
        return self.grille.grille
