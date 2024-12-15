from plateau import Plateau
from graphism import InterfaceGraphique

class Jeu:
    def __init__(self):
        self.plateau = Plateau()

    def lancer(self):
        interface = InterfaceGraphique(self.plateau)
        interface.demarrer()
