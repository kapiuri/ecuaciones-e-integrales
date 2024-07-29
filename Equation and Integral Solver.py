import tkinter as tk
from tkinter import ttk
import sympy as sp

def solve_two_variable_system(equation1, equation2):
    x, y = sp.symbols('x y')
    eq1 = sp.Eq(*map(sp.sympify, equation1.split('=')))
    eq2 = sp.Eq(*map(sp.sympify, equation2.split('=')))

    solution = sp.solve((eq1, eq2), (x, y))
    return solution

def solve_three_variable_system(equation1, equation2, equation3):
    x, y, z = sp.symbols('x y z')
    eq1 = sp.Eq(*map(sp.sympify, equation1.split('=')))
    eq2 = sp.Eq(*map(sp.sympify, equation2.split('=')))
    eq3 = sp.Eq(*map(sp.sympify, equation3.split('=')))

    solution = sp.solve((eq1, eq2, eq3), (x, y, z))
    return solution

def calculate_integrals(function, variable):
    var = sp.symbols(variable)
    f = sp.sympify(function)
    integral = sp.integrate(f, var)
    return integral

def update_interface():
    type_selection = type_var.get()
    if type_selection == "Two variables":
        equation1_label.config(text="Equation 1:")
        equation2_label.grid()
        equation2_entry.grid()
        equation3_label.grid_remove()
        equation3_entry.grid_remove()
        variable_frame.grid_remove()
        method_frame.grid()
    elif type_selection == "Three variables":
        equation1_label.config(text="Equation 1:")
        equation2_label.grid()
        equation2_entry.grid()
        equation3_label.grid()
        equation3_entry.grid()
        variable_frame.grid_remove()
        method_frame.grid_remove()
    elif type_selection == "Integrals":
        equation1_label.config(text="Function:")
        equation2_label.grid_remove()
        equation2_entry.grid_remove()
        equation3_label.grid_remove()
        equation3_entry.grid_remove()
        variable_frame.grid()

def execute():
    type_selection = type_var.get()
    result = ""

    if type_selection == "Two variables":
        eq1 = equation1_entry.get()
        eq2 = equation2_entry.get()
        result = solve_two_variable_system(eq1, eq2)
    elif type_selection == "Three variables":
        eq1 = equation1_entry.get()
        eq2 = equation2_entry.get()
        eq3 = equation3_entry.get()
        result = solve_three_variable_system(eq1, eq2, eq3)
    elif type_selection == "Integrals":
        function = equation1_entry.get()
        variable = variable_entry.get()
        result = calculate_integrals(function, variable)

    result_label.config(text=f"Result: {result}")

# Interface setup
root = tk.Tk()
root.title("Equation and Integral Solver")

type_var = tk.StringVar(value="Two variables")

ttk.Label(root, text="Select what to solve:").grid(column=0, row=0, pady=5)

type_frame = ttk.Frame(root)
type_frame.grid(column=0, row=1, pady=5)

ttk.Radiobutton(type_frame, text="Two variables", variable=type_var, value="Two variables", command=update_interface).pack(side="left")
ttk.Radiobutton(type_frame, text="Three variables", variable=type_var, value="Three variables", command=update_interface).pack(side="left")
ttk.Radiobutton(type_frame, text="Integrals", variable=type_var, value="Integrals", command=update_interface).pack(side="left")

method_frame = ttk.Frame(root)
method_frame.grid(column=0, row=2, pady=5)

# The method frame is no longer used, so we remove the part of the method buttons.

equation1_label = ttk.Label(root, text="Equation 1:")
equation1_label.grid(column=0, row=3, pady=5)
equation1_entry = ttk.Entry(root, width=40)
equation1_entry.grid(column=0, row=4, pady=5)

equation2_label = ttk.Label(root, text="Equation 2:")
equation2_label.grid(column=0, row=5, pady=5)
equation2_entry = ttk.Entry(root, width=40)
equation2_entry.grid(column=0, row=6, pady=5)

equation3_label = ttk.Label(root, text="Equation 3:")
equation3_label.grid(column=0, row=7, pady=5)
equation3_entry = ttk.Entry(root, width=40)
equation3_entry.grid(column=0, row=8, pady=5)

variable_frame = ttk.Frame(root)
variable_frame.grid(column=0, row=9, pady=5)

ttk.Label(variable_frame, text="Variable (for integrals):").pack(side="left")
variable_entry = ttk.Entry(variable_frame, width=10)
variable_entry.pack(side="left")

ttk.Button(root, text="Calculate", command=execute).grid(column=0, row=10, pady=10)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(column=0, row=11, pady=5)

update_interface()
root.mainloop()
