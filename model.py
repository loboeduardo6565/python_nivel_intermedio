
from tkinter import *
import sqlite3
from tkinter import messagebox
import re

"""
Se crea la base de datos y el cursor de conexión. 

"""

conn = sqlite3.connect("proyecto_01.db") # Creamos la BD 
cursor = conn.cursor() # Creamos el cursor


# Creamos la Tabla si no existe. 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS REPUESTOS(
        PRODUCT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50),
        CATEGORIA VARCHAR(50),
        CANTIDAD INTEGER,
        PRECIO REAL,
        DESC VARCHAR(50)
        )
''') 

conn.commit() # Para impactar la query anterior 

product_id = 0 # Se declara la variable Global correspondiente al id



"""
Definición de todas las funciones que se utilizaran. 

"""

def validacion(var_name, var_cantidad, var_desc):
   """ Función que permite validar que los campos implicados no se encuentren vacíos. """
   return len(var_name) != 0 and int(var_cantidad) != 0  and len(var_desc) != 0
#       
# def agregar_01():
#    """ Inicialmente hace un llamado a la función validación y luego de validar 
#    
#    el valor correspondiente al campo de precio agregar un nuevo registro a la BD
#    
#    """
#
#    if validacion():
#        # Generando la Instrucción en pasos. 
#        cursor = conn.cursor()
#        
#        patron1 = re.compile(
#        r"""\d +  # Parte entera
#                       \.    # Punto decimal
#                       \d *  # Parte de fracción""",
#        re.X,
#        )
#
#        precio = precio.get()
#        if patron1.search(precio):
#            var_name=var_name.get()
#            var_categoria=var_categoria.get()
#            var_cantidad=var_cantidad.get()
#            var_precio=var_precio.get()
#            var_desc=var_desc.get()
#            repuestos = [
#            (var_name.get()), 
#            (var_categoria.get()), 
#            (var_cantidad.get()),
#            (var_precio.get()),
#            (var_desc.get()),
#            ]
#            cursor.execute("INSERT INTO REPUESTOS VALUES (NULL,?,?,?,?,?)", repuestos) # NOMBRE CATEGORIA CANTIDAD PRECIO DESC
#            conn.commit() #Guardando el registro
#            agregar()
#            limpiar()
#            agregar_msj()
#        else:
#            messagebox.showerror("Error en campo Precio", "Debe ingresar el monto con decimales")
#            print(type(precio))
#            print(patron1.search(precio))
#    else:
#        messagebox.showerror("Error", "Debe agregar la información de cada campo") 
#
# def agregar_msj():
#    messagebox.showinfo("Información", "Se ha guardado un nuevo registro") 
#
# def borrando_msj():
#    messagebox.showerror("Repuesto Borrado", "Se ha borrado el registro seleccionado") 
#
# def agregar(tree,var_name, var_categoria, var_cantidad, var_desc, var_precio):
#    """ Función que permite llenar el treeview """
#
#    tree.insert("","end", text=str(product_id), values=(var_name.get(), var_categoria.get(), var_cantidad.get(), var_desc.get(), var_precio.get()))

# def limpiar(var_name, var_categoria, var_cantidad, var_desc, var_precio):
#     """ Función que permite limpiar los campos de ingreso"""
# 
#    var_name.set("")
#    var_categoria.set("")
#    var_cantidad.set(0)
#    var_desc.set("")
#    var_precio.set(0)

def limpiar_tree(tree):
    """ Función que permite limpiar el treeview"""

    for content in tree.get_children():
        tree.delete(content)



def consultar(comboCategoria, arbol):
    """ Función que permite consultar los datos existentes dentro de la BD a través del campo CATEGORÍA """

    print('consultar')
    #limpiar_tree()
    print("Limpiando el treeview")
    cursor = conn.cursor()
    categoria=[comboCategoria,] # No está trayendo el parametro desde la vista 
    print(categoria)
    cursor.execute("SELECT * FROM REPUESTOS WHERE CATEGORIA=?", categoria)
    consulta = cursor.fetchall()
    print(consulta)
    for registro in consulta:
        #print("No llega aqui")
        print(registro)
        arbol.insert("","end", text = registro[0], values=(registro[1], registro[2], registro[3], registro[5],registro[4]))
    #limpiar()

def modificar(var_name, var_categoria, var_cantidad, var_desc, var_precio, tree):
   """ Función que permite modificar los datos de un registro existente posicionandose en el registro que quiere modificar """
   if validacion(var_name, var_cantidad, var_desc):
       item = tree.focus()
       if item:
           item_id = tree.item(tree.selection())['text']        
           cursor = conn.cursor()
           repuestos = [
               var_name, 
               var_categoria, 
               var_cantidad,
               var_precio,
               var_desc,
               item_id,
               ]
           cursor.execute("UPDATE REPUESTOS SET NOMBRE = ?, CATEGORIA = ?, CANTIDAD = ?, PRECIO = ?, DESC = ? WHERE PRODUCT_ID=?", repuestos)
           conn.commit()
           print(f"Modificando el registro con el Product_ID {item_id} de la BD")
           tree.get_children()
           messagebox.showinfo("Información", "Se ha modificado el registro seleccionado") 
           #consultar()
           #limpiar()
       else:
           messagebox.showerror("Error", "Debe posicionarse en el item a modificar") 
   else:
       messagebox.showerror("Error", "Debe agregar la información a modificar en cada campo")

#def borrar(tree):
#    """ Función que permite borrar un registro de la BD posicionandose en el mismo desde el treeview """
#
#    item = tree.focus()
#    if item:
#        item_id = tree.item(tree.selection())['text']
#        cursor = conn.cursor()
#        cursor.execute("DELETE FROM REPUESTOS WHERE PRODUCT_ID=?", (item_id,)) # La coma la agregamos ya que el item_id es un entero, pero está representado dentro de una tupla
#        conn.commit()
#        print(f"Borrando el registro con el Product_ID {item_id} de la BD")
#        tree.delete(item)
#        print("Limpiando el registro del Treeview")
#        borrando_msj()
#        limpiar()
#    else:
#        messagebox.showinfo("Información", "Se debe seleccionar un registro") 