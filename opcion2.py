
from hojasDeVida import *

def option2():
    if len(CVs) == 0:         
        
        print("Error: No tienes registrado nada aun...")
    else:
        search = input("Ingresa el nombre del producto a buscar: ")
        value = CVs.get(search)              
        

        if value is None:                     
            
            print("Producto no existe")
        else:
            print(f"El nombre del producto es: {search}")   
            print(f"El precio es: {CVs[search]["price"]}")        
            print(f"La cantidad del producto es: {CVs[search]["quantity"]}")

    menu()