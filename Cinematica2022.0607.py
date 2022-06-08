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

        '''Explicació dels blocs de codi:
        nom_label: Una etiqueta per explicar al usuari les dades que ha d'introduir.
        nom_entry: Es el requadre d'introducció de dades.
        nom: Les dades convertides a float per poder calcular amb elles.
        self.nom_calc: Variable tipus boolean per defecte False.
        nom_select: Un botó per a seleccionar el que vull calcular.
        Aquest patró es repeteix amb totes les incognites sent identic entre elles, obviament canviant noms'''


        time_label = tk.Label(text="Tiempo en segundos")
        time_label.place(x=20, y=20)
        time_entry = (ttk.Entry(width=5))
        time_entry.place(x=200, y=20)
        time = float(time_entry.get())
        self.time_calc = tk.BooleanVar(self)
        time_select = ttk.Checkbutton(self, text="Tiempo", variable=self.time_calc)
        time_select.place(x=125, y=220)

        space_label = tk.Label(text="Espacio en metros")
        space_label.place(x=20, y=60)
        space_entry = (ttk.Entry(width=5))
        space_entry.place(x=200, y=60)
        space = float(space_entry.get())
        self.space_calc = tk.BooleanVar(self)
        space_select = ttk.Checkbutton(self, text="Espacio", variable=self.space_calc)
        space_select.place(x=200, y=260)

        finalspeed_label = tk.Label(text="Velocidad final en m/s")
        finalspeed_label.place(x=20, y=100)
        finalspeed_entry = (ttk.Entry(width=5))
        finalspeed_entry.place(x=200, y=100)
        finalspeed = float(finalspeed_entry.get())
        self.finalspeed_calc = tk.BooleanVar(self)
        finalspeed_select = ttk.Checkbutton(self, text="Velocidad final", variable=self.finalspeed_calc)
        finalspeed_select.place(x=50, y=260)

        initialspeed_label = tk.Label(text="Velocidad inicial en m/s")
        initialspeed_label.place(x=20, y=140)
        initialspeed_entry = (ttk.Entry(width=5))
        initialspeed_entry.place(x=200, y=140)
        initialspeed = float(initialspeed_entry.get())
        self.initialspeed_calc = tk.BooleanVar(self)
        initialspeed_select = ttk.Checkbutton(self, text="Velocidad inicial", variable=self.initialspeed_calc)
        initialspeed_select.place(x=50, y=300)

        aceleracion_label = tk.Label(text="Aceleración en m/s^2")
        aceleracion_label.place(x=20, y=180)
        aceleracion_entry = (ttk.Entry(width=5))
        aceleracion_entry.place(x=200, y=180)
        aceleracion = float(aceleracion_entry.get())
        self.aceleracion_calc = tk.BooleanVar(self)
        aceleracion_select = ttk.Checkbutton(self, text="Aceleración", variable=self.aceleracion_calc)
        aceleracion_select.place(x=200, y=300)

        # Ací estàn els botons d'eixida del programa i el de calcular.

        Salir = ttk.Button(text="Salir", command=root.destroy)
        Salir.place(x=100, y=380)

        calc = ttk.Button(text="Calcular", command=calcular)
        calc.place(x=100, y=340)
        '''Ací es fan els càlculs, basicament, quan el boolean anterior siga True, en cada incognita es fara el sugüent:
        Comprobar altres variables requerides en la fòrmula
        Realitzar els càlculs
        Una finestra amb el resultat'''
        def __init__(self):
            super(calcular, self).__init__(parent)
            if self.time_calc == True:
                if not space or space == 0:
                    if aceleracion == 0 or not aceleracion and initialspeed == finalspeed:
                        time = space/finalspeed
                        messagebox.showinfo(message=time, title="Tiempo en segundos")
                    elif aceleracion == 0 or not aceleracion and initialspeed != finalspeed:
                        messagebox.showinfo(message="La aceleración no puede ser 0 en un MUA o la velocidad no puede variar en un MU. Erno 5", tittle="Erno 5")
                    else:
                        time2 = ((2*(finalspeed-initialspeed)/aceleracion))
                        messagebox.showinfo(message=time2, title="Tiempo en segundos")
                else:
                    messagebox.showinfo(message="Ha ocurrido un error", title="Erno 1")
            elif self.space_calc == True:
                if aceleracion == 0 or not aceleracion and initialspeed == finalspeed or initialspeed == 0 and finalspeed != 0 or initialspeed != 0 and finalseepd == 0 or not initialspeed or not finalspeed:
                    if initialspeed == 0 or not initialspeed:
                        espacio1 = finalspeed*time
                        messagebox.showinfo(message=espacio1, title="Espacio en metros")
                    elif finalspeed == 0 or not finalspeed:
                        espacio2 = initialspeed*time
                        messagebox.showinfo(message=espacio12, title="Espacio en metros")
                    elif finalspeed == initialspeed:
                        espacio3 = initialspeed*time
                        messagebox.showinfo(message=espacio3, title="Espacio en metros")
                if aceleracion != 0:
                    espacio4 = ((initialspeed*time)+(1/2)*aceleracion*tiempo**2)
                    messagebox.showinfo(message=espacio4, title="Espacio en metros")
                else:
                    messagebox.showinfo(message="Ha ocurrido un error", title="Erno 1")

            elif self.finalspeed.calc == True:
                if aceleracion == 0 or not aceleracion and time > 0:
                    messagebox.showinfo(message=initialspeed, title="Velocidad Final en metros por segundo")
                elif aceleracion != 0 and time > 0:
                    finalspeed1 = (((2*finalspeed)-(2*initialspeed))/time)
                    messagebox.showinfo(message=finalspeed1, title="Velocidad Final en metros por segundo")
                else:
                    messagebox.showinfo(message="Ha ocurrido un error", title="Erno 1")

            elif self.initialspeed.calc == True:
                if space != 0 and aceleracion != 0 and time > 0:
                    velinic = (space + (aceleracion*(time)**2)/2)/time
                    messagebox.showinfo(message=velinic, title="Velocidad inicial en metros por segundo")
                elif finalspeed != 0 and space == 0 or not space:
                    velinic2 = (aceleracion * time) - finalspeed
                    messagebox.showinfo(message=velinic2, title="Velocidad inicial en metros por segundo")
                else:
                    messagebox.showinfo(message="Ha ocurrido un error", title="Erno 1")

            elif self.aceleracion.calc == True:
                if space != 0 and initialspeed != 0 and time > 0:
                    acc = (2 * space - (2 * initialspeed * time)/(time)**2)
                    messagebox.showinfo(message=acc, title="Aceleración en metros por segundo ^2")
                if finalspeed != 0 and initialspeed != 0 and time > 0:
                    acc2 = ((finalspeed - initialspeed)/ time)
                    messagebox.showinfo(message=acc2, title="Aceleración en metros por segundo ^2")
                else:
                    messagebox.showinfo(message="Ha ocurrido un error", title="Erno 1")
            else:
                messagebox.showinfo(message="Ha ocurrido un error", title="Erno 1")
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculadora de operaciones de física")
    root.geometry("400x300")
    main = Cinematica(root)
    main.pack(fill="both", expand=True)
    root.mainloop()
