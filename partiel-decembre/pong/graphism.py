import tkinter as tk

class Graphism:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Pong")
        
        self.width = width
        self.height = height
        
        # Création du canevas où le jeu sera affiché
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

    def draw_rectangle(self, x1, y1, x2, y2, color):
        """ Dessiner un rectangle (raquette ou balle) """
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def draw_oval(self, x1, y1, x2, y2, color):
        """ Dessiner une balle """
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def update(self):
        """ Met à jour l'affichage du canevas """
        self.canvas.update()

    def clear(self):
        """ Efface tout l'affichage du canevas """
        self.canvas.delete("all")

    def mainloop(self):
        """ Démarre la boucle principale de Tkinter """
        self.root.mainloop()

    def bind_key(self, key, func):
        """ Lier une touche à une fonction """
        self.root.bind(key, func)
