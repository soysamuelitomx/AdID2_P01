from dataInput import greet, showOptions, selectOption, resolveOperation, handleShutdown

print("------------------------------------------------------------------------")
print("---CALCULADORA AVANZADA---")
print("------------------------------------------------------------------------")
greet()
notShutDown = True
while notShutDown:
    print("------------------------------------------------------------------------")
    showOptions()
    print("------------------------------------------------------------------------")
    resolveOperation(selectOption())
    print("------------------------------------------------------------------------")
    notShutDown = handleShutdown()

print("Gracias :)")