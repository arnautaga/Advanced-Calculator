import tkinter as tk
import math
from tkinter import ttk, messagebox


class Cinematica(tk.Frame):
    def __init__(self, parent, calcular):

        super().__init__()
        time_label = tk.Label(text="Tiempo en segundos")
        time_label.place(x=20, y=20)
        time = (ttk.Entry(width=5))
        time.place(x=200, y=20)
        self.time_calc = tk.BooleanVar(self)
        time_select = ttk.Checkbutton(self, text="Tiempo", variable=self.time_calc)
        time_select.place(x=125, y=220)
        if self.time_calc == True:
            messagebox.showinfo(text="se ha activado el Boolean")

        space_label = tk.Label(text="Espacio en metros")
        space_label.place(x=20, y=60)
        space = (ttk.Entry(width=5))
        space.place(x=200, y=60)
        self.space_calc = tk.BooleanVar(self)
        space_select = ttk.Checkbutton(self, text="Espacio", variable=self.space_calc)
        space_select.place(x=200, y=260)

        finalspeed_label = tk.Label(text="Velocidad final en m/s")
        finalspeed_label.place(x=20, y=100)
        finalspeed = (ttk.Entry(width=5))
        finalspeed.place(x=200, y=100)
        self.finalspeed_calc = tk.BooleanVar(self)
        finalspeed_select = ttk.Checkbutton(self, text="Velocidad final", variable=self.finalspeed_calc)
        finalspeed_select.place(x=50, y=260)

        initialspeed_label = tk.Label(text="Velocidad inicial en m/s")
        initialspeed_label.place(x=20, y=140)
        initialspeed = (ttk.Entry(width=5))
        initialspeed.place(x=200, y=140)
        self.initialspeed_calc = tk.BooleanVar(self)
        initialspeed_select = ttk.Checkbutton(self, text="Velocidad inicial", variable=self.initialspeed_calc)
        initialspeed_select.place(x=50, y=300)

        aceleracion_label = tk.Label(text="Aceleración en m/s^2")
        aceleracion_label.place(x=20, y=180)
        aceleracion = (ttk.Entry(width=5))
        aceleracion.place(x=200, y=180)
        self.aceleracion_calc = tk.BooleanVar(self)
        aceleracion_select = ttk.Checkbutton(self, text="Aceleración", variable=self.aceleracion_calc)
        aceleracion_select.place(x=200, y=300)

        Salir = ttk.Button(text="Salir", command=root.destroy)
        Salir.place(x=100, y=380)

        calc = ttk.Button(text="Salir", command=calcular)
        calc.place(x=100, y=340)

        def calcular():
            if self.time_calc == True:
                # Test





if __name__ == "__main__":

    root = tk.Tk()
    root.title("Calculadora de operaciones de física")
    root.geometry("400x300")
    main = Cinematica(root)
    main.pack(fill="both", expand=True)
    root.mainloop()
