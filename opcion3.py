
    
    
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
        

def menu():
    while True:
        print("¿Que desea actualizar?")
        print("1. Editar Datos personales")
        print("2. Añadir Formacion Academica")
        print("3. Añadir Experiencia profesional")
        print("4. Cambiar o Agregar Habilidades ")
        print("5 Cambiar o Agregar Referencias")
        
        opcion= input("Elije una opcion (1-4): ")
            
        match opcion:
            case "1":
                aditar_datos_person(CVs)
            case "2":
                agregar_formacion(CVs)
            case "3":
                profesionalExperience(CVs)
            case "4":
                pass    
        
            
def aditar_datos_person(CVs):
    print("Que desea Actualizar")
    print("1 Nombre")
    print("2 Contacto")
    print("3 Direccion")
    print("4 Correo")
    print("5 salir")    
    
    opcion= input("Opcion: ").strip().lower()
    
    if opcion in CVs:
        
        if opcion == "1":
            CVs["nombre"] = input("Nuevo nombre: ")         
        elif opcion == "2":
            CVs["contacto"]= input("Nuevo Contacto: ")
        elif opcion == "3":
            CVs["direccion"]= input("Niueva Direccion")
        elif opcion == "4":
            CVs["Correo"]= input("Nuevo Correo")     
        elif opcion == "5":
            menu()        
        else: 
            print("Opcion Invalido")
        
def agregar_formacion(CVs):
    title  = input("Titulo Obtenido: ")
    institute = input("Institucion: ")
    years = input("Año de finalizacion: ")
    
    CVs["academicEductaion"].append({
        "title":title,
        "institute":institute,
        "years":years
    })
    
def profesionalExperience(CVs):
    company= input("Ingrese el nombre de la empresa")
    job= input("Ingrese el cargo o puesto")
    length= input("Ingrese la duracion en la empresa ")
    
    CVs["profesionalExperience"].append({
        "company":company,
        "job":job,
        "length":length
    })


    
def workReferences(CVs):
    print=(f"Referencias actuales: {CVs['workReferences']} ")
    agg= input("Desea agregar alguna referencia (s/n): ")
    
    if agg.lower() == 's':
        name = input("Nombre de la referencia: ")
        phoneNumber= input("Ingrese el cel: ")
        CVs["workReferences"].append({
            "name":name,
            "phoneNumber":phoneNumber
        })
    
def skills(CVs):
    print(f"Habilidades actuales: {CVs['skills']}")
    agg= input("Desea agregar una habilidad? (s/n): ")
    
    if agg.lower() == 's':
        skills= input("Ingresar Nueva Habilidad: ")
        CVs['skills'].append(skills)   
    

def certifications(CVs):
    print=(f"Certificaciones actuales: {CVs['certifications']} ")
    agg= input("Desea agregar alguna certificacion (s/n): ")
    
    if agg.lower() == 's':
        name = input("Nombre del certificado: ")
        CVs["certifications"].append({
    
        })
    
        
menu()
    
    
    
    