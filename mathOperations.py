def getSum(numberList):
    answer = 0
    for i in range(len(numberList)):
        answer = answer + numberList[i]
    return answer

def getProduct(numberList):
    answer = 1
    for i in range(len(numberList)):
        answer = answer * numberList[i]
    return answer

def getQuotient():
    try:
        while True:
            try:
                numerator = float(input("Digite el numerador: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.\n")

        while True:
            try:
                denominator = float(input("Digite el denominador: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
        
        return numerator / denominator
    except:
        return print("NULA")

def setFactorialArgument():
    while True:
        try:
            factorialArgument = int(input("Digite el numero para sacarle el factorial: "))
            if factorialArgument >= 0:
                return factorialArgument
            else:
                print("Por favor, ingrese un número mayor o igual a 0.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")

def getFactorial(factorialArgument):
    factorial = factorialArgument
    if factorialArgument == 0:
        factorial = 1
    else:
        factorial = factorial * getFactorial(factorialArgument - 1)
    return factorial

def getTable(tableNumber):
    print(f"La tabla del {tableNumber}\n")
    for i in range(10):
        print(f"{tableNumber} x {i} = {tableNumber * i}")

def getSquared(number):
    return number * number

def getCubed(number):
    return number * number * number

def getMean(numberList):
    totalSum = 0
    for i in range(len(numberList)):
        totalSum = totalSum + numberList[i]
    return totalSum / len(numberList)

def getMaxNumber(numberList):
    maximumNumber = numberList[0]
    for i in range(len(numberList)):
        if numberList[i] > maximumNumber:
            maximumNumber = numberList[i]
    return maximumNumber