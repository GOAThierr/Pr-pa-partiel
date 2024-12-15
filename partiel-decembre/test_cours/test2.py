
import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Grande fenêtre")
fenetre.geometry("800x600")  # Taille raisonnable (800px x 600px)

# Ajout d'un label pour afficher un texte
label = tk.Label(fenetre, text="C'est une grande fenêtre !", font=("Arial", 15))
label.pack(pady=50)
ButtonLeave = tk.Button(fenetre, text="Quitter", font=("Arial", 15), command=fenetre.destroy)
ButtonLeave.pack(side= tk.BOTTOM, pady=20)
# Lancement de la boucle principale
fenetre.mainloop()
