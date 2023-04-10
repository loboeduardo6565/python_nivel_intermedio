"""
Inicialmente se importan todas las librerías requeridas para el funcionamiento de la aplicación. 

"""

import tkinter as tk
from tkinter import *
from tkinter import ttk 
import tkinter as tk
from PIL import ImageTk, Image
#import sqlite3
from tkinter import messagebox
#import re
import model

"""
Se definen varias variables que serán utilizadas para almacenar la información de los productos que se agregarán a una lista.

""" 




"""
Se crea una instancia de la clase Tk() para crear la ventana principal de la aplicación.

""" 

ventana = Tk() # inicio del lanzamiento de la ventana, solo puede haber una ventana principal. 
ventana.geometry("440x530")
ventana.resizable(0,0) # Se bloquea la modificación del tamaño de la ventana por parte del usuario.
ventana.title("Inventario de Repuestos") #bg='#2e2e2e'

var_name = StringVar()
var_categoria = StringVar()
var_cantidad = IntVar()
var_precio = DoubleVar()
var_desc = StringVar()



"""
Creación de Segmentos, se crean varios objetos Frame que se usarán para organizar los elementos de la interfaz gráfica.

"""

segmento1 = Frame(ventana) 
segmento1.grid(row=0, column=0)
segmento1.place(x=20, y=50)
segmento2 = Frame(ventana)
segmento2.grid(row=0, column=2)
segmento2.place(x=290, y=0)
segmento3 = Frame(ventana)
segmento3.grid(row=1, column=0)
segmento3.place(x=40, y=210)
segmento4 = Frame(ventana)
segmento4.grid(row=2, column=0)
segmento4.place(x=20, y=260)
segmento5 = Frame(ventana)
segmento5.grid(row=5, column=0)
segmento5.place(x=15, y=280)

"""
Se crean varios objetos Label, Entry, Combo y Spin que se utilizarán para 

recopilar información sobre los productos que se agregarán al inventario,

estos objetos se asociaran a las variables creadas previamente. 

"""


# ---------------------------- Segmento 1 ----------------------------

name = Label(segmento1, text= "Nombre del producto")    # En este caso saco el nombre de la ventana principal y le asigno el nombre del segmento
name.grid(row=0, column=0, sticky=E)                    # sticky permite personalizar la ubicación de los objetos
entry_name = Entry(segmento1, textvariable=var_name)    # textvariable permite setear el valor de la variable definido en el campo entry 
entry_name.grid(row=0, column=1, sticky=E) 

categoria = Label(segmento1, text="Categoría")
categoria.grid(row=1, column=0, sticky=W)
comboCategoria = ttk.Combobox(segmento1, textvariable=var_categoria) 
comboCategoria = ttk.Combobox(
    state="readonly",
    values=["ACCESORIOS", "AUTOPARTES", "DISTRIBUCION", "ELECTRICO",\
            "EMBRAGUE", "ENCENDIDO", "FILTROS", "FRENOS", "MOTOR", \
            "REFRIGERACION", "SUSPENSION", "TRANSMISION"]
)
comboCategoria.set("ACCESORIOS")
comboCategoria.place(x=141, y=72, width=124)

cantidad = Label(segmento1, text="Cantidad")
cantidad.grid(row=2, column=0, sticky=W)
# Se agrega un SpinBox para evitar errores de tipeo
spin_cantidad = Spinbox(segmento1, textvariable=var_cantidad, from_=0, to=10000, increment=1, state="readonly", width=18) 
spin_cantidad.grid(row=2, column=1, sticky=W)
spin_cantidad.config(justify="right")

precio = Label(segmento1, text="Precio")
precio.grid(row=3, column=0, sticky=W)
entry_precio = Entry(segmento1, textvariable=var_precio, width=10)
entry_precio.grid(row=3, column=1, sticky=W)

desc = Label(segmento1, text="Descripción")
desc.grid(row=4, column=0, sticky=W)
entry_desc = Entry(segmento1, textvariable=var_desc) 
entry_desc.grid(row=4, column=1, sticky=W)

# ---------------------------- Segmento 2 ----------------------------

# Se agrega la imagen

imagen=tk.PhotoImage(file="amortiguadores.png") 
imagen_chica=imagen.subsample(6) #Se reduce las dimensiones de la imagen en un (ancho_imagen / 6)
imagen=ttk.Label(segmento2, image=imagen_chica)
imagen.grid(row=0, column=0, pady=20, sticky=E)



# ---------------------------- Segmento 3 ----------------------------

"""
Se agregan los botones del CRUD

"""



#boton_a = Button(segmento3, text= "Agregar", command=modelo.agregar_01, width=10, height=1)
#boton_a.grid(row= 0, column=0, padx=7, pady=20)
boton_c = Button(segmento3, text= "Consultar", command=lambda:model.consultar(comboCategoria.get(), tree), width=10, height=1, )
boton_c.grid(row= 0, column=1, padx=7, pady=20)
#boton_u = Button(segmento3, text= "Modificar", command=modelo.modificar, width=10, height=1) #, state=DISABLED
#boton_u.grid(row= 0, column=2, padx=7, pady=20)
#boton_m = Button(segmento3, text= "Borrar", command=modelo.borrar, width=10, height=1) #, state=DISABLED
#boton_m.grid(row= 0, column=3, padx=7, pady=20)

# ---------------------------- Segmento 4 ----------------------------

ttk.Separator(
    master=segmento4,
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



tree = ttk.Treeview(segmento5)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=30, minwidth=50, anchor=W)      # esta es la primer columna 
tree.heading('#0', text='ID')                           # Definición del nombre de la columna
tree.column("col1", width=80, minwidth=50, anchor=W)    # Esto es una tupla 
tree.heading('col1', text='Producto')
tree.column("col2", width=60, minwidth=50, anchor=W)
tree.heading('col2', text='Categoría')
tree.column("col3", width=60, minwidth=50, anchor=W)
tree.heading('col3', text='Cantidad')
tree.column("col4", width=120, minwidth=50, anchor=W)
tree.heading('col4', text='Descripción')
tree.column("col5", width=60, minwidth=90, anchor=W)
tree.heading('col5', text='Precio')
tree.grid(column=1, row=8, columnspan=6)


ventana.mainloop() # Fin del lanzamiento de la ventana
