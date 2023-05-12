"""
Inicialmente se importan todas las librerías requeridas para el funcionamiento de la aplicación. 

"""

#import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk
from model import Crud

""" Se crea una instancia de la clase Tk() para crear la ventana principal de la aplicación. """ 

class Ventana():
    def __init__(self, window):
        self.model=Crud()
        self.ventana = window
    # def ventana_principal(ventana):

        self.ventana.geometry("440x530")
        self.ventana.resizable(0,0) # Se bloquea la modificación del tamaño de la ventana por parte del usuario.
        self.ventana.title("Inventario de Repuestos") #bg='#2e2e2e'

    # Se definen varias variables que serán utilizadas para almacenar la información de los productos que se agregarán a una lista.

        self.var_name = StringVar()
        self.var_categoria = StringVar()
        self.var_cantidad = IntVar()
        self.var_precio = DoubleVar()
        self.var_desc = StringVar()

        """
        Creación de Segmentos, se crean varios objetos Frame que se usarán para organizar los elementos de la interfaz gráfica.

        """

        self.segmento1 = Frame(self.ventana) 
        self.segmento1.grid(row=0, column=0)
        self.segmento1.place(x=20, y=50)
        self.segmento2 = Frame(self.ventana)
        self.segmento2.grid(row=0, column=2)
        self.segmento2.place(x=290, y=0)
        self.segmento3 = Frame(self.ventana)
        self.segmento3.grid(row=1, column=0)
        self.segmento3.place(x=40, y=210)
        self.segmento4 = Frame(self.ventana)
        self.segmento4.grid(row=2, column=0)
        self.segmento4.place(x=20, y=260)
        self.segmento5 = Frame(self.ventana)
        self.segmento5.grid(row=5, column=0)
        self.segmento5.place(x=15, y=280)

        """
        Se crean varios objetos Label, Entry, Combo y Spin que se utilizarán para 

        recopilar información sobre los productos que se agregarán al inventario,

        estos objetos se asociaran a las variables creadas previamente. 

        """


        # ---------------------------- Segmento 1 ----------------------------

        self.name = Label(self.segmento1, text= "Nombre del producto")    # En este caso saco el nombre de la ventana principal y le asigno el nombre del segmento
        self.name.grid(row=0, column=0, sticky=E)                    # sticky permite personalizar la ubicación de los objetos
        self.entry_name = Entry(self.segmento1, textvariable=self.var_name)    # textvariable permite setear el valor de la variable definido en el campo entry 
        self.entry_name.grid(row=0, column=1, sticky=E) 

        self.categoria = Label(self.segmento1, text="Categoría")
        self.categoria.grid(row=1, column=0, sticky=W)
        self.comboCategoria = ttk.Combobox(self.segmento1, textvariable=self.var_categoria) 
        self.comboCategoria = ttk.Combobox(
            state="readonly",
            values=["ACCESORIOS", "AUTOPARTES", "DISTRIBUCION", "ELECTRICO",\
                    "EMBRAGUE", "ENCENDIDO", "FILTROS", "FRENOS", "MOTOR", \
                    "REFRIGERACION", "SUSPENSION", "TRANSMISION"]
        )
        self.comboCategoria.set("ACCESORIOS")
        self.comboCategoria.place(x=141, y=72, width=124)

        self.cantidad = Label(self.segmento1, text="Cantidad")
        self.cantidad.grid(row=2, column=0, sticky=W)
        # Se agrega un SpinBox para evitar errores de tipeo
        self.spin_cantidad = Spinbox(self.segmento1, textvariable=self.var_cantidad, from_=0, to=10000, increment=1, state="readonly", width=18) 
        self.spin_cantidad.grid(row=2, column=1, sticky=W)
        self.spin_cantidad.config(justify="right")

        self.precio = Label(self.segmento1, text="Precio")
        self.precio.grid(row=3, column=0, sticky=W)
        self.entry_precio = Entry(self.segmento1, textvariable=self.var_precio, width=10)
        self.entry_precio.grid(row=3, column=1, sticky=W)

        self.desc = Label(self.segmento1, text="Descripción")
        self.desc.grid(row=4, column=0, sticky=W)
        self.entry_desc = Entry(self.segmento1, textvariable=self.var_desc) 
        self.entry_desc.grid(row=4, column=1, sticky=W)

        # ---------------------------- Segmento 2 ----------------------------

        # Se agrega la imagen

        self.imagen=tk.PhotoImage(file="amortiguadores.png") 
        self.imagen_chica=self.imagen.subsample(6) #Se reduce las dimensiones de la imagen en un (ancho_imagen / 6)
        self.imagen=ttk.Label(self.segmento2, image=self.imagen_chica)
        self.imagen.grid(row=0, column=0, pady=20, sticky=E)


        # ---------------------------- Segmento 3 ----------------------------
        
        """
        Se definen las funciones que se van a invocar desde la vista. 

        """

        def limpiar():
            """ Función que permite limpiar los campos de ingreso"""
            self.var_name.set("")
            self.var_categoria.set("")
            self.var_cantidad.set(0)
            self.var_desc.set("")
            self.var_precio.set(0)

        def funciones_consultar():
            self.model.limpiar_tree(self.tree)
            self.model.consultar(self.comboCategoria.get(), self.tree)    

        def funciones_modificar():
            self.model.validacion(self.var_name.get(), self.var_cantidad.get(), self.var_desc.get())
            self.model.modificar(self.var_name.get(), self.comboCategoria.get(), self.var_cantidad.get(), self.var_desc.get(), self.var_precio.get(), self.tree)
            limpiar()
            self.model.limpiar_tree(self.tree)
            self.model.consultar(self.comboCategoria.get(), self.tree)

        def funciones_agregar():
            self.model.agregar_01(self.var_name.get(), self.comboCategoria.get(), self.var_cantidad.get(), self.var_desc.get(), self.var_precio.get(), self.tree)
            limpiar()

        def funciones_borrar():
            try:
                self.model.borrar(self.tree)        
            except:
                messagebox.showinfo("Información", "Se debe seleccionar un registro") 
            else:
                messagebox.showerror("Repuesto Borrado", "Se ha borrado el registro seleccionado") 

        """
        Se agregan los botones del CRUD

        """

        self.boton_a = Button(self.segmento3, text= "Agregar", command=lambda:funciones_agregar(), width=10, height=1)
        self.boton_a.grid(row= 0, column=0, padx=7, pady=20)
        self.boton_c = Button(self.segmento3, text= "Consultar", command=lambda:funciones_consultar(), width=10, height=1)
        self.boton_c.grid(row= 0, column=1, padx=7, pady=20)
        self.boton_u = Button(self.segmento3, text= "Modificar", command=lambda:funciones_modificar(), width=10, height=1) #, state=DISABLED
        self.boton_u.grid(row= 0, column=2, padx=7, pady=20)
        self.boton_m = Button(self.segmento3, text= "Borrar", command=lambda:funciones_borrar(), width=10, height=1) #, state=DISABLED
        self.boton_m.grid(row= 0, column=3, padx=7, pady=20)

        # ---------------------------- Segmento 4 ----------------------------

        ttk.Separator(
            master=self.segmento4,
            orient=HORIZONTAL,
            style='blue.TSeparator',
            class_= ttk.Separator,
            takefocus= 1,
            cursor='plus'    
        ).grid(row=0, column=0, ipadx=200, pady=10)


        # ---------------------------- Segmento 5 ----------------------------

        """
        Se agrega el segmento de visualización de los registros.

        """

        self.tree = ttk.Treeview(self.segmento5)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree.column("#0", width=30, minwidth=50, anchor=W)      # esta es la primer columna 
        self.tree.heading('#0', text='ID')                           # Definición del nombre de la columna
        self.tree.column("col1", width=80, minwidth=50, anchor=W)    # Esto es una tupla 
        self.tree.heading('col1', text='Producto')
        self.tree.column("col2", width=60, minwidth=50, anchor=W)
        self.tree.heading('col2', text='Categoría')
        self.tree.column("col3", width=60, minwidth=50, anchor=W)
        self.tree.heading('col3', text='Cantidad')
        self.tree.column("col4", width=120, minwidth=50, anchor=W)
        self.tree.heading('col4', text='Descripción')
        self.tree.column("col5", width=60, minwidth=90, anchor=W)
        self.tree.heading('col5', text='Precio')
        self.tree.grid(column=1, row=8, columnspan=6)
