import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def main():
    try:
        root = tk.Tk()
        root.title("Крестики-нолики")
        root.geometry("400x450")
        root.resizable(True, True)

        game = control_unit(root)
        menu = navbar(root, game)

        # Запуск первой игры
        game.reset_game()

        # Обработка закрытия окна
        root.protocol("WM_DELETE_WINDOW", menu.safe_exit)

        root.mainloop()

    except KeyboardInterrupt:
        print("\n[INFO] Программа прервана пользователем.")
    except Exception as e:
        print(f"[CRITICAL] Критическая ошибка: {e}")
        try:
            messagebox.showerror(
                "Критическая ошибка", f"Программа завершилась с ошибкой:\n{e}"
            )
        except:
            pass  # Если окно уже неактивно


if __name__ == "__main__":
    main()
