from opcion1 import *
from verifies import *
import json



from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def generar_pdf_cv(data, document):
    nombre_archivo = f"CV_{document}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=LETTER)
    width, height = LETTER
    y = height - 50

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, y, "Hoja de Vida")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Documento: {document}")
    y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Información Personal:")
    y -= 20
    c.setFont("Helvetica", 12)
    for key, value in data["personalInfo"].items():
        c.drawString(70, y, f"{key.capitalize()}: {value}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Formación Académica:")
    y -= 20
    for edu in data.get("academicEducation", []):
        c.drawString(70, y, f"- {edu}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Habilidades:")
    y -= 20
    for skill in data.get("skills", []):
        c.drawString(70, y, f"- {skill}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Certificaciones:")
    y -= 20
    for cert in data.get("certifications", []):
        c.drawString(70, y, f"- {cert}")
        y -= 20

    c.save()
    print(f"PDF generado: {nombre_archivo}")
# CVs = {10358:
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

CVs = 0

with open("datos.json","r") as dictionario:
    CVs = json.load(dictionario)

for key in CVs.keys():
    CVs[key]["skills"] = set(CVs[key]["skills"])
    CVs[key]["certifications"] = set(CVs[key]["certifications"])


# print(CVs)


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
        print(f"Duracion en años: {j[3]}")

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



def list_cvc_superior_export():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return

    try:
        n = int(input("Ingrese el número de años de experiencia: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    reporte = {}

    for document, data in CVs.items():
        experiencie = data.get("profesionalExperience", [])
        total_years = 0

        for item in experiencie:
            try:
                total_years += int(item[3])
            except (ValueError, IndexError):
                continue

        if total_years > n:
            reporte[document] = data

    if reporte:
        with open("reporte_experiencia_superior.json", "w", encoding="utf-8") as file:
            json.dump(reporte, file, indent=4, default=list)
        print("Reporte exportado como 'reporte_experiencia_superior.json'")
    else:
        print(f"No se encontraron hojas de vida con más de {n} años de experiencia.")

    
def ncertif_nformation_export():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return

    f = input("Ingrese el tipo de certificación o formación: ").strip()
    if f == "":
        print("CAMPO VACÍO: Por favor ingrese caracteres")
        return

    reporte = {}

    for document, data in CVs.items():
        name = data["personalInfo"]["name"]
        
        formation = data.get("academicEducation", [])
        found_in_formation = any(f.lower() in str(item).lower() for item in formation)

        skills = data.get("skills", set())
        found_in_skills = any(f.lower() in skill.lower() for skill in skills)

        certifications = data.get("certifications", set())
        found_in_certifications = any(f.lower() in cert.lower() for cert in certifications)

        if found_in_formation or found_in_skills or found_in_certifications:
            reporte[document] = data

    if reporte:
        with open("reporte_formacion_certificacion.json", "w", encoding="utf-8") as file:
            json.dump(reporte, file, indent=4, default=list)
        print("Reporte exportado como 'reporte_formacion_certificacion.json'")
    else:
        print(f"No se encontraron hojas de vida relacionadas con '{f}'.")

        
def export_single_cv_json(filename, document_id, cvs_data):
    def convert_sets(obj):
        if isinstance(obj, set):
            return list(obj)
        return obj

    if document_id in cvs_data:
        single_cv = {document_id: cvs_data[document_id]}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(single_cv, file, indent=4, default=convert_sets)
        print("Archivo exportado exitosamente como: ", filename)
    else:
        print("Documento no encontrado")



def menu_3():



    doc = input("Ingrese el documento de la cv la cual modificara: ")
    doc = verifyInt(doc, "Ingrese el documento de la cv la cual modificara: ")
    doc = str(doc)

    if doc in CVs.keys():
        print("¿Que desea actualizar?")
        print("1. Editar Datos personales")
        print("2. Añadir Formacion Academica")
        print("3. Añadir Experiencia profesional")
        print("4. Cambiar o Agregar Habilidades ")
        print("5 Cambiar o Agregar Referencias")
        print("6. Salir")
        
        opcion= input("Elije una opcion (1-6): ")
            
        match opcion:
            case "1":
                editar_datos_person(CVs[doc]["personalInfo"])
            case "2":
                agg_formacion(CVs[doc])
            case "3":
                profesionalExperience(CVs[doc])
            case "4":
                skills(CVs[doc])
            case "5":
                certifications(CVs[doc])
            case "6":
                pass
    
    else:
        print(f"No se encontro un cv con documento {doc}")
        
        
            
def editar_datos_person(CVs):
    print("Que desea Actualizar")
    print("1 Nombre")
    print("2 Contacto")
    print("3 Direccion")
    print("4 Correo")
    print("5 salir")    
    
    opcion= input("Opcion: ")
    

        
    if opcion == "1":
        CVs["name"] = input("Nuevo nombre: ")         
    elif opcion == "2":
        CVs["phoneNumber"]= int(input("Nuevo Contacto: "))
    elif opcion == "3":
        CVs["address"]= input("Niueva Direccion: ")
    elif opcion == "4":
        CVs["email"]= input("Nuevo Correo: ")     
    elif opcion == "5":
        menu_3()        
    else: 
        print("Opcion Invalido")
        
def agg_formacion(CVs):
    title  = input("Titulo Obtenido: ")
    institute = input("Institucion: ")
    years = input("Año de finalizacion: ")
    
    CVs["academicEducation"].append([
        title,
        institute,
        years
    ])
    
def profesionalExperience(CVs):
    company= input("Ingrese el nombre de la empresa")
    job= input("Ingrese el cargo o puesto")
    length= input("Ingrese la duracion en la empresa ")
    
    CVs["profesionalExperience"].append([
        company,
        job,
        length
    ])


    
def workReferences(CVs):
    print(f"Referencias actuales: {CVs['workReferences']} ")
    agg= input("Desea agregar alguna referencia (s/n): ")
    
    if agg.lower() == 's':
        name = input("Nombre de la referencia: ")
        relation = input("Ingrese el parentesco con la referencia laboral: ")
        phoneNumber= input("Ingrese el cel: ")
        CVs["workReferences"].append([
            name,
            relation,
            phoneNumber
        ])
    
def skills(CVs):
    print(f"Habilidades actuales: {CVs["skills"]}")
    agg= input("Desea agregar una habilidad? (s/n): ")
    
    if agg.lower() == 's':
        skills= input("Ingresar Nueva Habilidad: ")
        CVs['skills'].append(skills)   
    

def certifications(CVs):
    print(f"Certificaciones actuales: {CVs['certifications']} ")
    agg= input("Desea agregar alguna certificacion (s/n): ")
    
    if agg.lower() == 's':
        certification = input("Nombre del certificado: ")
        CVs["certifications"].append(certification)


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
                        break
                
                else:
                        print(f"La hoja de vida con nombre {name} no esta registrada")
                    
        elif option == 2:

            if len(CVs) == 0:
                print("No hay hojas de vida registradas")

            else:

                id = input("Ingrese el documento de la cv que quiere buscar: ")
                id = verifyInt(id, "Ingrese el documento de la cv que quiere buscar: ")
                id = str(id)
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

                    if value["personalInfo"]["email"] == e_mail:

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




while 1:

    print("Bienvenido a VitaeCoonsole")
    print("=========== Menu Principal =============")
    print("1. Registrar una hoja de vida completa: ")
    print("2. Consultar hojas de vida")
    print("3. Actualizar informacion registrada")
    print("4. Generar reportes")
    print("5. Exportar cv en pdf")
    print("6. Salir")

    option = input("Selecciona una opcion del 1 al 6: ")
    option = verifyInt(option, "Selecciona una opcion del 1 al 6: ")
    option = verifyRange(1,6,option,"Selecciona una opcion del 1 al 6: ")

    if option == 1:
        add_cv(CVs)
    elif option == 2:
        menu_2()
    elif option == 3:
        menu_3()
    elif option == 4:
        
        print("1. Exportar cvs con n años de experiencia")
        print("2. Exportar cvs con n skills o formacion")
        print("3. Exportar cv con un documento especifico")
        print("3. Salir")

        option = input("Seleccione una opcion: ")
        option = verifyInt(option, "Seleccione una opcion: ")
        option = verifyRange(1,3,option,"Seleccione una opcion: ")

        if option == 1:

            list_cvc_superior_export()
        
        elif option == 2:
            ncertif_nformation_export()
        elif option == 3:
            
            id_do = input("Ingrese el numero de documento de la cv que desea exportar: ")
            id_do = verifyInt(id_do, "Ingrese el numero de documento de la cv que desea exportar: ")
            id_do = str(id_do)

            if id_do in CVs.keys():
                export_single_cv_json("reporte.json",id_do,CVs)
            else:
                print(f"Cv con documento {id_do} no encontrado")
        else:
            pass
    elif option == 5:
            id_do = input("Ingrese el numero de documento de la cv que desea exportar en pdf: ")
            id_do = verifyInt(id_do, "Ingrese el numero de documento de la cv que desea exportar en pdf: ")
            id_do = str(id_do)

            if id_do in CVs.keys():
                generar_pdf_cv(CVs[id_do],id_do)
            else:
                print(f"Cv con documento {id_do} no encontrado")


    else:

        for key in CVs.keys():
            CVs[key]["skills"] = list(CVs[key]["skills"])
            CVs[key]["certifications"] = list(CVs[key]["certifications"])

        print(CVs)
        with open("datos.json","w") as archivo:


            json.dump(CVs, archivo, indent=4)

        break
