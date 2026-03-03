# Clases

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar (self,a,b):
        return a + b

    def restar (self, a,b):
        return a - b

    def multiplicar (self, a,b):
        return a * b

    def dividir (self, a,b):
        if  b != 0:
            return a // b
        else:
            print("No se puede dividir entre cero")

    def mostrarResultado (self):
        return self.resultado

# Funciones

# FUN: Menú

def menu():

    calculadoraOBJ = Calculadora()

    acciones = {
        1: calculadoraOBJ.sumar,
        2: calculadoraOBJ.restar,
        3: calculadoraOBJ.multiplicar,
        4: calculadoraOBJ.dividir
    }

    while True:
        try:
            opt = int(input("""
Bienvenido a la calculadora de CTR
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver historial
6. Borrar historial
7. Salir

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

        else:
            print("Ingrese una opción válida ")
            continue


# Ejecutar el programas

menu()

# TEST: Llamado al objeto

Calcu = Calculadora()

print(Calcu.dividir(10,2))