from operator import indexOf
from opcion1 import *
from hojasDeVida import *
from verifies import *
import json


# CVss = {10358:
#        {
#            "personalInfo":
#            {
#             "name":"Daniel",
#            "phoneNumber":321432543,
#            "address":"CR 54",
#            "email":"k@l.com",
#            "dateAge":("day","month","year")
#            },

#            "academicEductaion":[
#                ("institute","title","years")
#            ],

#             "profesionalExperience":[
#                 ("company","job","functions","duration")
#             ],

#             "personalReferences":[
#                 ("nombre","relation","phoneNumber")
#             ],

#             "workReferences":[
#                 ("nombre","relation","phoneNumber")
#             ],

#             "skills": set(
#                 ""
#             ),

#             "certifications": set(
#                 ""
#             )

#        }}


print(" ")

Equipo = "Error 404" 

CVss = 0

with open("datos.json","r") as dictionario:
    CVss = json.load(dictionario)

for key in CVss.keys():
    CVss[key]["skills"] = set(CVss[key]["skills"])
    CVss[key]["certifications"] = set(CVss[key]["certifications"])


print(CVss)

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
        add_cv(CVss)
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:

        for key in CVss.keys():
            CVss[key]["skills"] = list(CVss[key]["skills"])
            CVss[key]["certifications"] = list(CVss[key]["certifications"])

        print(CVss)
        with open("datos.json","w") as archivo:
            json.dump(CVss, archivo, indent=4)

        break
