import tkinter as tk

class QuoridorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quoridor")
        self.board_size = 9
        self.cell_size = 50
        self.players = ['P1', 'P2']
        self.current_player = 0
        self.board = [[0] * (self.board_size * 2 + 1) for _ in range(self.board_size * 2 + 1)]
        self.walls_h = [[0] * self.board_size for _ in range(self.board_size + 1)]
        self.walls_v = [[0] * (self.board_size + 1) for _ in range(self.board_size)]

        self.canvas = tk.Canvas(self.root, width=self.board_size * self.cell_size * 2, height=self.board_size * self.cell_size * 2)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(self.board_size * 2 + 1):
            for col in range(self.board_size * 2 + 1):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if self.board[row][col] == 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.walls_h[row][col] == 1:
                    x1 = col * self.cell_size
                    y1 = (row + 1) * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + 5
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")

                if self.walls_v[row][col] == 1:
                    x1 = (col + 1) * self.cell_size
                    y1 = row * self.cell_size
                    x2 = x1 + 5
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row*2+1][col*2+1] == 1:
                    x = (col * self.cell_size) + (self.cell_size // 2)
                    y = (row * self.cell_size) + (self.cell_size // 2)
                    self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="blue")

                if self.board[row*2+1][col*2+1] == 2:
                    x = (col * self.cell_size) + (self.cell_size // 2)
                    y = (row * self.cell_size) + (self.cell_size // 2)
                    self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="red")

    def handle_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            if self.board[row*2+1][col*2+1] == 0:
                self.move_player(row, col)
            elif self.current_player == 0:
                self.place_wall(row, col)

    def move_player(self, row, col):
        self.board[row*2+1][col*2+1] = self.current_player + 1
        self.current_player = 1 - self.current_player
        self.draw_board()

    def place_wall(self, row, col):
        if self.current_player == 0:
            if row < self.board_size and self.walls_h[row][col] == 0:
                self.walls_h[row][col] = 1
                self.current_player = 1 - self.current_player
        else:
            if col < self.board_size and self.walls_v[row][col] == 0:
                self.walls_v[row][col] = 1
                self.current_player = 1 - self.current_player

        self.draw_board()

root = tk.Tk()
game = QuoridorGUI(root)
root.mainloop()
