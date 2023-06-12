from tkinter import *

def seleccionar_opcion(opcion):
    print("Opción seleccionada:", opcion)

ventana = Tk()
ventana.title("Lista de Opciones")

opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

opcion_seleccionada = StringVar(ventana)
opcion_seleccionada.set(opciones[0])  # Establecer la opción predeterminada

opcion_menu = OptionMenu(ventana, opcion_seleccionada, *opciones, command=seleccionar_opcion)
opcion_menu.pack()

ventana.mainloop()
