from calculator.gui import CalculatorApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()  # Создаем основное окно Tkinter
    app = CalculatorApp(root)  # Передаем его в CalculatorApp
    root.mainloop()  # Запускаем основной цикл приложения
