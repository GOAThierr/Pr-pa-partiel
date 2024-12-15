class Game:
    def __init__(self):
        # Plateau de jeu : 6 lignes x 7 colonnes
        self.board = [[" " for _ in range(7)] for _ in range(6)]
        self.current_player = "Joueur 1"  # Le joueur X commence
        self.winner = None

    def make_move(self, column):
        """Effectue un mouvement pour le joueur actuel dans la colonne donnée."""
        if self.winner:
            return False  # Le jeu est terminé

        for row in reversed(range(6)):  # On commence par la dernière ligne
            if self.board[row][column] == " ":
                self.board[row][column] = self.current_player
                if self.check_victory(row, column):
                    self.winner = self.current_player
                else:
                    self.current_player = "Joueur 2" if self.current_player == "Joueur 1" else "Joueur 1"
                return True
        return False  # La colonne est pleine

    def check_victory(self, row, column):
        """Vérifie si le joueur actuel a gagné après avoir placé un jeton à (row, column)."""
        directions = [
            [(0, 1), (0, -1)],  # Horizontal
            [(1, 0), (-1, 0)],  # Vertical
            [(1, 1), (-1, -1)],  # Diagonale principale
            [(1, -1), (-1, 1)],  # Diagonale secondaire
        ]

        for direction in directions:
            count = 1  # Le jeton actuel
            for dr, dc in direction:
                r, c = row + dr, column + dc
                while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.current_player:
                    count += 1
                    r, c = r + dr, c + dc
            if count >= 4:
                return True
        return False

    def get_board(self):
        """Retourne l'état actuel du plateau."""
        return self.board

    def reset_game(self):
        """Réinitialise le jeu."""
        self.board = [[" " for _ in range(7)] for _ in range(6)]
        self.current_player = "Joueur 1"
        self.winner = None