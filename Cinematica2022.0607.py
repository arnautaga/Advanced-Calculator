#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# I'm going to import the libraries
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

        calc = ttk.Button(text="Calcular", command=calcular)
        calc.place(x=100, y=340)

        def __init__(self):
            super(calcular, self).__init__(parent)
            if self.time_calc == True:
                if not space or space == 0:
                    if aceleracion == 0 or not aceleracion and initialspeed == finalspeed:
                        time = space/finalspeed
                        messagebox.showinfo(message=time, tittle="Tiempo en segundos")
                    elif aceleracion == 0 or not aceleracion and initialspeed != finalspeed:
                        messagebox.showinfo(message="La aceleración no puede ser 0 en un MUA o la velocidad no puede variar en un MU. Erno 5", tittle="Erno 5")
                    else:
                        time2 = ((2*(finalspeed-initialspeed)/aceleracion))
                        messagebox.showinfo(message=time2, tittle="Tiempo en segundos")

            if self.space_calc == True:
                if aceleracion == 0 or not aceleracion and initialspeed == finalspeed or initialspeed == 0 and finalspeed != 0 or initialspeed != 0 and finalseepd == 0 or not initialspeed or not finalspeed:
                    if initialspeed == 0 or not initialspeed:
                        espacio1 = finalspeed*time
                        messagebox.showinfo(message=espacio1, tittle="Espacio en metros")
                    elif finalspeed == 0 or not finalspeed:
                        espacio2 = initialspeed*time
                        messagebox.showinfo(message=espacio12, tittle="Espacio en metros")
                    elif finalspeed == initialspeed:
                        espacio3 = initialspeed*time
                        messagebox.showinfo(message=espacio3, tittle="Espacio en metros")
                if aceleracion != 0:
                    espacio4 = ((initialspeed*time)+(1/2)*aceleracion*tiempo**2)
                    messagebox.showinfo(message=espacio4, tittle="Espacio en metros")
            if self.finalspeed.calc == True:
                if aceleracion == 0 or not aceleracion and time > 0:
                    messagebox.showinfo(message=initialspeed, tittle="Velocidad Final en metros por segundo")
                elif aceleracion != 0 and time > 0:
                    finalspeed1 = (((2*finalspeed)-(2*initialspeed))/time)
                    messagebox.showinfo(message=finalspeed1, tittle="Velocidad Final en metros por segundo")
                else:
                    messagebox.showinfo(message="Ha ocurrido un error", tittle="Erno 6")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculadora de operaciones de física")
    root.geometry("400x300")
    main = Cinematica(root)
    main.pack(fill="both", expand=True)
    root.mainloop()
