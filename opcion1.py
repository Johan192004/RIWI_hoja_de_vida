from datetime import date
from verifies import verifyInt, verifyName, verifyEmail, verifyEmpty, verifyRange, daysMonth

addresses = {}

def add_cv(dict):


    documet = input("Ingrese el numero de documento: ")
    documet = verifyInt(documet,"Ingrese un numero de documento valido: ")

    if str(documet) not in dict.keys():

        print("\nInformacion personal\n")

        name = input("Ingrese su nombre: ")
        name = verifyName(name, "Ingrese su nombre: ")

        cellPhone = input("Ingrese su numero de telefono: ")
        cellPhone = verifyInt(cellPhone,"Ingrese un numero de telefono valido: ") ###

        address = input("Ingrese su direccion: ")

        while 1:
            if address.replace(" ","") == "":
                print("Error, no ingresaste nada")
                address = input("Por favor ingresa tu direccion: ")
            else:
                break

        
        email = input("Ingrese su correo electronico: ")

        email = verifyEmail(email)

        while 1:

            if email in addresses:

                print("Error, el correo electronico ya se encuentra registrado")

                email = input("Ingrese su correo electronico: ")
                email = verifyEmail(email)

            else:
                break

        
        

        year = input("Ingresa tu año de nacimiento: ")
        year = verifyInt(year,"Ingresa tu año de nacimiento: ")
        year = verifyRange(1850,2010,year,"Ingresa tu año de nacimiento: ")

        print("1.Enero")
        print("2.Febrero")
        print("3.Marzo")
        print("4.Abril")
        print("5.Mayo")
        print("6.Junio")
        print("7.Julio")
        print("8.Agosto")
        print("9.Septiembre")
        print("10.Octubre")
        print("11.Noviembre")
        print("12.Diciembre")
        month = input("Selecciona tu mes de nacimiento(numero): ")
        month = verifyInt(month,"Selecciona tu mes de nacimiento(numero): ")
        month = verifyRange(1,12,month,"Selecciona tu mes de nacimiento(numero): ")

        day = input("Ingresa tu dia de nacimiento: ")
        day = verifyInt(day,"Ingresa tu dia de nacimiento: ")
        day = verifyRange(1, daysMonth[month - 1], day, "Ingresa tu dia de nacimiento: ")

        dateAge = (day,month,year)



        ### Academic
        print("\nFormacion academica\n")


        institution = input("Ingrese el nombre de la institucion: ")
        institution = verifyName(institution, "Ingrese el nombre de la institucion: ")

        title = input("Ingrese el titulo que obtuvo: ")
        title = verifyName(title, "Ingrese el titulo que obtuvo: ")

        startYear = input("Ingrese el año en el que comenzo a cursar el titulo: ")
        startYear = verifyInt(startYear, "Ingrese el año en el que comenzo a cursar el titulo: ")
        startYear = verifyRange(1930,2024,startYear, "Ingrese el año en el que comenzo a cursar el titulo: ")

        finishYear = input("Ingrese el año en finalizo los estudios: ")
        finishYear = verifyInt(finishYear, "Ingrese el año en finalizo los estudios: ")
        finishYear = verifyRange(startYear,2025,finishYear, "Ingrese el año en finalizo los estudios: ")

        
        ### Work
        print("\nExperiencia laboral\n")


        company = input("Ingrese el nombre de la compañia: ")
        company = verifyName(company, "Ingrese el titulo que obtuvo: ")

        job = input("Ingrese el cargo: ")
        job = verifyName(job, "Ingrese el cargo: ")


        responsability = input("Ingresa las funciones en tu cargo: ")
        responsability = verifyEmpty(responsability, "Ingresa las funciones en tu cargo: ")[1]

        duration = input("Ingresa la duracion en años: ")
        duration = verifyInt(duration, "Ingresa la duracion en años: ")

        ### Personal references
        print("\nReferencia personal\n")


        namePersonal = input("Ingrese el nombre de la referencia personal: ")
        namePersonal = verifyName(namePersonal, "Ingrese el nombre de la referencia personal: ")

        relationPersonal = input("Ingrese el parentesco de la referencia personal: ")
        relationPersonal = verifyName(relationPersonal, "Ingrese el parentesco de la referencia personal: ")

        PhoneNumberPersonal = input("Ingrese el numero de telefono de la referencia personal: ")
        PhoneNumberPersonal = verifyInt(PhoneNumberPersonal, "Ingrese el numero de telefono de la referencia personal: ")

        ### Work references
        print("\nReferencia laboral\n")



        nameWork = input("Ingrese el nombre de la referencia laboral: ")
        nameWork = verifyName(nameWork, "Ingrese el nombre de la referencia laboral: ")

        relationWork = input("Ingrese el parentesco de la referencia laboral: ")
        relationWork = verifyName(relationWork, "Ingrese el parentesco de la referencia laboral: ")

        PhoneNumberWork = input("Ingrese el numero de telefono de la referencia laboral: ")
        PhoneNumberWork = verifyInt(PhoneNumberWork, "Ingrese el numero de telefono de la referencia laboral: ")


        ### skills
        print("\nHabilidades\n")
        

        skill = input("Ingrese una habilidad suya: ")
        skill = verifyName(skill, "Ingrese una habilidad suya: ")

        ### certifications
        print("\nCertificados\n")


        certification = input("Ingrese un certificado que haya obtenido: ")
        certification = verifyName(certification, "Ingrese un certificado que haya obtenido: ")


        dict[str(documet)] = {
            "personalInfo":{
                "name":name,
                "phoneNumber": cellPhone,
                "address": address,
                "email": email,
                "dateAge":dateAge
            },

            "academicEducation":[
                (institution,title,f"{startYear} -- {finishYear}")
            ],

            "profesionalExperience":[
                (company, job, responsability, duration)
            ],

            "personalReferences":[
                (namePersonal, relationPersonal, PhoneNumberPersonal)
            ],

            "workReferences":[
                (nameWork, relationWork, PhoneNumberWork)
            ],

            "skills":{
                skill
            }    ,

            "certifications":{
                certification
            }


        }
