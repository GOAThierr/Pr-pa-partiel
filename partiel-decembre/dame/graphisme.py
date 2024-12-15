import tkinter as tk
from tkinter import messagebox

class Graphisme:
    def __init__(self, jeu):
        self.jeu = jeu
        self.root = tk.Tk()
        self.root.title("Jeu de Dames")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.clic_case)
        self.selection = None  # Aucune pièce sélectionnée au départ
        self.dessiner_plateau()

    def dessiner_plateau(self):
        """Dessine le plateau et les pièces"""
        self.canvas.delete("all")  # Supprime les dessins précédents
        for i in range(8):
            for j in range(8):
                couleur = "black" if (i + j) % 2 == 0 else "white"
                self.canvas.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=couleur)

                # Dessiner les pièces
                piece = self.jeu.get_plateau().cases[i][j]
                if piece:
                    couleur_piece = 'black' if piece == 'Noir' else 'white'
                    self.canvas.create_oval(i * 50 + 10, j * 50 + 10, (i + 1) * 50 - 10, (j + 1) * 50 - 10, fill=couleur_piece)

        # Affichage du joueur actif
        joueur_actuel = self.jeu.obtenir_joueur_actuel()
        self.canvas.create_text(200, 380, text=f"Joueur {1 if joueur_actuel == 1 else 2} à l'action", font=("Arial", 12), fill = 'red')

    def clic_case(self, event):
        """Gère le clic sur une case du plateau"""
        x, y = event.x // 50, event.y // 50  # Coordonnées de la case cliquée
        plateau = self.jeu.get_plateau()

        if self.selection:  # Si une pièce est sélectionnée
            x1, y1 = self.selection
            if self.jeu.effectuer_deplacement(x1, y1, x, y):  # Valider le déplacement
                self.dessiner_plateau()  # Re-dessiner le plateau après le déplacement
                self.selection = None
            else:
                messagebox.showerror("Erreur", "Déplacement ou capture invalide")
                self.selection = None  # Annuler la sélection si invalide
        else:  # Si aucune pièce n'est sélectionnée
            if plateau.cases[x][y] == ('Noir' if self.jeu.obtenir_joueur_actuel() == 1 else 'Blanc'):
                self.selection = (x, y)  # Sélectionner la pièce

        # Re-dessiner le plateau
        self.dessiner_plateau()

    def lancer(self):
        """Lancer la boucle principale de tkinter"""
        self.root.mainloop()
