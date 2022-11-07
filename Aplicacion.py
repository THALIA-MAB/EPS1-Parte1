from os import system
import time
import sqlite3

conexion = sqlite3.connect("Parillo_Vargas_Wong_almacen.db")

def crear():
    codigo = str(input("INGRESA EL CODIGO: "))
    nombre = str(input("INGRESE SU NOMBRE: "))
    precio = int(input("INGRESE SU PRECIO: "))
    if(len(codigo) > 0 and len(nombre) > 0 ):
        consulta = """ INSERT INTO
                   producto(codigo,nombre,precio)
                   VALUES(?,?,?)
               """
        parametros =(codigo,nombre,precio)
        cursor = conexion.cursor()
        cursor.execute(consulta,parametros)
        conexion.commit()
        conexion.close()

def listar():
    consulta = """ SELECT *
                   FROM producto
               """
    cursor = conexion.cursor()
    productos =  cursor.execute(consulta)
 

    #Acá libros es una lista ...
   
    
    for data in productos:
        print(""" 
        ID :        {}
        codigo :    {}
        nombre :     {}
        precio :     {}
        """.format(data[0],data[1],data[2],data[3]))
    conexion.close()
    
def modificar():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
      codigo = str(input("INGRESA EL CODIGO: "))
      nombre = str(input("INGRESE SU NOMBRE: "))
      precio = int(input("INGRESE SU PRECIO: "))
      consulta = """ UPDATE producto
                   SET
                      codigo = ?,
                      nombre = ?,
                      precio = ?
                   WHERE
                        idproducto = ?
               """
    parametros = (codigo,nombre,precio,id)
    cursor = conexion.cursor()
    cursor.execute(consulta,parametros)
    conexion.commit()
    conexion.close()

def eliminar():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        consulta = """ DELETE FROM producto
                   WHERE
                        idproducto = ?
               """
    parametro=(id,)
    cursor = conexion.cursor()
    cursor.execute(consulta,parametro)
    conexion.commit()
    conexion.close()
    
def salir():
    exit()

while True:
    print("=========================================")
    print("\tMENU")
    print("=========================================")
    print("\t[1] REGISTRA")
    print("\t[2] ELIMINA")
    print("\t[3] EDITAR")
    print("\t[4] LISTAR")
    print("\t[5] Salir")
    print("=========================================")

    try:
        opcion = int(input("Selecciona una opcion: "))
        
        if(opcion == 1):
            crear()
            
        elif (opcion == 2):
            eliminar()
            
        elif (opcion == 3):
            modificar()
            
        elif (opcion == 4):
            listar()

        elif (opcion == 5):
            salir()
            break
        
    except:
        print("Por favor, selecciona las opciones correctas")
        system("clear")