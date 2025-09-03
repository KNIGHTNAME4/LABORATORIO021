# calculadora1.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División entre cero"
    return a / b

def main():
    print("Calculadora 1")
    print("Operaciones disponibles: +, -, *, /")
    
    num1 = float(input("Ingresa el primer número: "))
    operador = input("Ingresa el operador (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))
    
    if operador == "+":
        resultado = suma(num1, num2)
    elif operador == "-":
        resultado = resta(num1, num2)
    elif operador == "*":
        resultado = multiplicacion(num1, num2)
    elif operador == "/":
        resultado = division(num1, num2)
    else:
        resultado = "Operador no válido"
    
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
