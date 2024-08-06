import tkinter as tk
from tkinter import ttk
import sympy as sp

def resolver_sistema_dos_incognitas(ecuacion1, ecuacion2):
    x, y = sp.symbols('x y')
    eq1 = sp.Eq(*map(sp.sympify, ecuacion1.split('=')))
    eq2 = sp.Eq(*map(sp.sympify, ecuacion2.split('=')))

    solucion = sp.solve((eq1, eq2), (x, y))
    return solucion

def resolver_sistema_tres_incognitas(ecuacion1, ecuacion2, ecuacion3):
    x, y, z = sp.symbols('x y z')
    eq1 = sp.Eq(*map(sp.sympify, ecuacion1.split('=')))
    eq2 = sp.Eq(*map(sp.sympify, ecuacion2.split('=')))
    eq3 = sp.Eq(*map(sp.sympify, ecuacion3.split('=')))

    solucion = sp.solve((eq1, eq2, eq3), (x, y, z))
    return solucion

def calcular_integrales(funcion, variable):
    var = sp.symbols(variable)
    f = sp.sympify(funcion)
    integral = sp.integrate(f, var)
    return integral

def actualizar_interfaz():
    tipo = tipo_var.get()
    if tipo == "Dos incógnitas":
        ecuacion1_label.config(text="Ecuación 1:")
        ecuacion2_label.grid()
        ecuacion2_entry.grid()
        ecuacion3_label.grid_remove()
        ecuacion3_entry.grid_remove()
        variable_frame.grid_remove()
        metodo_frame.grid()
    elif tipo == "Tres incógnitas":
        ecuacion1_label.config(text="Ecuación 1:")
        ecuacion2_label.grid()
        ecuacion2_entry.grid()
        ecuacion3_label.grid()
        ecuacion3_entry.grid()
        variable_frame.grid_remove()
        metodo_frame.grid_remove()
    elif tipo == "Integrales":
        ecuacion1_label.config(text="Función:")
        ecuacion2_label.grid_remove()
        ecuacion2_entry.grid_remove()
        ecuacion3_label.grid_remove()
        ecuacion3_entry.grid_remove()
        variable_frame.grid()

def ejecutar():
    tipo = tipo_var.get()
    resultado = ""

    if tipo == "Dos incógnitas":
        eq1 = ecuacion1_entry.get()
        eq2 = ecuacion2_entry.get()
        resultado = resolver_sistema_dos_incognitas(eq1, eq2)
    elif tipo == "Tres incógnitas":
        eq1 = ecuacion1_entry.get()
        eq2 = ecuacion2_entry.get()
        eq3 = ecuacion3_entry.get()
        resultado = resolver_sistema_tres_incognitas(eq1, eq2, eq3)
    elif tipo == "Integrales":
        funcion = ecuacion1_entry.get()
        variable = variable_entry.get()
        resultado = calcular_integrales(funcion, variable)

    resultado_label.config(text=f"Resultado: {resultado}")

# Configuración de la interfaz
root = tk.Tk()
root.title("Resolución de Ecuaciones e Integrales")

tipo_var = tk.StringVar(value="Dos incógnitas")

ttk.Label(root, text="Selecciona qué resolver:").grid(column=0, row=0, pady=5)

tipo_frame = ttk.Frame(root)
tipo_frame.grid(column=0, row=1, pady=5)

ttk.Radiobutton(tipo_frame, text="Dos incógnitas", variable=tipo_var, value="Dos incógnitas", command=actualizar_interfaz).pack(side="left")
ttk.Radiobutton(tipo_frame, text="Tres incógnitas", variable=tipo_var, value="Tres incógnitas", command=actualizar_interfaz).pack(side="left")
ttk.Radiobutton(tipo_frame, text="Integrales", variable=tipo_var, value="Integrales", command=actualizar_interfaz).pack(side="left")

metodo_frame = ttk.Frame(root)
metodo_frame.grid(column=0, row=2, pady=5)

# El marco del método ya no se usa, así que eliminamos la parte de los botones de método.

ecuacion1_label = ttk.Label(root, text="Ecuación 1:")
ecuacion1_label.grid(column=0, row=3, pady=5)
ecuacion1_entry = ttk.Entry(root, width=40)
ecuacion1_entry.grid(column=0, row=4, pady=5)

ecuacion2_label = ttk.Label(root, text="Ecuación 2:")
ecuacion2_label.grid(column=0, row=5, pady=5)
ecuacion2_entry = ttk.Entry(root, width=40)
ecuacion2_entry.grid(column=0, row=6, pady=5)

ecuacion3_label = ttk.Label(root, text="Ecuación 3:")
ecuacion3_label.grid(column=0, row=7, pady=5)
ecuacion3_entry = ttk.Entry(root, width=40)
ecuacion3_entry.grid(column=0, row=8, pady=5)

variable_frame = ttk.Frame(root)
variable_frame.grid(column=0, row=9, pady=5)

ttk.Label(variable_frame, text="Variable (para integrales):").pack(side="left")
variable_entry = ttk.Entry(variable_frame, width=10)
variable_entry.pack(side="left")

ttk.Button(root, text="Calcular", command=ejecutar).grid(column=0, row=10, pady=10)

resultado_label = ttk.Label(root, text="Resultado: ")
resultado_label.grid(column=0, row=11, pady=5)

actualizar_interfaz()
root.mainloop()
