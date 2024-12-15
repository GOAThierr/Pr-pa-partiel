import tkinter as tk

class Graphique:
    def __init__(self, jeu):
        self.jeu = jeu
        self.root = tk.Tk()
        self.root.title("Morpion")
        self.boutons = []
        self.creer_interface()

    def creer_interface(self):
        frame = tk.Frame(self.root)
        frame.pack()

        # Création des boutons pour la grille
        for ligne in range(self.jeu.grille.taille):
            row = []
            for colonne in range(self.jeu.grille.taille):
                bouton = tk.Button(frame, text=" ", font=("Arial", 24), width=3, height=1,
                                   command=lambda l=ligne, c=colonne: self.jouer(l, c))
                bouton.grid(row=ligne, column=colonne)
                row.append(bouton)
            self.boutons.append(row)

    def jouer(self, ligne, colonne):
        # Jouer un coup dans la case sélectionnée
        resultat = self.jeu.jouer_coup(ligne, colonne)
        self.mettre_a_jour_interface()

        if "gagné" in resultat or "Match nul" in resultat:
            self.afficher_message(resultat)
            # Désactiver tous les boutons une fois la partie terminée
            for row in self.boutons:
                for bouton in row:
                    bouton.config(state="disabled")

    def mettre_a_jour_interface(self):
        # Mettre à jour les boutons en fonction de l'état de la grille
        grille = self.jeu.etat_grille()
        for ligne in range(self.jeu.grille.taille):
            for colonne in range(self.jeu.grille.taille):
                self.boutons[ligne][colonne].config(text=grille[ligne][colonne])

    def afficher_message(self, message):
        # Fenêtre pop-up pour afficher le message de fin de partie
        popup = tk.Toplevel(self.root)
        popup.title("Fin de la partie")
        label = tk.Label(popup, text=message, font=("Arial", 14))
        label.pack(pady=10)
        bouton = tk.Button(popup, text="OK", command=lambda: [popup.destroy(), self.root.quit()])
        bouton.pack(pady=10)

    def lancer_interface(self):
        # Lancer la boucle principale de l'interface
        self.root.mainloop()
