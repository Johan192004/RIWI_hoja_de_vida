

    
from verifies import verifyInt


CVs = {10352:
        {
            "personalInfo":
            {
            "name":"Daniel",
            "phoneNumber":321432543,
            "address":"CR 54",
            "email":"k@l.com",
            "birthAge":(2000)
            },

            "academicEductaion":[
                ("institute","title","years")
            ],

            "profesionalExperience":[
                ("company","job","length")
            ],

            "personalReferences":[
                ("nombre","relation","phoneNumber")
            ],

            "workReferences":[
                ("nombre","relation","phoneNumber")
            ],

            "skills": set(
                ""
            ),

            "certifications": set(
                ""
            )

        }}
        


def menu_3():

    while 1:

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
            
            opcion= input("Elije una opcion (1-5): ")
                
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
                    break
        
        else:
            print(f"No se encontro un cv con documento {doc}")
        
        
            
def editar_datos_person(CVs):
    print("Que desea Actualizar")
    print("1 Nombre")
    print("2 Contacto")
    print("3 Direccion")
    print("4 Correo")
    print("5 salir")    
    
    opcion= input("Opcion: ").strip().lower()
    
    if opcion in CVs:
        
        if opcion == "1":
            CVs["name"] = input("Nuevo nombre: ")         
        elif opcion == "2":
            CVs["phoneNumber"]= int(input("Nuevo Contacto: "))
        elif opcion == "3":
            CVs["address"]= input("Niueva Direccion")
        elif opcion == "4":
            CVs["email"]= input("Nuevo Correo")     
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
        

    
    
    
    