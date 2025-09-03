# calculadora2_persona1.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def main():
    print("Calculadora 2 - Persona 1")
    print("Opciones: +, -, *, /")
    
    num1 = float(input("Ingresa tu primer número: "))
    operador = input("Ingresa el operador: ")
    num2 = float(input("Ingresa tu segundo número: "))
    
    if operador == "+":
        resultado = sumar(num1, num2)
    elif operador == "-":
        resultado = restar(num1, num2)
    elif operador == "*":
        resultado = multiplicar(num1, num2)
    elif operador == "/":
        resultado = dividir(num1, num2)
    else:
        resultado = "Operador inválido"
    
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
