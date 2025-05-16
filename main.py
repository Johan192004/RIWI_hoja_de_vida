from operator import indexOf
from opcion1 import *
from hojasDeVida import *
from verifies import *
import json

print(" ")

Equipo = "Error 404" 

add_cv(CVs)

while 1:

    print("1. Registrar una hoja de vida completa: ")
    print("2. Consultar hojas de vida")
    print("3. Actualizar informacion registrada")
    print("4. Generar reportes")
    print("5. Salir")

    option = input("Selecciona una opcion del 1 al 5: ")
    option = verifyInt(option, "Selecciona una opcion del 1 al 5: ")
    option = verifyRange(1,5,option,"Selecciona una opcion del 1 al 5: ")

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        with open("datos.json","w") as archivo:
            json.dump(CVs, archivo, indent=4)

        break
