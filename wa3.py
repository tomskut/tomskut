import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Variable untuk menyimpan perhitungan sekarang
        self.current = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        # Memory variable
        self.memory = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        display = ttk.Entry(self.root, textvariable=self.display_var, justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Tombol-tombol
        buttons = [
            ('MC', 1, 0), ('MR', 1, 1), ('M+', 1, 2), ('M-', 1, 3),
            ('%', 2, 0), ('CE', 2, 1), ('C', 2, 2), ('⌫', 2, 3),
            ('x²', 3, 0), ('√x', 3, 1), ('÷', 3, 2), ('×', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('-', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('+', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('=', 6, 3, 2),  # span 2 rows
            ('0', 7, 0, 2), ('.', 7, 2)  # 0 spans 2 columns
        ]
        
        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            rowspan = 1
            colspan = 1
            
            if len(button) > 3:
                if len(button) == 4:
                    colspan = button[3]
                    
            btn = ttk.Button(self.root, text=text, command=lambda x=text: self.button_click(x))
            btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=1, pady=1)
            
        # Configure grid
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def button_click(self, value):
        if value == '=':
            try:
                # Mengganti operator
                result = self.current.replace('×', '*').replace('÷', '/')
                result = eval(result)
                self.display_var.set(result)
                self.current = str(result)
            except:
                self.display_var.set("Error")
                self.current = ""
                
        elif value == 'C' or value == 'CE':
            self.current = ""
            self.display_var.set("0")
            
        elif value == '⌫':
            self.current = self.current[:-1]
            self.display_var.set(self.current if self.current else "0")
            
        elif value == 'x²':
            try:
                result = float(self.current) ** 2
                self.current = str(result)
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
                self.current = ""
                
        elif value == '√x':
            try:
                result = float(self.current) ** 0.5
                self.current = str(result)
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
                self.current = ""
                
        elif value == '%':
            try:
                result = float(self.current) / 100
                self.current = str(result)
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
                self.current = ""
                
        # Memory operations
        elif value == 'MC':
            self.memory = 0
        elif value == 'MR':
            self.current = str(self.memory)
            self.display_var.set(self.memory)
        elif value == 'M+':
            try:
                self.memory += float(self.current)
            except:
                pass
        elif value == 'M-':
            try:
                self.memory -= float(self.current)
            except:
                pass
                
        else:
            self.current += value
            self.display_var.set(self.current)

def main():
    root = tk.Tk()
    root.title("Calculator")
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()