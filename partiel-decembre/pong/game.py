import time
from paddle import Paddle
from graphism import Graphism
import tkinter as tk

class Game:
    def __init__(self):
        # Paramètres du jeu
        self.width = 800
        self.height = 600
        self.graphism = Graphism(self.width, self.height)

        # Création des raquettes
        self.left_paddle = Paddle(50, self.height // 2 - 50, 10, 100, 20)
        self.right_paddle = Paddle(self.width - 60, self.height // 2 - 50, 10, 100, 20)

        # Création de la balle
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_radius = 10
        self.ball_speed_x = 5
        self.ball_speed_y = 5

        # Variables de score
        self.left_score = 0
        self.right_score = 0

        # Lier les touches
        self.graphism.bind_key('<KeyPress-Up>', self.move_right_paddle_up)
        self.graphism.bind_key('<KeyPress-Down>', self.move_right_paddle_down)
        self.graphism.bind_key('<KeyPress-w>', self.move_left_paddle_up)
        self.graphism.bind_key('<KeyPress-s>', self.move_left_paddle_down)

        # Créer une fenêtre de jeu principale
        self.window = tk.Tk()
        self.window.title("Jeu Pong")
        self.window.protocol("WM_DELETE_WINDOW", self.quit_game)

    def move_left_paddle_up(self, event):
        """ Déplacer la raquette gauche vers le haut """
        self.left_paddle.move_up()

    def move_left_paddle_down(self, event):
        """ Déplacer la raquette gauche vers le bas """
        self.left_paddle.move_down()

    def move_right_paddle_up(self, event):
        """ Déplacer la raquette droite vers le haut """
        self.right_paddle.move_up()

    def move_right_paddle_down(self, event):
        """ Déplacer la raquette droite vers le bas """
        self.right_paddle.move_down()

    def move_ball(self):
        """ Déplacer la balle """
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        # Collision avec le plafond et le sol
        if self.ball_y - self.ball_radius <= 0 or self.ball_y + self.ball_radius >= self.height:
            self.ball_speed_y = -self.ball_speed_y

        # Collision avec les raquettes
        if self.left_paddle.get_position()[0] < self.ball_x - self.ball_radius < self.left_paddle.get_position()[2]:
            if self.left_paddle.get_position()[1] < self.ball_y < self.left_paddle.get_position()[3]:
                self.ball_speed_x = -self.ball_speed_x

        if self.right_paddle.get_position()[0] < self.ball_x + self.ball_radius < self.right_paddle.get_position()[2]:
            if self.right_paddle.get_position()[1] < self.ball_y < self.right_paddle.get_position()[3]:
                self.ball_speed_x = -self.ball_speed_x

        # Si la balle sort du terrain
        if self.ball_x - self.ball_radius <= 0:
            self.right_score += 1
            self.reset_ball()

        if self.ball_x + self.ball_radius >= self.width:
            self.left_score += 1
            self.reset_ball()

    def reset_ball(self):
        """ Réinitialise la position de la balle après un point marqué """
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_speed_x = -self.ball_speed_x

    def draw(self):
        """ Dessiner les éléments du jeu (raquettes, balle, score) """
        self.graphism.clear()

        # Dessiner les raquettes
        left_x1, left_y1, left_x2, left_y2 = self.left_paddle.get_position()
        right_x1, right_y1, right_x2, right_y2 = self.right_paddle.get_position()
        self.graphism.draw_rectangle(left_x1, left_y1, left_x2, left_y2, "blue")
        self.graphism.draw_rectangle(right_x1, right_y1, right_x2, right_y2, "red")

        # Dessiner la balle
        self.graphism.draw_oval(self.ball_x - self.ball_radius, self.ball_y - self.ball_radius,
                                self.ball_x + self.ball_radius, self.ball_y + self.ball_radius, "green")

        # Afficher le score
        self.graphism.canvas.create_text(self.width // 4, 30, text=str(self.left_score), font=("Arial", 30), fill="blue")
        self.graphism.canvas.create_text(3 * self.width // 4, 30, text=str(self.right_score), font=("Arial", 30), fill="red")

    def check_victory(self):
        """ Vérifie si un joueur a gagné """
        if self.left_score >= 1:
            self.show_end_screen("Joueur Gauche Gagnant!")
            return True
        elif self.right_score >= 1:
            self.show_end_screen("Joueur Droit Gagnant!")
            return True
        return False

    def show_end_screen(self, winner_text):
        """ Affiche l'écran de fin de jeu avec le message du gagnant """
        self.graphism.canvas.create_rectangle(0, 0, self.width, self.height, fill="black", outline="black", width=0)
        self.graphism.canvas.create_text(self.width // 2, self.height // 3, text=winner_text, font=("Arial", 40), fill="white")
        self.graphism.canvas.create_text(self.width // 2, self.height // 2, text="Appuyez sur 'Rejouer' ou 'Quitter'", font=("Arial", 20), fill="white")
        self.graphism.update()

        # Ajouter les boutons pour rejouer ou quitter
        self.add_end_game_buttons()

    def add_end_game_buttons(self):
        """ Crée les boutons 'Rejouer' et 'Quitter' """
        replay_button = tk.Button(self.window, text="Rejouer", font=("Arial", 20), command=self.reset_game)
        replay_button.pack(pady=10)

        quit_button = tk.Button(self.window, text="Quitter", font=("Arial", 20), command=self.quit_game)
        quit_button.pack(pady=10)

    def reset_game(self):
        """ Réinitialise le jeu pour recommencer """
        self.left_score = 0
        self.right_score = 0
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.graphism.clear()
        self.run()

    def quit_game(self):
        """ Quitte le jeu """
        self.window.quit()

    def run(self):
        """ Boucle du jeu """
        while True:
            # Vérifier la condition de victoire
            if self.check_victory():
                break  # Arrêter la boucle lorsque quelqu'un gagne

            start_time = time.time()  # Pour calculer le temps de la boucle

            self.move_ball()
            self.draw()
            self.graphism.update()

            # Contrôler la vitesse du jeu en ajustant le temps de la boucle
            elapsed_time = time.time() - start_time
            sleep_time = max(0, 0.016 - elapsed_time)  # Pour environ 60 FPS
            time.sleep(sleep_time)

        # Lancer la fenêtre Tkinter après la fin du jeu
        self.window.mainloop()
