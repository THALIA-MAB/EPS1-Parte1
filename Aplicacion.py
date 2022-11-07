from os import system
import time
import sqlite3


def crear():
    exit()

def listar():
    exit()
    
def modificar():
    exit()

def eliminar():
    exit()
    
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
            listar()
            
        elif (opcion == 3):
            modificar()
            
        elif (opcion == 4):
            eliminar()

        elif (opcion == 5):
            salir()
            break
        
    except:
        print("Por favor, selecciona las opciones correctas")
        system("clear")