class Carte:
    def __init__(self, valeur, couleur, visible=False):
        self.valeur = valeur
        self.couleur = couleur
        self.visible = visible
        self.position = (0, 0)  # Par défaut, la position est (0, 0)

    def rendre_visible(self):
        self.visible = True

    def __str__(self):
        return f"{self.valeur}{self.couleur}" if self.visible else "??"
