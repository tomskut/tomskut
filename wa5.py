from tkinter import *

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.current = ""
        self.input_value = StringVar()
        self.setup_ui()

    def press(self, key):
        if key == "=":
            try:
                # Handle percentage calculations
                expr = self.current.replace('x', '*').replace('÷', '/')
                while '%' in expr:
                    i = expr.index('%')
                    start = i - 1
                    while start >= 0 and (expr[start].isdigit() or expr[start] == '.'):
                        start -= 1
                    num = float(expr[start + 1:i])
                    expr = expr[:start + 1] + str(num / 100) + expr[i + 1:]
                result = eval(expr)
                # Format result to avoid long decimal places
                if isinstance(result, float):
                    result = '{:.8f}'.format(result).rstrip('0').rstrip('.')
                self.current = str(result)
            except Exception as e:
                self.current = "Error"
            self.input_value.set(self.current)
        elif key == "C":
            self.current = ""
        elif key == "⌫":
            self.current = self.current[:-1]
        elif key == "%":
            if self.current and self.current[-1].isdigit():
                self.current += "%"
        else:
            # Prevent multiple operators in a row
            if key in ['+', '-', 'x', '÷']:
                if self.current and self.current[-1] not in ['+', '-', 'x', '÷']:
                    self.current += key
            elif key == '.':
                # Check if the last number already has a decimal point
                parts = ''.join(c if c.isdigit() or c == '.' else ' ' for c in self.current).split()
                if not parts or '.' not in parts[-1]:
                    self.current += key
            else:
                self.current += str(key)
        
        self.input_value.set(self.current)

    def setup_ui(self):
        # Configure grid weights to make the calculator expandable
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

        # Display
        Entry(self.window, font=("arial", 20), textvariable=self.input_value, bd=30, 
                bg="lightgrey", justify="right").grid(columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('x', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('00', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
            ('C', 1, 0), ('%', 1, 1), ('⌫', 1, 2), ('÷', 1, 3)
        ]

        btn_props = {
            'font': ('arial', 20), 
            'padx': 20, 
            'pady': 20, 
            'bd': 4, 
            'fg': 'black',
            'bg': 'white'
        }

        for (text, row, col) in buttons:
            # Different color for special buttons
            if text in ['=', 'C', '⌫']:
                btn_props['bg'] = 'lightblue'
            elif text in ['+', '-', 'x', '÷', '%']:
                btn_props['bg'] = 'lightgray'
            else:
                btn_props['bg'] = 'white'
                
            Button(self.window, text=text, command=lambda x=text: self.press(x), 
                   **btn_props).grid(row=row, column=col, sticky="nsew")

        # Set minimum window size
        self.window.minsize(400, 600)

if __name__ == "__main__":
    calc = Calculator()
    calc.window.mainloop()