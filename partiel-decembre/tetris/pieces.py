import random

class Piece:
    def __init__(self, forme, x, y):
        self.forme = forme
        self.x = x
        self.y = y

    def get_forme(self):
        return self.forme

    def get_forme_tournee(self):
        return [(-y, x) for x, y in self.forme]

    def tourner(self):
        self.forme = self.get_forme_tournee()

class PiecesFactory:
    @staticmethod
    def creer_piece(largeur):
        formes = [
            [(0, 0), (1, 0), (0, 1), (1, 1)],  # Carré
            [(0, 0), (1, 0), (2, 0), (3, 0)],  # Ligne
            [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z
            [(0, 1), (1, 1), (1, 0), (2, 0)],  # S inversé
            [(0, 0), (1, 0), (2, 0), (1, 1)],  # T
            [(0, 0), (0, 1), (1, 1), (2, 1)],  # L
            [(2, 0), (0, 1), (1, 1), (2, 1)],  # L inversé
        ]
        forme = random.choice(formes)
        return Piece(forme, largeur // 2, 0)
