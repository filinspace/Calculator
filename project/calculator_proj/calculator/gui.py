import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(True, True)

        # Настройка сетки для растягивания
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Экран калькулятора
        self.screen = tk.Entry(root, justify='right', font=('Arial', 18), bd=10, insertwidth=2)
        self.screen.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Настройка сетки кнопок
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action)
            btn.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Настройка столбцов и строк для растягивания
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
            self.root.rowconfigure(i + 1, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.screen.get()))
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, result)
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, "Error")
        else:
            current_text = self.screen.get()
            self.screen.delete(0, tk.END)
            self.screen.insert(tk.END, current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
