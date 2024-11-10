import tkinter as tk
from tkinter import messagebox

user_input_font = 'arial 35 bold'
user_output_font = 'arial 15'
keys_font = 'arial 25'

keys_bg_colour = '#000000'
keys_fg_colour = '#FFFFFF'

bd_width = 0

#C:\\Users\\Asus\\OneDrive\\Pictures\\chika.jpg
class Calculator:
    def __init__(self):
        # Creation of Calculator window
        self.window = tk.Tk()
        self.window.geometry("500x690+400-35")
        self.window.resizable(True, True)
        self.window.title("CALCULATOR!")

        # Setting/initialising evaluation of user input to an empty string
        self.result = ""

        # Setting/initialising user's current input to an empty string
        self.equation = ""
        self.display_frame = self.create_display_frame()

        # Setting label spaces for evaluation of and current user's input
        self.result_label, self.equation_label = self.create_display_labels()

        # Keys for digits specified with row and column respectively -> key:(row, column)
        self.digits_positions = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        # Keys for normal operations and stored Unicode character(for Python) for special operations '/' and '*'
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        # Sets weight and row/column configuration for each key in 4 x 5 layout
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        # Binds and returns value of each created box(using '<Return>' binding value) in self.digits_positions list
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits_positions:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        # Binds and returns value of each created box in self.operations list
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        # Initialises special buttons - 'clear', 'equal to', 'ce', 'sqrt' and 'sqr'
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_backspace_button()

    def create_display_labels(self):
        # Creates answer label for display
        result_label = tk.Label(self.display_frame, text=self.result, anchor='e', font=user_output_font,
                                bg=keys_bg_colour, fg=keys_fg_colour)
        result_label.pack(expand=True, fill='both')

        # Creates user input for display
        equation_label = tk.Label(self.display_frame, text=self.equation, anchor='e', font=user_input_font,
                                    bg=keys_bg_colour, fg=keys_fg_colour)
        equation_label.pack(expand=True, fill='both')

        # .pack is used instead of .grid so everything is automatically justified to the center with less specification
        # and the widgets expand.

        return result_label, equation_label

    def create_display_frame(self):
        # Creates display frame for display on main window
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        # Includes user input for display using the self.update_label()
        self.equation += str(value)
        self.update_equation_label()

    def create_digit_buttons(self):
        # Creates and displays digit buttons
        for digit, grid_value in self.digits_positions.items():
            button = tk.Button(self.buttons_frame, text=str(digit), command=lambda x=digit: self.add_to_expression(x),
                                borderwidth=bd_width, font=keys_font, bg=keys_bg_colour, fg=keys_fg_colour)
            button.grid(row=grid_value[0], column=grid_value[1], sticky='nsew')

    def append_operator(self, operator):
        # Adds each operator when clicked on by the user using the update_total_label() function
        self.equation += operator
        self.result += self.equation
        self.equation = ""
        self.update_result_label()
        self.update_equation_label()

    def create_operator_buttons(self):
        # Creates the buttons that will display the operators to the user
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, command=lambda x=operator: self.append_operator(x),
                                borderwidth=bd_width, font=keys_font, bg=keys_bg_colour, fg=keys_fg_colour)
            button.grid(row=i, column=4, sticky='nsew')
            i += 1

    def clear(self):
        # Clear function for when the user wants to clear current operation
        self.equation = ""
        self.result = ""
        self.update_equation_label()
        self.update_result_label()

    def create_clear_button(self):
        # Creates button to clear and appends the operation
        button = tk.Button(self.buttons_frame, text="C", command=self.clear, borderwidth=bd_width, font=keys_font,
                            bg=keys_bg_colour, fg=keys_fg_colour)
        button.grid(row=0, column=1, sticky='nsew')

    def backspace(self):
        self.equation = self.equation if not self.equation else self.equation[
                                                                :-1]
        self.update_equation_label()

    def create_backspace_button(self):
        # Creates backspace button
        button = tk.Button(self.buttons_frame, text="CE", command=self.backspace, borderwidth=bd_width, font=keys_font,
                            bg=keys_bg_colour, fg=keys_fg_colour)
        button.grid(row=4, column=4, sticky='nsew')

    def square(self):
        try:
            self.equation = str(abs(eval(f"{self.equation}**2")))
        except Exception:
            self.equation = messagebox.showerror("Error", "Invalid input")
            Calculator.clear(self)
        finally:
            self.update_equation_label()

    def create_square_button(self):
        # \u00b2 being the Unicode character in Python for square sign
        button = tk.Button(self.buttons_frame, text="x\u00b2", borderwidth=bd_width, command=self.square,
                            font=keys_font,
                            bg=keys_bg_colour, fg=keys_fg_colour)
        button.grid(row=0, column=2, sticky='nsew')

    def sqrt(self):
        try:
            if int(self.equation) < 0:
                self.equation = messagebox.showerror("Error", "Invalid input")
                Calculator.clear(self)
            else:
                self.equation = str(eval(f"{self.equation}**0.5"))
        except Exception:
            self.equation = messagebox.showerror("Error", "Invalid input")
            Calculator.clear(self)
        finally:
            self.update_equation_label()

    def create_sqrt_button(self):
        # \u221a being the Unicode character in Python for square root sign
        button = tk.Button(self.buttons_frame, text="\u221ax", borderwidth=bd_width, command=self.sqrt, font=keys_font,
                            bg=keys_bg_colour, fg=keys_fg_colour)
        button.grid(row=0, column=3, sticky='nsew')

    def evaluate(self):
        # Creates evaluation/equals-to function for user input operation
        self.result += self.equation[:11]
        self.update_result_label()

        # Returns error if evaluation to user's input is mathematically 'impossible'
        try:
            self.equation = str(eval(self.result))

            # self.total_expression = ""
        except Exception:
            self.equation = messagebox.showerror("Error", "Invalid input")
            Calculator.clear(self)
        finally:
            self.update_equation_label()

    def create_equals_button(self):
        # Creates button to evaluate/equals-to and appends the operation
        button = tk.Button(self.buttons_frame, text="=", command=self.evaluate, borderwidth=bd_width, font=keys_font,
                            bg=keys_bg_colour, fg=keys_fg_colour)
        button.grid(row=4, column=3, sticky='nsew')

    def create_buttons_frame(self):
        # Creates frame that will take in all buttons and justify to the center/fill in the window using .pack
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_result_label(self):
        # Returns supposed operator and its symbol as an expression in the expression display label
        # when called in the calculator
        expression = self.result
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.result_label.config(text=expression)

    def update_equation_label(self):
        # Configures set expression to label in a maximum length of 11 characters.
        self.equation_label.config(text=self.equation[:11])

    def run(self):
        self.window.mainloop()


calc = Calculator()
calc.run()