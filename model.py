import sqlite3
import re

"""
Se crea la base de datos y el cursor de conexión. 

"""
product_id = 0 # Se declara la variable Global correspondiente al id

class Crud():
    def __init__(self):
        try:
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
        except:
            pass

    def connect(self,):
        conn = sqlite3.connect("proyecto_01.db") # Creamos la BD 
        return conn

    """ Función que permite validar que los campos implicados en operaciones como modidificar o agregar no se encuentren vacíos. """
    def validacion(self, var_name, var_cantidad, var_desc):
       return len(var_name) != 0 and int(var_cantidad) != 0  and len(var_desc) != 0

    def agregar_01(self, var_name, var_categoria, var_cantidad, var_desc, var_precio, tree):
       """ Inicialmente hace un llamado a la función validación y luego de validar 
       el valor correspondiente al campo de precio agregar un nuevo registro a la BD
       """
       if self.validacion(var_name, var_cantidad, var_desc):
           # Generando la Instrucción en pasos. 
           conn = self.connect()
           cursor = conn.cursor()
           patron1 = re.compile(
           r"""\d +  # Parte entera
                          \.    # Punto decimal
                          \d *  # Parte de fracción""",
           re.X,
           )
           precio = str(var_precio)
           if patron1.search(precio):
               var_name=var_name
               var_categoria=var_categoria
               var_cantidad=var_cantidad
               var_precio=var_precio
               var_desc=var_desc
               repuestos = [
               (var_name), 
               (var_categoria), 
               (var_cantidad),
               (var_precio),
               (var_desc),
               ]
               cursor.execute("INSERT INTO REPUESTOS VALUES (NULL,?,?,?,?,?)", repuestos) # NOMBRE CATEGORIA CANTIDAD PRECIO DESC
               conn.commit() #Guardando el registro
               tree.insert("","end", text=str(product_id), values=(var_name, var_categoria, var_cantidad, var_desc, var_precio))
               #limpiar()
               #agregar_msj()
           else:
               #messagebox.showerror("Error en campo Precio", "Debe ingresar el monto con decimales")
               print("Error en campo Precio, Debe ingresar el monto con decimales")
               print(type(precio))
               print(patron1.search(precio))
       else:
           #messagebox.showerror("Error al agregar", "Debe agregar la información de cada campo") 
           print("Error al agregar, Debe agregar la información de cada campo")     

    def agregar(var_name, var_categoria, var_cantidad, var_desc, var_precio, tree):
       """ Función que permite llenar el treeview """
       tree.insert("","end", text=str(product_id), values=(var_name.get(), var_categoria.get(), var_cantidad.get(), var_desc.get(), var_precio.get()))

    def limpiar_tree(self, tree):
        """ Función que permite limpiar el treeview"""
        for content in tree.get_children():
            tree.delete(content)

    def consultar(self, comboCategoria, arbol):
        """ Función que permite consultar los datos existentes dentro de la BD a través del campo CATEGORÍA """
        print('consultar')
        print("Limpiando el treeview")
        conn = self.connect()
        cursor = conn.cursor()
        categoria=[comboCategoria,] # No está trayendo el parametro desde la vista 
        print(categoria)
        cursor.execute("SELECT * FROM REPUESTOS WHERE CATEGORIA=?", categoria)
        consulta = cursor.fetchall()
        print(consulta)
        for registro in consulta:
            print(registro)
            arbol.insert("","end", text = registro[0], values=(registro[1], registro[2], registro[3], registro[5],registro[4]))

    def modificar(self, var_name, var_categoria, var_cantidad, var_desc, var_precio, tree):
       """ Función que permite modificar los datos de un registro existente posicionandose en el registro que quiere modificar """
       if self.validacion(var_name, var_cantidad, var_desc):
           item = tree.focus()
           if item:
               item_id = tree.item(tree.selection())['text']        
               conn = self.connect()
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
               print("Información, Se ha modificado el registro seleccionado")
           else:
               print("Error, Debe posicionarse en el item a modificar") 
       else:
           print("Error, Debe agregar la información a modificar en cada campo")

    def borrar(self, tree):
        """ Función que permite borrar un registro de la BD posicionandose en el mismo desde el treeview """
        item = tree.focus()
        if item:
            item_id = tree.item(tree.selection())['text']
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM REPUESTOS WHERE PRODUCT_ID=?", (item_id,)) # La coma la agregamos ya que el item_id es un entero, pero está representado dentro de una tupla
            conn.commit()
            print(f"Borrando el registro con el Product_ID {item_id} de la BD")
            tree.delete(item)
            print("Limpiando el registro del Treeview")
        else:
            print("Información, Se debe seleccionar un registro")