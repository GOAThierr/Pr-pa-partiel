import tkinter as tk

class Graphism:
    def __init__(self, largeur, hauteur, jeu):
        self.jeu = jeu
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = 30
        self.root = tk.Tk()
        self.root.title("Tetris")
        self.canvas = tk.Canvas(
            self.root,
            width=self.largeur * self.taille_case,
            height=self.hauteur * self.taille_case,
            bg="black"
        )
        self.canvas.pack()
        self.root.bind("<Key>", self.gestion_clavier)

    def afficher(self):
        self.actualiser_grille()
        self.root.mainloop()

    def actualiser_grille(self):
        self.canvas.delete("all")
        # Dessiner la grille
        for y, ligne in enumerate(self.jeu.grille):
            for x, cell in enumerate(ligne):
                if cell:
                    self.dessiner_case(x, y, "blue")
        # Dessiner la pièce en cours
        if self.jeu.piece_actuelle:
            for x, y in self.jeu.piece_actuelle.get_forme():
                self.dessiner_case(x + self.jeu.piece_actuelle.x, y + self.jeu.piece_actuelle.y, "red")
        # Afficher le score
        self.canvas.create_text(
            10, 10, anchor="nw", text=f"Score: {self.jeu.score}", fill="white", font=("Arial", 16)
        )

    def dessiner_case(self, x, y, couleur):
        self.canvas.create_rectangle(
            x * self.taille_case,
            y * self.taille_case,
            (x + 1) * self.taille_case,
            (y + 1) * self.taille_case,
            fill=couleur,
            outline="black"
        )

    def gestion_clavier(self, event):
        if event.keysym == "Left":
            self.jeu.deplacer_piece(-1, 0)
        elif event.keysym == "Right":
            self.jeu.deplacer_piece(1, 0)
        elif event.keysym == "Down":
            self.jeu.deplacer_piece(0, 1)
        elif event.keysym == "Up":
            self.jeu.tourner_piece()

    def actualiser_grille(self):
        self.canvas.delete("all")
        # Dessiner la grille
        for y, ligne in enumerate(self.jeu.grille):
            for x, cell in enumerate(ligne):
                if cell:
                    self.dessiner_case(x, y, "blue")
        # Dessiner la pièce en cours
        if self.jeu.piece_actuelle:
            for x, y in self.jeu.piece_actuelle.get_forme():
                self.dessiner_case(x + self.jeu.piece_actuelle.x, y + self.jeu.piece_actuelle.y, "red")
        # Afficher le score
        self.canvas.create_text(
            10, 10, anchor="nw", text=f"Score: {self.jeu.score}", fill="white", font=("Arial", 16)
        )

    def afficher_message(self, message):
        """Affiche un message sur le canvas."""
        self.canvas.create_text(
            self.largeur * self.taille_case // 2,
            self.hauteur * self.taille_case // 2,
            text=message,
            fill="white",
            font=("Arial", 24),
            anchor="center"
        )
