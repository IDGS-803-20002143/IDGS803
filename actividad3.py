class operacion():
    a=0
    b=0
   
    def suma(self):
        return self.a + self.b
    def resta(self):
        return self.a - self.b
    def multiplicacion(self):
        return self.a * self.b
    def divicion(self):
        return self.a / self.b
    

    
def main(op):
    obj = operacion()
    obj.a = float(input("primer numero"))
    obj.b = float(input("segundo numero"))


    if (op==1):
     print(obj.suma())
     elegir()
    elif (op==2):
     print(obj.resta())
    elif (op==3):
     print(obj.multiplicacion())
     elegir()
    elif (op==4):
     print(obj.divicion())
     elegir()
    if (op==5):
     print("salir")

def elegir():
     print(" operaciones.")
     print("1. Suma")
     print("2. Resta")
     print("3. Multiplicacion")
     print("4. Division")
     print("5. Salir")
     op =int(input("selecionar la opcion"))
     main(op)


    

        

if __name__ == "__main__":
        elegir()