from tkinter import *


def seleccionar_origen(opcion):
    GUI.guardar_origen(GUI,opcion)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
def seleccionar_destino(opcion):
    GUI.guardar_destino(GUI,opcion)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
def seleccionar_color(color):
    GUI.guardar_color(GUI, color)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
    

class GUI:
    def __init__(self):
        self.lista_trayectos=[] #lista donde se guardan los trayectos
        self.lista=[] # lista donde se guardan los aero puertos
        self.ventana = Tk()
        self.ventana.title("Círculo")
        self.ventana.geometry("1000x500")

        self.canvas_width = 1000
        self.canvas_height = 400
        self.canvas = Canvas(self.ventana, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        color = "red"
        pos_x = self.canvas_width // 2
        pos_y = self.canvas_height // 2
        texto = "Hola"
        
        self.crear_circulo(pos_x, pos_y, color, texto)

        self.button = Button(self.ventana, text="Agregar círculo", command=self.open_form)
        self.button.pack()
        self.button = Button(self.ventana, text="Crear Trayecto", command=self.open_trayecto)
        self.button.pack()


        self.ventana.mainloop()
    
    def open_trayecto(self):
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres()
        
        letrero = Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")
        
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)
        opcion_menu.pack()
        
        letrero2 = Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")
        
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_destino)
        opcion_menu.pack()
        
        letrero3= Label(self.formulario, text="Duracion")
        letrero3.pack()
        self.duracion = Entry(self.formulario)
        self.duracion.pack()
        
        letrero4= Label(self.formulario, text="Distancia")
        letrero4.pack()
        self.distancia = Entry(self.formulario)
        self.distancia.pack()
        
        submit_button = Button(self.formulario, text="crear", command=self.add_trayecto)
        submit_button.pack()
        
    def add_trayecto(self):
        origen=self.nombre_origen
        destino=self.nombre_destino
        duracion = self.duracion.get()
        distacia = self.duracion.get()
        if(origen==destino):
            self.show_error_window("el origen ye destino deben ser diferentes")
        else:
            self.crear_linea(origen, destino, duracion, distacia)
            self.formulario.destroy()
    
    def open_form(self):
        self.form_window = Toplevel(self.ventana)
        self.form_window.title("Agregar círculo")

        name_label = Label(self.form_window, text="Nombre:")
        name_label.pack()
        self.name_entry = Entry(self.form_window)
        self.name_entry.pack()

        pos_x_label = Label(self.form_window, text="Posición X:")
        pos_x_label.pack()
        self.pos_x_entry = Entry(self.form_window)
        self.pos_x_entry.pack()

        pos_y_label = Label(self.form_window, text="Posición Y:")
        pos_y_label.pack()
        self.pos_y_entry = Entry(self.form_window)
        self.pos_y_entry.pack()
        
        color_label = Label(self.form_window, text="Color:")
        color_label.pack()
        Colores=["red","blue","yellow","orange", "purple","green","grey","black"]
        color = StringVar(self.form_window)
        color.set("ninguno")
        opcion_color = OptionMenu(self.form_window,color, *Colores, command=seleccionar_color )
        opcion_color.pack()

        submit_button = Button(self.form_window, text="Guardar", command=self.add_circle)
        submit_button.pack()
        
    def guardar_origen(self,name):
        self.nombre_origen=name
    def guardar_destino(self,name):
        self.nombre_destino=name
        
    def guardar_color(self,color):
        self.color=color
        
    def add_circle(self):
        name = self.name_entry.get()
        color = self.color
        pos_y = self.pos_y_entry.get()
        pos_x = self.pos_x_entry.get()
        if name == '' or color == '' or pos_x == '' or pos_y == '':
            self.show_error_window("llena los datos faltantes")
        else:
            x=int(self.pos_x_entry.get())
            y=int(self.pos_y_entry.get())
            existe= self.comprobar(x,y, name)
            if(existe):
                self.crear_circulo(x, y, color, name)
                self.form_window.destroy()

    def show_error_window(self, text):
        error_window = Toplevel(self.ventana)
        error_window.title("Error")

        error_label = Label(error_window, text=text)
        error_label.pack()

        ok_button = Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

    def crear_circulo(self, x, y, color, name ):
        contenido=[]
        radius = 30
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,fill=color)
        self.canvas.create_text(x, y, text=name, fill="white")
        contenido.append(name)
        contenido.append(color)
        contenido.append(x)
        contenido.append(y)
        self.lista.append(contenido)
    def crear_linea(self,origen, destino, duracion, distancia):
        trayecto=[]
        for lista in self.lista:
            if(lista[0]==origen):
                x=lista[2]
                y=lista[3]
        for lista in self.lista:
            if(lista[0]==destino):
                x2=lista[2]
                y2=lista[3]
        self.canvas.create_line(x,y,x2,y2)
        trayecto.append(origen)
        trayecto.append(destino)
        trayecto.append(duracion)
        trayecto.append(distancia)
        self.lista_trayectos.append(trayecto)
        
    def comprobar(self,x,y,name):
        existe= True
        for lista in self.lista:
                tamañox1= lista[2]+30
                tamañox2= lista[2]-30
                tamañoy1= lista[3]+30
                tamañoy2= lista[3]-30
                if (tamañox1>=x and tamañox2<=x or tamañoy1>=y and tamañoy2<=y or name==lista[0]):
                    self.show_error_window("Este aeropuerto ya existe o choca con otro aeropuerto")
                    existe=False 
        return existe
    def lista_Nombres(self):
        Nombres=[]
        for lista in self.lista:
            Nombres.append(lista[0])
        return Nombres
gui = GUI()
