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
        self.ventana = Tk() # ventana principal
        self.ventana.title("Círculo")
        self.ventana.geometry("1000x500")# tamaño de la ventana

        self.canvas_width = 1000
        self.canvas_height = 400
        self.canvas = Canvas(self.ventana, width=self.canvas_width, height=self.canvas_height)# lugar donde se muestran los circulos y las lineas
        self.canvas.pack(fill=BOTH, expand=True)
        scrollbar = Scrollbar(self.ventana, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=scrollbar.set)
        #aero puerto inicial
        color = "blue"
        pos_x = self.canvas_width // 2
        pos_y = self.canvas_height // 2
        texto = "Hola"
        
        self.crear_circulo(pos_x, pos_y, color, texto)

        CrearA= Button(self.ventana, text="Agregar Aeropuerto", command=self.open_form)
        CrearA.pack(side=LEFT, padx=5)
        BuscarA= Button(self.ventana, text="Buscar Aeropuerto", command=self.Buscar_Aero)
        BuscarA.pack(side=LEFT, padx=5)
        EliminarA= Button(self.ventana, text="Eliminar Aeropuerto")
        EliminarA.pack(side=LEFT, padx=5)
        CrearT= Button(self.ventana, text="Crear Trayecto", command=self.open_trayecto)
        CrearT.pack(side=LEFT, padx=5)
        BuscarT= Button(self.ventana, text="Buscar Trayecto", command=self.Buscar_Trayecto)
        BuscarT.pack(side=LEFT, padx=5)
        EliminarT= Button(self.ventana, text="Eliminar Trayecto")
        EliminarT.pack(side=LEFT, padx=5)


        self.ventana.mainloop()
        
    def guardar_origen(self,name):#guarda el origen del trayecto seleccionado en open_trayecto
        self.nombre_origen=name
    def guardar_destino(self,name):#guarda el destino del trayecto selleccionado en open_trayecto
        self.nombre_destino=name
        
    def guardar_color(self,color):#guarda el color del aeropuerto seleccionado en open_trayecto
        self.color=color

    def Buscar_Aero(self):
        self.panel = Toplevel(self.ventana)
        self.panel.title("Buscar Aeropuerto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = Label(self.panel, text="Aeropuertos existentes")
        letrero.pack()
        
        opciones = StringVar(self.panel)
        opciones.set("ninguno")
        opcion_menu = OptionMenu(self.panel, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        submit_button = Button(self.panel, text="señalar", command=self.Señalar_Aero)
        submit_button.pack(padx=5)
        submit_button = Button(self.panel, text="cerrar", command=self.cerrar)
        submit_button.pack(padx=5)
    
    def Buscar_Trayecto(self):#Abre una ventada donde se ven las rutas
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        letrero2 = Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")# primera opcion
    
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_destino)# menu de opciones de destino
        opcion_menu.pack()
        
        submit_button = Button(self.formulario, text="Señalar", command=self.Señalar_Trayecto)
        submit_button.pack()
        submit_button = Button(self.formulario, text="Cerrar", command=self.cerrar_trayecto)
        submit_button.pack()
    
    def Señalar_Aero(self):# cambia el color del aeropuerto para asi encontrarlo visualmente
        nombre=self.nombre_origen
        for lista in self.lista:
            if(lista[0]==nombre):
                self.color_original=lista[1]
                lista[1]="red"
                estado= True
                self.cambiar_color(lista, estado)
                letrero = Label(self.panel, text="Posion en x")
                letrero.pack(side=LEFT)
                letrero = Label(self.panel, text=lista[2])
                letrero.pack(side=LEFT)
                letrero = Label(self.panel, text="Pocion en y")
                letrero.pack(side=LEFT)
                letrero = Label(self.panel, text=lista[3])
                letrero.pack(side=LEFT)
    def Señalar_Trayecto(self):# cambia el color de la linea de trayecto para asi identificarla
        origen=self.nombre_origen
        destino=self.nombre_destino
        datos=[]
        Trayectos= self.lista_Nombres_Trayectos()
        direccion=origen+"-"+destino
        for trayecto in Trayectos:
            if(direccion==trayecto):
                estado=True
        if(estado):
            for lista in self.lista:
                    if(lista[0]==origen):
                        datos.append(lista)
                        for lista in self.lista:
                            if(lista[0]==destino):
                                datos.append(lista)
                                estado=False
                                self.cambiar_color(datos,estado)
        else:
            self.show_error_window("El trayecto no existe")
    def cerrar(self):#cierra el panel ademas de volver el aero puerto a su color original
        nombre=self.nombre_origen
        for lista in self.lista:
            if(lista[0]==nombre):
                lista[1]=self.color_original
                estado= True
                self.cambiar_color(lista,estado)
        self.panel.destroy()
    def cerrar_trayecto(self):#cierra el panel ademas de volver el trayecto a su color original
        self.cambiar_color(None,False)
        self.formulario.destroy()
    def cambiar_color(self, listas, Estado):# cambia de color el aeropuerto
        if(Estado):
            radius=30
            x=int(listas[2])
            y=int(listas[3])
            
            self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,fill=listas[1])
            self.canvas.create_text(x, y, text=listas[0], fill="white")
        else:
            if(listas):
                for lista in listas:
                    if(lista[0]==self.nombre_origen):
                        print(lista[0],lista[1], lista[2], lista[3])
                        self.x=lista[2]
                        self.y=lista[3]
                    else:
                        if(lista[0]==self.nombre_destino):
                            self.x2=lista[2]
                            self.y2=lista[3]
                self.canvas.create_line(self.x,self.y,self.x2,self.y2,fill="red")
            else:
                self.canvas.create_line(self.x,self.y,self.x2,self.y2,fill="black")
        
    def open_trayecto(self):# formulario de creacion de trayectos
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        letrero2 = Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")# primera opcion
    
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_destino)# menu de opciones de destino
        opcion_menu.pack()
        
        letrero3= Label(self.formulario, text="Duracion")
        letrero3.pack()
        self.duracion = Entry(self.formulario)# entrada de duracion
        self.duracion.pack()
        
        letrero4= Label(self.formulario, text="Distancia")
        letrero4.pack()
        self.distancia = Entry(self.formulario)# entrada de distancia
        self.distancia.pack()
        
        submit_button = Button(self.formulario, text="crear", command=self.add_trayecto)
        submit_button.pack()
        
    def add_trayecto(self):# es donde se comparan los datos a ver si son correctos
        origen=self.nombre_origen
        destino=self.nombre_destino
        duracion = self.duracion.get()
        distacia = self.duracion.get()
        if(origen==destino):
            self.show_error_window("el origen y destino deben ser diferentes")# abre la ventada de error con el mensaje que tiene dentro
        else:
            self.crear_linea(origen, destino, duracion, distacia)
            self.formulario.destroy()
    
    def open_form(self):# formulario para crear un aero puerto
        self.form_window = Toplevel(self.ventana)
        self.form_window.title("Agregar círculo")

        name_label = Label(self.form_window, text="Nombre:")
        name_label.pack()
        self.name_entry = Entry(self.form_window)#guarda el nombre del aeropuerto
        self.name_entry.pack()

        pos_x_label = Label(self.form_window, text="Posición X:")
        pos_x_label.pack()
        self.pos_x_entry = Entry(self.form_window)#guarda la posicion en x del aeropuerto
        self.pos_x_entry.pack()

        pos_y_label = Label(self.form_window, text="Posición Y:")
        pos_y_label.pack()
        self.pos_y_entry = Entry(self.form_window)#guarda la posicion en y del aeropuerto
        self.pos_y_entry.pack()
        
        color_label = Label(self.form_window, text="Color:")
        color_label.pack()
        Colores=["blue","yellow","orange", "purple","green","grey","black"]# lista de coleres que puede utilizar el usuario
        color = StringVar(self.form_window)
        color.set("ninguno")# primera opcion
        opcion_color = OptionMenu(self.form_window,color, *Colores, command=seleccionar_color )
        opcion_color.pack()

        submit_button = Button(self.form_window, text="Crear", command=self.add_circle)
        submit_button.pack()
        
    def add_circle(self):# conpara los datos seleccionado en open_form para ver si son correctos
        name = self.name_entry.get()
        color = self.color
        pos_y = self.pos_y_entry.get()
        pos_x = self.pos_x_entry.get()
        if name == '' or color == '' or pos_x == '' or pos_y == '':
            self.show_error_window("llena los datos faltantes")# abre una ventada de error si se cumple alguna de las condiciones
        else:
            x=int(self.pos_x_entry.get())
            y=int(self.pos_y_entry.get())
            existe= self.comprobar(x,y, name)#mira que los aero puertos no choquen entre si
            if(existe):
                self.crear_circulo(x, y, color, name)# crea el area que va ocupar los aero puertos
                self.form_window.destroy()

    def show_error_window(self, text):# crea la ventana de error
        error_window = Toplevel(self.ventana)
        error_window.title("Error")

        error_label = Label(error_window, text=text)
        error_label.pack()

        ok_button = Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

    def crear_circulo(self, x, y, color, name ):# crea el area de los aero puertos
        contenido=[]# lista donde se añade la informacion del aero puerto
        radius = 30
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,fill=color)
        self.canvas.create_text(x, y, text=name, fill="white")
        # se añaden los datos del aeropuertoa a la lista contenido
        contenido.append(name)
        contenido.append(color)
        contenido.append(x)
        contenido.append(y)
        # se añade la lista contenido a la lista self.lista donde se guarda la informacion de todos los aviones
        self.lista.append(contenido)
    def crear_linea(self,origen, destino, duracion, distancia):# crea las lineas de trayecto
        trayecto=[]# lista donde se añade la informacion del trayecto
        for lista in self.lista:
            if(lista[0]==origen):
                x=lista[2]
                y=lista[3]
        for lista in self.lista:
            if(lista[0]==destino):
                x2=lista[2]
                y2=lista[3]
        self.canvas.create_line(x,y,x2,y2, fill="black")
        # se añade la informacion del trayecto a la lista trayecto
        trayecto.append(origen)
        trayecto.append(destino)
        trayecto.append(duracion)
        trayecto.append(distancia)
        trayecto.append("black")
        # se añade la lista trayecto a la lista lista_trayecto
        self.lista_trayectos.append(trayecto)
        
    def comprobar(self,x,y,name):# funcion  que devuelve un boolen si la informacion no esta repetida
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
    def lista_Nombres(self):# crea una lista con los nombres de los aero puertos
        Nombres=[]
        for lista in self.lista:
            Nombres.append(lista[0])
        return Nombres
    def lista_Nombres_Trayectos(self):
        Trayectos=[]
        for lista in self.lista_trayectos:
            Trayectos.append(lista[0]+"-"+lista[1])
        return Trayectos
gui = GUI()
