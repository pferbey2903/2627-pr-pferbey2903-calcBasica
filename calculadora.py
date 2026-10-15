
def sumar(num1: float, num2: float) -> float:
    """Suma de dos números"""
    suma = num1 + num2
    return float(suma)


def restar(num1: float, num2: float) -> float:
    """Resta de dos números"""
    resta = num1 - num2
    return float(resta)


def multiplicar(num1: float, num2: float) -> float:
    """Multiplicación de dos números"""
    multiplicacion = num1 * num2
    return float(multiplicacion)


def dividir(num1: float, num2: float) -> float:
    """División de dos números"""
    division = num1 / num2
    return float(division)

def main():

    num1 = float(input("Escribe un número: "))
    num2 = float(input("Escribe otro número: "))

    print(f"La suma es: {sumar(num1, num2)}")
    print(f"La resta es: {restar(num1, num2)}")
    print(f"La multiplicación es: {multiplicar(num1, num2)}")
    print(f"La división es: {dividir(num1, num2)}")

if __name__ == "__main__":
    main()