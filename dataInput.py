from mathOperations import getSum, getProduct, getQuotient, getFactorial, setFactorialArgument, getTable, getSquared, getCubed, getMean, getMaxNumber

def greet():
    userName = input("Bienvenido, digite su nombre: ")
    print(f"------Hola {userName}------\n")
    print("------Esta es su calculadora :D------")

def handleShutdown():
    shouldExit = input("Desea salir del programa (s/n)? ")
    if shouldExit.lower() == 's':
        return False
    else:
        return True 

def showOptions():
    print("---------------------------------------------------------------------------------")
    print("------MENU PRINCIPAL------")
    print("1. Suma de n números;")
    print("2. Producto de n números;")
    print("3. División de 2 números;")
    print("4. Calcular el factorial de un número;")
    print("5. Impresión en pantalla de las tablas de multiplicar (del 1 al 10, permitiendo al usuario seleccionar el número de tabla).")
    print("6. Cálculo del cuadrado.")
    print("7. Calculo del cubo de un número introducido por teclado.")
    print("8. Determinación del promedio (media) de una serie de números. El programa debe dejar de aceptar valores cuando se indique el valor -1.")
    print("9. Acepte 'n' cantidad de números enteros e imprima los valores máximo y mínimo, con el total de valores que se introdujeron por teclado.")
    print("10. Apagar.")
    print("---------------------------------------------------------------------------------")

def selectOption():
    optionSelected = input("Seleccione su operación: ")
    return optionSelected

def resolveOperation(optionSelected):
    if optionSelected == '1':
        print("---Suma de n números---")
        print("Ingrese los números para sumar:")
        print(f"La respuesta es: {getSum(addNumbers())}")
    elif optionSelected == '2':
        print("---Producto de n números---")
        print("Ingrese los números para multiplicar:")
        print(f"La respuesta es: {getProduct(addNumbers())}")
    elif optionSelected == '3':
        print("---El Cociente entre dos números---")
        print("Ingrese los números para dividir:")
        print(f"La respuesta es: {getQuotient()}")
    elif optionSelected == '4':
        print("---El factorial de un número---")
        print("Ingrese el número para obtener su factorial")
        print(f"La respuesta es: {getFactorial(setFactorialArgument())}")
    elif optionSelected == '5':
        print("---La tabla de un número---")
        print("Ingrese el número para mostrar su tabla de multiplicar:")
        getTable(setRealNumber())
    elif optionSelected == '6':
        print("---El cuadrado de un número---")
        print("Ingrese el número y su potencia para:")
        print(f"La respuesta es: {getSquared(setRealNumber())}")
    elif optionSelected == '7':
        print("---El cubo de un número---")
        print("Ingrese el número y su potencia para:")
        print(f"La respuesta es: {getCubed(setRealNumber())}")
    elif optionSelected == '8':
        print("---La media de n números---")
        print("Ingrese la cantidad de números para sacar su media:")
        print(f"La respuesta es: {getMean(addNumbers())}")
    elif optionSelected == '9':
        print("---El mayor de n números---")
        print("Ingrese la cantidad de números para obtener cuál es el mayor de todos:")
        print(f"La respuesta es: {getMaxNumber(addNumbers())}")
    else:
        return

def setRealNumber():
    while True:
        try:
            realNumber = float(input("Digite el número para su operación: "))
            return realNumber
        except ValueError:
            print("Por favor, ingrese un número real.\n")

def setQuantity():
    while True:
        try:
            quantity = int(input("Digite la cantidad de números: "))
            if quantity >= 1:
                return quantity
            else:
                print("Por favor, ingrese un número mayor o igual a 1.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")

def addNumbers():
    numberType = input("¿Qué tipo de números desea ingresar? (real, natural): ").strip().lower()
    
    while numberType not in ["real", "natural"]:
        print("Por favor, ingrese 'real' o 'natural'.")
        numberType = input("¿Qué tipo de números desea ingresar? (real, natural): ").strip().lower()
    
    while True:
        try:
            numbersQuantity = int(input("¿Cuántos números desea ingresar? "))
            if numbersQuantity >= 1:
                break
            else:
                print("Por favor, digite un numero valido")
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad de números.")
    
    numberList = []
    
    for i in range(numbersQuantity):
        while True:
            try:
                if numberType == "real":
                    number = float(input(f"Digite el número {i + 1}: "))
                else:
                    number = int(input(f"Digite el número {i + 1}: "))
                    if number < 0:
                        print("Por favor, ingrese un número natural (mayor o igual a 0).")
                        continue

                numberList.append(number)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    return numberList