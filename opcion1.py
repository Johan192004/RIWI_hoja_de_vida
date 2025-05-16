from verifies import *

addresses = {}

def add_cv(dict):


    documet = input("Ingrese el documento")
    documet = verifyInt(documet,"Ingrese un numero de documento valido: ")

    if documet not in dict.keys():

        name = input("Ingrese su nombre: ")
        name = verifyName(name)

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

        company = input("Ingrese el nombre de la compañia: ")
        company = verifyName(company, "Ingrese el titulo que obtuvo: ")

        job = input("Ingrese el cargo: ")
        job = verifyName(job, "Ingrese el cargo: ")


        responsability = input("Ingresa las funciones en tu cargo: ")
        responsability = verifyEmpty(responsability, "Ingresa las funciones en tu cargo: ")

        duration = input("Ingresa la duracion en meses: ")
        duration = verifyInt(duration, "Ingresa la duracion en meses: ")

        ### Personal references

        name = input("Ingrese el nombre de la referencia personal: ")
        name = verifyName(name, "Ingrese el nombre de la referencia personal: ")

        relation = input("Ingrese el parentesco de la referencia personal: ")
        relation = verifyName(relation, "Ingrese el parentesco de la referencia personal: ")

        






