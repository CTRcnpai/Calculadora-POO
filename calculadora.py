# Clases

class Calculadora:
    def __init__(self):
        self.historial = [[], # NUMERO A
                     [], # OPERACION
                     [], # NUMERO B
                     []] # RESULTADO

    def mostrarHistorial (self):
        if len(self.historial[3]) != 0:
            print("\n=== LISTA DE OPERACIONES EN ORDEN === \n")
            for i in range(len(self.historial[3])):
                a = self.historial[0][i]
                operacion = self.historial[1][i]
                b = self.historial[2][i]
                resultado = self.historial[3][i]

                print(f"{i+1}. {a} {operacion} {b} = {resultado}")

        else:
            print ("\nNo hay historial que mostrar\n")

    def sumar (self,a,b):
            resultado = a + b
            self.historial[0].append(a)
            self.historial[1].append("+")
            self.historial[2].append(b)
            self.historial[3].append(resultado)
            return resultado


    def restar (self, a,b):
            resultado = a - b
            self.historial[0].append(a)
            self.historial[1].append("-")
            self.historial[2].append(b)
            self.historial[3].append(resultado)
            return resultado

    def multiplicar (self, a,b):
            resultado = a * b
            self.historial[0].append(a)
            self.historial[1].append("*")
            self.historial[2].append(b)
            self.historial[3].append(resultado)
            return resultado

    def dividir (self, a,b):
        if  b != 0:
            resultado = a / b
            self.historial[0].append(a)
            self.historial[1].append("/")
            self.historial[2].append(b)
            self.historial[3].append(resultado)
            return resultado
        else:
            print("No se puede dividir entre cero")

# FUNCIÓN: Menú

def menu():

    calculadoraOBJ = Calculadora()

    acciones = {
        1: calculadoraOBJ.sumar,
        2: calculadoraOBJ.restar,
        3: calculadoraOBJ.multiplicar,
        4: calculadoraOBJ.dividir,
    }

    while True:
        try:
            opt = int(input("""
Bienvenido a la calculadora de CTR
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Mostrar Historial
6. Salir

Seleccione una opción: """))
            
        except ValueError: 
            print("Ingrese una opción válida")
            continue

        # Validar si es una opción valida

        if opt in acciones:

            try:
                a = int(input("Ingrese el número A: "))
                b = int(input("Ingrese el número B: "))
            except:
                print("=== Use solamente números enteros ===\n")
                continue

            print(f"\nEl resultado es:",acciones[opt](a,b))

        elif opt == 5:
            calculadoraOBJ.mostrarHistorial()
            input("\nAprete enter para continuar  ")

        elif opt == 6:
            print("\n=== Muchas gracias por usar mi calculadora ===\n")
            break

        else:
            print("Ingrese una opción válida ")
            continue


# Ejecutar el programa

menu()