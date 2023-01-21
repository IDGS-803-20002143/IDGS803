def menu():
    print("App de operaciones.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    op = input ("Escriba la opcion:")

    op = int(op)

    if op==1: suma()
    elif op==2: resta()
    elif op==3: multiplicacion()
    elif op==4: division()
    else: exit("hasta luego")

    def suma():
     print("")
     print ("suma")
     num1 = input("Numero 1: ")
     num2 = input("Numero 2: ")
     num1 = float(num1)
     num2 = float(num2)
     print ("Resultado: ", num1+num2)
     print("")
     menu()
    
def resta():
    print("")
    print ("resta.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1-num2)
    print("")
    menu()

def multiplicacion():
    print("")
    print ("multiplicacion.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1*num2)
    print("")
    menu()

def division():
    print("")
    print ("division.")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")
    num1 = float(num1)
    num2 = float(num2)
    print ("Resultado: ", num1/num2)
    print("")
    menu()
menu()