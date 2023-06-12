from tkinter import *

class GUI:
    ventana = Tk()
    ventana.title("Círculo")

    canvas_width = 400
    canvas_height = 400
    canvas = Canvas(ventana, width=canvas_width, height=canvas_height)
    canvas.pack()

    color = "red"
    pos_x = canvas_width // 2
    print(pos_x)
    pos_y = canvas_height // 2
    radius = 50

    canvas.create_oval(pos_x - radius, pos_y - radius, pos_x + radius, pos_y + radius, fill=color)

    texto = "Hola"
    canvas.create_text(pos_x, pos_y, text=texto, fill="white")
    

    color = "red"
    pos_x2 = 80
    pos_y2 = 80
    radius = 50

    canvas.create_oval(pos_x2 - radius, pos_y2 - radius, pos_x2 + radius, pos_y2 + radius, fill=color)
    texto = "Adios"
    canvas.create_text(pos_x2, pos_y2, text=texto, fill="white")
    canvas.create_line(200, 200, 80, 80)


    ventana.mainloop()


