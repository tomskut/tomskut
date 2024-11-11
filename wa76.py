from tkinter import *

def buttonclick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonclear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    try:
        # Replace unary minus with special character temporarily
        processed_expr = operator
        # Handle unary minus at the start of expression
        if processed_expr.startswith('-'):
            processed_expr = '§' + processed_expr[1:]
        
        # Handle unary minus after operators
        for op in ['+', '-', 'x', '/', '(']:
            processed_expr = processed_expr.replace(op + '-', op + '§')
        
        # Replace commas with dots for calculation
        calc_expr = processed_expr.replace(',', '.')
        
        # Handle percentage calculations
        while '%' in calc_expr:
            idx = calc_expr.index('%')
            start_idx = idx - 1
            while start_idx >= 0 and (calc_expr[start_idx].isdigit() or calc_expr[start_idx] == '.'):
                start_idx -= 1
            start_idx += 1
            num = float(calc_expr[start_idx:idx])
            decimal = num / 100
            calc_expr = calc_expr[:start_idx] + str(decimal) + calc_expr[idx + 1:]
        
        # Replace operators and restore unary minus
        calc_expr = calc_expr.replace('x', '*').replace('^', '**').replace('§', '-')
        
        result = eval(calc_expr)
        formatted_result = str(result).replace('.', ',')
        input_value.set(formatted_result)
        operator = formatted_result
    except Exception as e:
        input_value.set("Error")
        operator = ""

def buttonDelete():
    global operator
    if operator:   
        operator = operator[:-1]   
        input_value.set(operator)

def buttonComma():
    global operator
    if operator and operator[-1].isdigit():
        last_operator_index = max((operator.rfind(x) for x in '+-x/^'), default=-1)
        current_number = operator[last_operator_index + 1:]
        if ',' not in current_number:
            operator = operator + ','
            input_value.set(operator)

def buttonPercentage():
    global operator
    operator = operator + '%'
    input_value.set(operator)

def buttonDivide():
    global operator
    operator = operator + '/'
    input_value.set(operator)

def buttonPower():
    global operator
    operator = operator + '^'
    input_value.set(operator)

def buttonMinus():
    global operator
    # Jika operator kosong atau karakter terakhir adalah operator, gunakan minus (negatif)
    if not operator or operator[-1] in '+-x/^(':
        operator = operator + '-'
    else:
        # Jika tidak, gunakan pengurangan
        operator = operator + '-'
    input_value.set(operator)

def buttonSubtract():
    global operator
    # Selalu menggunakan pengurangan
    operator = operator + '-'
    input_value.set(operator)

main = Tk()
main.title("Calculator")
operator = ""
input_value = StringVar()

display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertborderwidth=4,
                    bg="Grey", justify=RIGHT)
display_text.grid(columnspan=5, sticky="nsew")

button_properties = {
    'padx': 20,
    'bd': 8,
    'fg': "black",
    'font': ("arial", 20, "bold"),
}

# Row 1
Button(main, **button_properties, text="7", command=lambda: buttonclick(7)).grid(row=2, column=0, sticky="nsew")
Button(main, **button_properties, text="8", command=lambda: buttonclick(8)).grid(row=2, column=1, sticky="nsew")
Button(main, **button_properties, text="9", command=lambda: buttonclick(9)).grid(row=2, column=2, sticky="nsew")
Button(main, **button_properties, text="+", command=lambda: buttonclick("+")).grid(row=4, column=3, sticky="nsew")
Button(main, **button_properties, text="^", command=buttonPower).grid(row=2, column=4, sticky="nsew")

# Row 2
Button(main, **button_properties, text="4", command=lambda: buttonclick(4)).grid(row=3, column=0, sticky="nsew")
Button(main, **button_properties, text="5", command=lambda: buttonclick(5)).grid(row=3, column=1, sticky="nsew")
Button(main, **button_properties, text="6", command=lambda: buttonclick(6)).grid(row=3, column=2, sticky="nsew")
Button(main, **button_properties, text="−", command=buttonSubtract).grid(row=3, column=3, sticky="nsew")  # Tombol pengurangan
Button(main, **button_properties, text="(", command=lambda: buttonclick("(")).grid(row=3, column=4, sticky="nsew")
Button(main, **button_properties, text=")", command=lambda: buttonclick(")")).grid(row=4, column=4, sticky="nsew")

# Row 3
Button(main, **button_properties, text="1", command=lambda: buttonclick(1)).grid(row=4, column=0, sticky="nsew")
Button(main, **button_properties, text="2", command=lambda: buttonclick(2)).grid(row=4, column=1, sticky="nsew")
Button(main, **button_properties, text="3", command=lambda: buttonclick(3)).grid(row=4, column=2, sticky="nsew")
Button(main, **button_properties, text="x", command=lambda: buttonclick("x")).grid(row=2, column=3, sticky="nsew")

# Row 4
Button(main, **button_properties, text="00", command=lambda: buttonclick(00)).grid(row=5, column=0, sticky="nsew")
Button(main, **button_properties, text="0", command=lambda: buttonclick(0)).grid(row=5, column=1, sticky="nsew")
Button(main, **button_properties, text="C", command=buttonclear).grid(row=1, column=0, sticky="nsew")
Button(main, **button_properties, text="=", command=buttonEqual).grid(row=5, column=3, sticky="nsew")
Button(main, **button_properties, text="⌫", command=buttonDelete).grid(row=1, column=2, sticky="nsew")

# Tombol minus (negatif)
Button(main, **button_properties, text="±", command=buttonMinus).grid(row=1, column=4, sticky="nsew")

Button(main, **button_properties, text=",", command=buttonComma).grid(row=5, column=2, sticky="nsew")
Button(main, **button_properties, text="%", command=buttonPercentage).grid(row=1, column=1, sticky="nsew")
Button(main, **button_properties, text="÷", command=buttonDivide).grid(row=1, column=3, sticky="nsew")

main.mainloop()