import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display
        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        button_list = [
            "MC", "MR", "M+", "M-", "MS",
            "%", "CE", "C", "☑",
            "1/x", "x²", "√x", "÷",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ".", "="
        ]

        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=5, height=2, command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

# Create main window and run calculator
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()