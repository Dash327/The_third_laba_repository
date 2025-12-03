import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.size = 3
        self.board = []
        self.current_player = "X"
        self.game_over = False

        # --- ЭЛЕМЕНТЫ УПРАВЛЕНИЯ ---
        self.create_status_label()
        self.create_buttons_frame()

    def create_status_label(self):
        """Создаёт строку состояния (кто ходит, результат)."""
        self.status_label = tk.Label(
            self.root, text="Ходит: X", font=("Arial", 16), pady=10
        )
        self.status_label.pack()

    def create_buttons_frame(self):
        """Создаёт контейнер для игрового поля."""
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10, expand=True)

    def update_board_ui(self):
        """Обновляет кнопки игрового поля под текущий размер."""
        # Очистка старых кнопок
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Создание нового поля
        for r in range(self.size):
            for c in range(self.size):
                btn = tk.Button(
                    self.buttons_frame,
                    text="",
                    font=("Arial", 20, "bold"),
                    width=4,
                    height=2,
                    command=lambda r=r, c=c: self.make_move(r, c),
                )
                btn.grid(row=r, column=c, padx=2, pady=2)

    def reset_game(self):
        """Сбрасывает доску и параметры (вызывается при новой игре)."""
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "X"
        self.game_over = False
        self.status_label.config(text="Ходит: X")
        self.update_board_ui()

    def make_move(self, row, col):
        if self.game_over or self.board[row][col] != "":
            return

        try:
            # Выполнить ход
            self.board[row][col] = self.current_player
            btn = self.buttons_frame.grid_slaves(row=row, column=col)[0]
            btn.config(
                text=self.current_player,
                state="disabled",
                disabledforeground="blue" if self.current_player == "X" else "red",
            )

            # Проверка окончания
            if self.check_winner(row, col):
                self.game_over = True
                self.status_label.config(text=f"Победил: {self.current_player}!")
                messagebox.showinfo(
                    "Игра окончена", f"Игрок {self.current_player} победил!"
                )
            elif self.is_board_full():
                self.game_over = True
                self.status_label.config(text="Ничья!")
                messagebox.showinfo("Игра окончена", "Ничья!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Ходит: {self.current_player}")

        except Exception as e:
            messagebox.showerror("Ошибка хода", f"Не удалось выполнить ход:\n{e}")

    def check_winner(self, row, col):
        player = self.board[row][col]
        n = self.size
        # Строка, столбец, диагонали
        win = (
            all(self.board[row][c] == player for c in range(n))
            or all(self.board[r][col] == player for r in range(n))
            or (row == col and all(self.board[i][i] == player for i in range(n)))
            or (
                row + col == n - 1
                and all(self.board[i][n - 1 - i] == player for i in range(n))
            )
        )
        return win

    def is_board_full(self):
        return all(cell != "" for row in self.board for cell in row)
