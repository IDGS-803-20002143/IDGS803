
def multiplicar():
    print("multiplicar")
    num1=int(input("dame un numero: "))

    for x in range(1,11):
        print("{} * {} = {}".format(num1,x,(num1*x)))
multiplicar()
