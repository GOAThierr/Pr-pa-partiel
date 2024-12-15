from graphism import Graphism
from pieces import Piece, PiecesFactory

class Jeu:
    def __init__(self):
        self.largeur = 10
        self.hauteur = 20
        self.grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        self.piece_actuelle = None
        self.en_cours = True
        self.graphisme = Graphism(self.largeur, self.hauteur, self)
        self.score = 0  # Initialisation du score

    def nouvelle_piece(self):
        """Crée une nouvelle pièce."""
        self.piece_actuelle = PiecesFactory.creer_piece(self.largeur)

    def verifier_collision(self, dx, dy, rotation=False):
        """Vérifie si un déplacement ou une rotation entraînerait une collision."""
        forme = self.piece_actuelle.get_forme()
        if rotation:
            forme = self.piece_actuelle.get_forme_tournee()
        for x, y in forme:
            nx, ny = x + self.piece_actuelle.x + dx, y + self.piece_actuelle.y + dy
            if nx < 0 or nx >= self.largeur or ny < 0 or ny >= self.hauteur or (ny >= 0 and self.grille[ny][nx]):
                return True
        return False

    def fixer_piece(self):
        """Fixe la pièce actuelle sur la grille."""
        for x, y in self.piece_actuelle.get_forme():
            self.grille[self.piece_actuelle.y + y][self.piece_actuelle.x + x] = 1
        self.supprimer_lignes()
        self.nouvelle_piece()

    def supprimer_lignes(self):
        """Supprime les lignes complètes et met à jour le score."""
        lignes_completees = [ligne for ligne in self.grille if all(cell == 1 for cell in ligne)]
        nb_lignes = len(lignes_completees)
        if nb_lignes > 0:
            # Ajouter des points selon le nombre de lignes supprimées
            if nb_lignes == 1:
                self.score += 100
            elif nb_lignes == 2:
                self.score += 300
            elif nb_lignes == 3:
                self.score += 500
            elif nb_lignes == 4:
                self.score += 800

        # Supprimer les lignes complètes
        self.grille = [ligne for ligne in self.grille if any(cell == 0 for cell in ligne)]
        while len(self.grille) < self.hauteur:
            self.grille.insert(0, [0] * self.largeur)

    def actualiser(self):
        """Fait descendre la pièce automatiquement ou la fixe si elle atteint un obstacle."""
        if self.verifier_collision(0, 1):
            if self.piece_actuelle.y == 0:
                self.en_cours = False  # Fin du jeu
                self.graphisme.afficher_message(f"Game Over!\nScore: {self.score}")
            else:
                self.fixer_piece()
        else:
            self.piece_actuelle.y += 1
        self.graphisme.actualiser_grille()
        if self.en_cours:
            self.graphisme.root.after(500, self.actualiser)  # Rappelle cette fonction après 500 ms

    def deplacer_piece(self, dx, dy):
        """Déplace la pièce horizontalement ou verticalement."""
        if not self.verifier_collision(dx, dy):
            self.piece_actuelle.x += dx
            self.piece_actuelle.y += dy
            self.graphisme.actualiser_grille()

    def tourner_piece(self):
        """Fait tourner la pièce si possible."""
        if not self.verifier_collision(0, 0, rotation=True):
            self.piece_actuelle.tourner()
            self.graphisme.actualiser_grille()

    def lancer(self):
        """Lance le jeu."""
        self.nouvelle_piece()
        self.graphisme.actualiser_grille()
        self.actualiser()  # Démarre la descente automatique
        self.graphisme.afficher()
