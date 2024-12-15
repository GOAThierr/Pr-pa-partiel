class Plateau:
    def __init__(self):
        # Créer un plateau de 8x8 avec les pièces initiales
        self.cases = [[None for _ in range(8)] for _ in range(8)]
        self.initialiser_plateau()

    def initialiser_plateau(self):
        # Placer les pièces sur le plateau de façon initiale
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 != 0:  # Placer des pièces sur les cases noires
                    if i < 3:
                        self.cases[i][j] = 'Noir'
                    elif i > 4:
                        self.cases[i][j] = 'Blanc'

    def valider_deplacement(self, x1, y1, x2, y2, joueur):
        """Vérifier si un déplacement est valide, y compris les captures"""
        if self.cases[x1][y1] == ('Noir' if joueur == 1 else 'Blanc'):
            # Vérifier si la case de destination est vide
            if self.cases[x2][y2] is None:
                # Vérification pour un déplacement simple (1 case en diagonale)
                if abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
                    return True
                # Vérification pour une capture (sauter une pièce adverse)
                elif abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
                    # Vérifier qu'il y a bien une pièce adverse à capturer
                    x_milieu, y_milieu = (x1 + x2) // 2, (y1 + y2) // 2
                    piece_milieu = self.cases[x_milieu][y_milieu]
                    if piece_milieu and piece_milieu != ('Noir' if joueur == 1 else 'Blanc'):
                        return True
        return False

    def deplacer(self, x1, y1, x2, y2):
        """Déplacer une pièce sur le plateau (effectuer un déplacement ou une capture)"""
        if abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
            # Si c'est une capture, retirer la pièce capturée
            x_milieu, y_milieu = (x1 + x2) // 2, (y1 + y2) // 2
            self.cases[x_milieu][y_milieu] = None  # Retirer la pièce capturée
        # Déplacer la pièce sur la nouvelle case
        self.cases[x2][y2] = self.cases[x1][y1]
        self.cases[x1][y1] = None

    def afficher(self):
        """Affichage du plateau dans la console (à titre de test)"""
        for row in self.cases:
            print(row)
