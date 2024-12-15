class Grille:
    def __init__(self, taille=3):
        self.taille = taille
        self.grille = [[" " for _ in range(self.taille)] for _ in range(self.taille)]

    def placer_pion(self, ligne, colonne, symbole):
        if 0 <= ligne < self.taille and 0 <= colonne < self.taille:
            if self.grille[ligne][colonne] == " ":
                self.grille[ligne][colonne] = symbole
                return True
        return False

    def verifier_victoire(self, symbole):
        # Vérification des lignes et colonnes
        for i in range(self.taille):
            if all(self.grille[i][j] == symbole for j in range(self.taille)):  # Ligne
                return True
            if all(self.grille[j][i] == symbole for j in range(self.taille)):  # Colonne
                return True

        # Vérification des diagonales
        if all(self.grille[i][i] == symbole for i in range(self.taille)):  # Diagonale principale
            return True
        if all(self.grille[i][self.taille - i - 1] == symbole for i in range(self.taille)):  # Diagonale secondaire
            return True

        return False

    def est_pleine(self):
        return all(self.grille[i][j] != " " for i in range(self.taille) for j in range(self.taille))
