import random
from cartes import Carte

class Plateau:
    def __init__(self):
        self.piles = [[] for _ in range(7)]
        self.talon = []
        self.colonnes = [[] for _ in range(7)]
        self.initialiser_cartes()

    def initialiser_cartes(self):
        valeurs = list(range(1, 14))  # 1 à 13 pour As à Roi
        couleurs = ['♠', '♥', '♦', '♣']
        deck = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(deck)

        for i in range(7):
            for j in range(i + 1):
                carte = deck.pop()
                if j == i:
                    carte.rendre_visible()
                carte.position = (100 + i * 60, 50 + j * 20)
                self.piles[i].append(carte)

        self.talon = deck

    def trouver_carte(self, x, y):
        for pile in self.piles:
            for carte in reversed(pile):  # Vérifie les cartes visibles en premier
                cx, cy = carte.position
                if cx <= x <= cx + 50 and cy <= y <= cy + 80:
                    return carte
        return None

    def selectionner_carte(self, carte):
        # Logique simplifiée de sélection et déplacement
        if carte.visible:
            print(f"Carte sélectionnée : {carte}")
