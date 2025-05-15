def verifyInt(number,message):

    while 1:

        if number.isdigit():

            intNumber = int(number)

            return intNumber
        
        else:
            print("Error, valor no valido")
            number = input(message)

def verifyName(name):

    while 1:

        

        if all(x.isalpha() or x.isspace() for x in name):

            rightString = name.strip()

            return rightString
        
        else:
            print("Error, nombre no valido")
            name = input("Ingrese un nombre valido: ")



def verifyEmail(email):
    return email

def verifyDateAge():
    return ""