class Quoridor:
    def __init__(self):
        self.board_size = 9
        self.players = ['P1', 'P2']
        self.current_player = 0
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.player_positions = {'P1': (0, self.board_size // 2), 'P2': (self.board_size - 1, self.board_size // 2)}
        self.wall_h = [[' ' for _ in range(self.board_size - 1)] for _ in range(self.board_size)]
        self.wall_v = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size - 1)]

    def print_board(self):
        for row in range(self.board_size):
            print(" ---" * self.board_size)
            for col in range(self.board_size):
                print("| " + self.board[row][col], end=" ")
            print("|")
        print(" ---" * self.board_size)

    def place_wall_h(self, row, col):
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size - 1:
            return False
        if self.wall_h[row][col] != ' ':
            return False
        self.wall_h[row][col] = '-'
        return True

    def place_wall_v(self, row, col):
        if row < 0 or row >= self.board_size - 1 or col < 0 or col >= self.board_size:
            return False
        if self.wall_v[row][col] != ' ':
            return False
        self.wall_v[row][col] = '|'
        return True

    def move_player(self, row, col):
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False
        if self.board[row][col] != ' ':
            return False
        player_row, player_col = self.player_positions[self.players[self.current_player]]
        if abs(row - player_row) + abs(col - player_col) != 1:
            return False
        self.board[player_row][player_col] = ' '
        self.board[row][col] = self.players[self.current_player]
        self.player_positions[self.players[self.current_player]] = (row, col)
        return True

    def check_win(self):
        if self.player_positions['P1'][0] == self.board_size - 1:
            return 'P1'
        if self.player_positions['P2'][0] == 0:
            return 'P2'
        return None

    def play(self):
        while True:
            self.print_board()
            print(f"Turn: {self.players[self.current_player]}")
            move_type = input("Enter 'M' for move or 'W' for wall: ")
            if move_type.upper() == 'M':
                row = int(input("Enter the row number: "))
                col = int(input("Enter the column number: "))
                if self.move_player(row, col):
                    winner = self.check_win()
                    if winner:
                        self.print_board()
                        print(f"{winner} wins!")
                        break
                    self.current_player = 1 - self.current_player
                else:
                    print("Invalid move. Try again.")
            elif move_type.upper() == 'W':
                wall_type = input("Enter 'H' for horizontal wall or 'V' for vertical wall: ")
                row = int(input("Enter the row number: "))
                col = int(input("Enter the column number: "))
                if wall_type.upper() == 'H':
                    if self.place_wall_h(row, col):
                        self.current_player = 1 - self.current_player
                    else:
                        print("Invalid wall placement. Try again.")
                elif wall_type.upper() == 'V':
                    if self.place_wall_v(row, col):
                        self.current_player = 1 - self.current_player
                    else:
                        print("Invalid wall placement. Try again.")
                else:
                    print("Invalid wall type. Try again.")
            else:
                print("Invalid move type. Try again.")


# Esempio di utilizzo:
game = Quoridor()
game.play()
