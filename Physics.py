# I'm going to import the libraries
import tkinter as tk
from tkinter import ttk, messagebox


# I'm creating the GUI

class Calculadora(tk.Frame):
    def __init__(self, parent):
        def cinematica():
           exec(open("Cinematica.py").read())
           
        def dinamica():
           exec(open("Dinamica.py").read())

        def campos():
           exec(open("Campos.py").read())

        def movimiento_armonico_simple():
           exec(open("MAS.py").read())

        super(Calculadora, self).__init__(parent)
        # tk.geometry("200x200")
        self.label = tk.Label(self, text="Calculadora de operaciones de física")
        self.label.pack(padx=20, pady=20)

        cinematica = ttk.Button(text="Cinemática", command=cinematica)
        cinematica.place(x=30, y=50)

        dinamica = ttk.Button(text="Dinámica", command=dinamica)
        dinamica.place(x=30, y=100)

        campos = ttk.Button(text="Campos", command=campos)
        campos.place(x=130, y=50)

        movimiento_armonico_simple = ttk.Button(text="Movimiento Armónico simple", command=movimiento_armonico_simple)
        movimiento_armonico_simple.place(x=130, y=100)

        salir = ttk.Button(text="Salir", command=root.destroy)
        salir.place(x=100, y=150)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora de operaciones de física")
    root.geometry("400x300")
    main = Calculadora(root)
    main.pack(fill="both", expand=True)
    root.mainloop()
