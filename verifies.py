daysMonth = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]


def verifyInt(number,message):

    while 1:

        if number.isdigit():

            intNumber = int(number)

            return intNumber
        
        else:
            print("Error, valor no valido")
            number = input(message)

def verifyName(name, message):

    while 1:


        name = verifyEmpty(name,message)
        

        if all(x.isalpha() or x.isspace() for x in name):

            rightString = name.strip()

            return rightString
        
        else:
            print("Error, nombre no valido")
            name = input(message)



def verifyEmail(email):

    while 1:
        emailVerification = verifyEmpty(email,"Ingrese su correo electronico: ")
        if emailVerification[0]:

            email = emailVerification[1]
            if "@" in email and "." in email:

                rightEmail = email.strip()
                return rightEmail
            
            else:

                print("Error, el correo debe contener @ y puntos")
                email = input("Ingrese un correo electronico valido: ")
            



def verifyRange(start,finish,number,message):

    while 1:

        if number >= start and number <= finish:

            rightNumber = number
            return rightNumber
        else:

            print(f"Error, valor fuera de rango, tiene que estar entre {start} y {finish}")
            number = input(message)
            number = verifyInt(number,message)


def verifyEmpty(string,message):

    while 1:
        if string == "":

            print("Error, no ingresaste nada")
            string = input(message)
        else:

            return True,string
        
        #