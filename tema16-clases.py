class padre():
    x=1
class operasbas():
    #defunur propiedades de clase
    num1=0
    num2=0
    res=0
    #definir constructr de  clase
    #def __init__(self, *args) 
    
    #definimos los metodos de la clase
    def suma(self,a,b):
        self.num1=a
        self.num2=b
        return a+b

obj=operasbas()