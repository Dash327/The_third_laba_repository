import tkinter as tk
from tkinter import simpledialog, messagebox
from typing import TYPE_CHECKING


class MenuBar:
    def __init__(self, root, game: control_unit):
        self.root = root
        self.game = game
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Игра", menu=game_menu)
        game_menu.add_command(label="Новая игра", command=self.game.reset_game)
        game_menu.add_command(label="Размер поля...", command=self.set_board_size)
        game_menu.add_separator()
        game_menu.add_command(label="Выход", command=self.safe_exit)

    def set_board_size(self):
        try:
            size_str = simpledialog.askstring(
                "Размер поля",
                f"Введите размер доски (3–6):\nТекущий: {self.game.size}×{self.game.size}",
                parent=self.root,
            )
            if size_str is None:
                return
            size = int(size_str.strip())
            if 3 <= size <= 6:
                self.game.size = size
                self.game.reset_game()
            else:
                messagebox.showwarning("Ошибка", "Размер должен быть от 3 до 6.")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неизвестная ошибка: {e}")

    def safe_exit(self):
        try:
            if messagebox.askyesno("Выход", "Вы действительно хотите выйти?"):
                self.root.destroy()
        except Exception as e:
            print(f"[INFO] Окно уже закрыто: {e}")
            self.root.quit()
