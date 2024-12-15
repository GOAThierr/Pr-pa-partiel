class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move_up(self):
        """ Déplace la raquette vers le haut """
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        """ Déplace la raquette vers le bas """
        if self.y + self.height < 600:  # Limite à la hauteur du canevas (600 px)
            self.y += self.speed

    def get_position(self):
        """ Retourne les coordonnées actuelles de la raquette """
        return self.x, self.y, self.x + self.width, self.y + self.height
