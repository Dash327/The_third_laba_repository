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
