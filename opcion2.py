import email
import json
from verifies import * 

with open("datos.json", "r") as f:
    CVs = json.load(f)

# def search_cvs(query = "", experiencia_min = None, formacion = None, habilidad = None):
#     resultados = []

#     for cv in CVs:
#         if (query.lower() in cv["name"].lower() or query in cv["document"] or query.lower() in cv["email"].lower()):

#             if experiencia_min and cv["experiencia"] < experiencia_min:
#                 continue

#             if formacion and cv["formacion"].lower() != formacion.lower():
#                 continue   

#             if habilidad and habilidad not in cv["habilidades"]:
#                 continue

#             resultados.append(cv)
    # return resultados
SUCCESS = "\033[92m"    
RESET = "\033[0m"
DANGER = "\033[91m"
def show_cv(cv,id):
    print("\nInformacion personal\n")
    print(f"Documento: {id}")
    print(f"Nombre: {cv["personalInfo"]["name"]}")
    print(f"Numero de telefono: {cv["personalInfo"]["phoneNumber"]}")
    print(f"Direccion: {cv["personalInfo"]["address"]}")
    print(f"Correo: {cv["personalInfo"]["email"]}")
    print(f"Fecha de nacimiento: dia:{cv["personalInfo"]["dateAge"][0]} mes:{cv["personalInfo"]["dateAge"][1]} años: {cv["personalInfo"]["dateAge"][2]}")
    
    print(f"\nEducacion\n")
    for h in cv["academicEducation"]:
        print(f"Institucion: {h[0]}")
        print(f"Titulo: {h[1]}")
        print(f"Años: {h[2]}")

    print("\nExperiencia profesional\n")
    for j in cv["profesionalExperience"]:

        print(f"Compañia: {j[0]}")
        print(f"Cargo: {j[1]}")
        print(f"Responsabilidades: {j[2]}")
        print(f"Duracion en meses: {j[3]}")

    print("\nReferencias personales\n")
    for k in cv["personalReferences"]:
        print(f"Nombre: {k[0]}")
        print(f"Parentesco: {k[1]}")
        print(f"Numero de telefono: {k[2]}")

    print("\nReferencias Laborales\n")

    for q in cv["workReferences"]:
        print(f"Nombre: {q[0]}")
        print(f"Relacion: {q[1]}")
        print(f"Numero de telefono: {q[2]}")

    print("\nHabilidades\n")
    for t in cv["skills"]:
        print(f"-{t}")    
        
    print("\nCertificaciones\n")
    for u in cv["certifications"]:
        print(f"-{u}")


def menu_2():

    print("Que desea?")
    print("1. Buscar hoja de vida")
    print("2. Filtrar experiencia o habilidades")
    print("3. Regresar al menu")

    option = input("Seleccione una opcion: ")
    option = verifyInt(option,"Seleccione una opcion: ")
    option = verifyRange(1,3,option,"Seleccione una opcion: ")

    if option == 1:

        print("=== CONSULTA DE HOJAS DE VIDA ===")
        print("1. Buscar por nombre")
        print("2. Buscar por documento")
        print("3. Buscar por correo")
        print("4. Regresar al menu")

        option = input("Seleccione una opcion: ")
        option = verifyInt(option, "Seleccione una opcion: ")
        option = verifyRange(1,4,option,"Seleccione una opcion: ")


        if option == 1:

            if len(CVs) == 0:
                print("No hay hojas de vida registradas")
            else:

                name = input("Ingrese el nombre de la persona que desea buscar: ")
                name = verifyName(name, "Ingrese el nombre de la persona que desea buscar: ")

                for key,value in CVs.items():

                    if value["personalInfo"]["name"] == name:

                        show_cv(value,key)
                
                else:
                        print(f"La hoja de vida con nombre {name} no esta registrada")
                    
        elif option == 2:

            if len(CVs) == 0:
                print("No hay hojas de vida registradas")

            else:

                id = input("Ingrese el documento de la cv que quiere buscar: ")
                id = verifyInt(id, "Ingrese el documento de la cv que quiere buscar: ")

                for key,value in CVs.items():

                    if key == id:

                        show_cv(value,id)
                
                else:
                        print(f"La hoja de vida con documento {id} no esta registrada")
            
        elif option == 3:

            if len(CVs) == 0:
                print("No hay hojas de vida registradas")
            else:

                e_mail = input("Ingrese el correo electronico de la hoja de vida que esta buscando: ")
                e_mail = verifyEmail(e_mail)

                for key,value in CVs.items:

                    if value["personalInfo"]["email"] == email:

                        show_cv(value,key)

                else:
                        print(f"La hoja de vida con correo {e_mail} no esta registrada")

        else:
            print("Regresando al menu principal")

    if option == 2:

        if len(CVs) == 0:
            print("No hay hojas de vida registradas")
        else:

            print("Por cual criterio desea filtrar?")
            print("1. Por años de experiencia")
            print("2. Por habilidades")
            print("3. Regresar al menu")

            option = input("Seleccine una opcion: ")
            option = verifyInt(option, "Seleccine una opcion: ")
            option = verifyRange(1,3, option, "Seleccine una opcion: ")

            if option == 1:

                exp = input("Ingrese la experiencia laboral minima en meses: ")
                exp = verifyInt(exp,"Ingrese la experiencia laboral minima en meses: ")

                how_many = 0
                for key,value in CVs.items:

                    sums = 0
                    
                    for k in value["profesionalExperience"]:

                        sums += k[2]
                    
                    if sums >= exp:
                        how_many += 1
                        show_cv(value,key)
                    
                print(f"Se entontraron {how_many} hojas de vida")


            elif option == 2:

                skill = input("Ingrese la habilidad que esta buscando: ")
                skill = verifyName(skill, "Ingrese la habilidad que esta buscando: ")

                how_many = 0
                for key,value in CVs.items:

                    sums = 0
                    
                    for k in value["profesionalExperience"]:

                        if k == skill:
                            how_many += 1
                            show_cv(value,key)
                    
                print(f"Se entontraron {how_many} hojas de vida")
            
            else:
                print("Regresando al menu principal")




if __name__ == '__main__':
    while True:
        menu_2()
        continuar = input("¿Deseas hacer otra búsqueda? (s/n): ").strip().lower()
        if continuar != 's':
            break
