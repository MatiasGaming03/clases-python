num1 = int(input("Introduzca, por favor, un numero: "))
num2 = int(input("Introduzca, por favor, otro numero: "))

tipo_calculo = input("suma, resta, multiplicar o dividir?: ")
if tipo_calculo == "suma":
    res = num1 + num2
    print("El resultado de la suma es:", res)
elif tipo_calculo == "resta":
    res = num1 - num2
    print("El resultado la resta es:", res)
elif tipo_calculo == "multiplicar":
    res = num1 * num2
    print("El resultado de la multplicacion es:", res)
elif tipo_calculo == "dividir":
    res = num1 / num2
    print("El resultado de la division es:", res)
else:
    print("ERROR: Selecciona un metodo valido.")