# calculadora3.py
# Esta es la tercera calculadora del proyecto (creada por Persona 1).
# Permite sumar, restar, multiplicar y dividir.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

if __name__ == "__main__":
    print("=== Calculadora 3 ===")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")

    opcion = int(input("Elige una opción: "))
    x = float(input("Ingresa el primer número: "))
    y = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print("Resultado:", suma(x, y))
    elif opcion == 2:
        print("Resultado:", resta(x, y))
    elif opcion == 3:
        print("Resultado:", multiplicacion(x, y))
    elif opcion == 4:
        print("Resultado:", division(x, y))
    else:
        print("Opción no válida")
