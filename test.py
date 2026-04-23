# class palabra():
#     def __init__(self):
#         self.historial = []
#         pass

#     def historial(a):
#         return historial

#     def mostrar(self,a):
#         return a

# palabraOBJ = palabra()

# dic = {1: palabra.mostrar}

# opt = int(input("numero: "))

# a = int(input("Ingrese numero: "))

# print(f"texto",dic[opt](a))

# ---------------------------------

# class numeros():
#     def __init__(self):
#         self.historial = []

#     def agregarHistorial(self,a):
#         self.historial.append(a)

#     def mostrarHistorial(self):

#         pos = len(self.historial) - 1

#         for i in self.historial:
#             if pos > 0:
#                 print(i,end=",")
#                 pos -= 1
#             else:
#                 print(i)


# listaOBJ = numeros()

# for i in range (3):
#     listaOBJ.agregarHistorial(int(input("Ingrese un numero: ")))

# listaOBJ.mostrarHistorial()


# ------------------------------------

# Clases

# class Calculadora:
#     def __init__(self):
#         self.historial = [[] # numero A
#                           ,[] # numero B
#                           ,[]] # resultado

#     def mostrarHistorial(self):

#         for i in range(len(self.historial)):
#             a = self.historial[0][i]
#             b = self.historial[1][i]
#             resultado = self.historial[2][i]

#             print(f"{i+1}. {a} + {b} = {resultado}")


        

#     def sumar (self,a,b):
#         suma = a + b
#         self.historial[0].append(a)
#         self.historial[1].append(b)
#         self.historial[2].append(suma)
#         return suma
    

# CalculadoraOBJ = Calculadora()



# for i in range (3):
#     a = int(input("numero A: "))
#     b = int(input("numero B: "))
#     print(CalculadoraOBJ.sumar(a,b))

# print("==================================")

# CalculadoraOBJ.mostrarHistorial()


# ------------------------------------


x = (lambda x:x+5)

numero = int(input("Ingrese un numero: "))

print(x(numero))

suma = lambda a,b: a+b

class OperacionesLambda:
    def __init__(self):
        self.operaciones = {
            "+" : lambda a,b: a+b,
            "-" : lambda a,b: a-b
        }
    
    def calcular (self,a,b,opt):
        resultado = self.operaciones[opt](a,b)
        return resultado

a = int(input("A: "))
b = int(input("B: "))
opt = input("suma (+) o resta (-): ")



OP = OperacionesLambda()

print(OP.calcular(a,b,opt))