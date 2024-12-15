import tkinter as tk
from tkinter import messagebox

class InterfaceGraphique:
    def __init__(self, plateau):
        self.plateau = plateau
        self.root = tk.Tk()
        self.root.title("Solitaire")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="green")
        self.canvas.pack()
        self.cartes_graphiques = {}
        self.creer_elements_graphiques()
        self.root.bind("<Button-1>", self.gestion_clic)

    def creer_elements_graphiques(self):
        for pile in self.plateau.piles:
            for carte in pile:
                self.ajouter_carte_graphique(carte)

    def ajouter_carte_graphique(self, carte):
        x, y = carte.position
        rectangle = self.canvas.create_rectangle(
            x, y, x + 50, y + 80, fill="white", outline="black"
        )
        texte = self.canvas.create_text(
            x + 25, y + 40, text=str(carte), fill="black"
        )
        self.cartes_graphiques[carte] = (rectangle, texte)

    def gestion_clic(self, event):
        carte = self.plateau.trouver_carte(event.x, event.y)
        if carte:
            self.plateau.selectionner_carte(carte)
            self.actualiser()

    def actualiser(self):
        for carte, (rectangle, texte) in self.cartes_graphiques.items():
            x, y = carte.position
            self.canvas.coords(rectangle, x, y, x + 50, y + 80)
            self.canvas.coords(texte, x + 25, y + 40)

    def demarrer(self):
        self.root.mainloop()
