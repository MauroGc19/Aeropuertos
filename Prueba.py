from tkinter import *


def seleccionar_opcion(opcion):
    print("Opción seleccionada:",opcion)
    GUI.guardar_opcion(GUI,opcion)
    

class GUI:
    def __init__(self):
        self.lista=[]
        self.ventana = Tk()
        self.ventana.title("Círculo")
        self.ventana.geometry("1000x500")

        self.canvas_width = 1000
        self.canvas_height = 400
        self.canvas = Canvas(self.ventana, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.color = "red"
        self.pos_x = self.canvas_width // 2
        self.pos_y = self.canvas_height // 2
        self.texto = "Hola"
        
        self.crear_circulo(self.pos_x, self.pos_y, self.color, self.texto)

        self.button = Button(self.ventana, text="Agregar círculo", command=self.open_form)
        self.button.pack()

        self.ventana.mainloop()
        

    def open_form(self):
        self.form_window = Toplevel(self.ventana)
        self.form_window.title("Agregar círculo")

        self.name_label = Label(self.form_window, text="Nombre:")
        self.name_label.pack()
        self.name_entry = Entry(self.form_window)
        self.name_entry.pack()

        self.color_label = Label(self.form_window, text="Color:")
        self.color_label.pack()
        self.color_entry = Entry(self.form_window)
        self.color_entry.pack()

        self.pos_x_label = Label(self.form_window, text="Posición X:")
        self.pos_x_label.pack()
        self.pos_x_entry = Entry(self.form_window)
        self.pos_x_entry.pack()

        self.pos_y_label = Label(self.form_window, text="Posición Y:")
        self.pos_y_label.pack()
        self.pos_y_entry = Entry(self.form_window)
        self.pos_y_entry.pack()
        
        self.letrero = Label(self.form_window, text="Trayecto")
        self.letrero.pack()
        lista=self.lista_Nombres()
        self.opciones = StringVar(self.form_window)
        self.opciones.set(lista[0])
        self.opcion_menu = OptionMenu(self.form_window, self.opciones, *lista, command=seleccionar_opcion)
        self.opcion_menu.pack()

        submit_button = Button(self.form_window, text="Guardar", command=self.add_circle)
        submit_button.pack()
    def guardar_opcion(self,name):
        self.nombre_opcion=name
        print(self.nombre_opcion)
    def add_circle(self):
        name = self.name_entry.get()
        color = self.color_entry.get()
        pos_y = self.pos_y_entry.get()
        pos_x = self.pos_x_entry.get()
        name_opcion=self.nombre_opcion
        if name == '' or color == '' or pos_x == '' or pos_y == '':
            self.show_error_window("llena los datos faltantes")
        else:
            x=int(self.pos_x_entry.get())
            y=int(self.pos_y_entry.get())
            existe= self.comprobar(x,y)
            if(existe):
                self.crear_circulo(x, y, color, name)
                self.crear_linea(x,y,name_opcion)
                self.form_window.destroy()

    def show_error_window(self, text):
        error_window = Toplevel(self.ventana)
        error_window.title("Error")

        error_label = Label(error_window, text=text)
        error_label.pack()

        ok_button = Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

    def crear_circulo(self, x, y, color, name ):
        self.contenido=[]
        radius = 30
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,fill=color)
        self.canvas.create_text(x, y, text=name, fill="white")
        self.contenido.append(name)
        self.contenido.append(color)
        self.contenido.append(x)
        self.contenido.append(y)
        self.lista.append(self.contenido)
    def crear_linea(self,x,y,name_opcion):
        x2=None
        y2=None
        for lista in self.lista:
            if(lista[0]==name_opcion):
                x2=lista[2]
                y2=lista[3]
        self.canvas.create_line(x,y,x2,y2)
    def comprobar(self,x,y):
        existe= True
        for lista in self.lista:
                tamañox1= lista[2]+30
                tamañox2= lista[2]-30
                tamañoy1= lista[3]+30
                tamañoy2= lista[3]-30
                if (tamañox1>=x and tamañox2<=x or tamañoy1>=y and tamañoy2<=y):
                    self.show_error_window("Este aeropuerto ya existe o choca con otro aeropuerto")
                    existe=False 
        return existe
    def lista_Nombres(self):
        Nombres=[]
        for lista in self.lista:
            Nombres.append(lista[0])
        return Nombres
gui = GUI()
