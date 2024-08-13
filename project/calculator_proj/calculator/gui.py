import tkinter as tk
from calculator.operations import CalculatorOperations

class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.operations = CalculatorOperations()
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()

        # Entry to show result
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 18), justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons
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
            b = tk.Button(self.root, text=button, width=5, height=2, command=action)
            b.grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == '=':
            expression = self.result_var.get()
            result = self.operations.evaluate(expression)
            self.result_var.set(result)
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)

    def run(self):
        self.root.mainloop()
