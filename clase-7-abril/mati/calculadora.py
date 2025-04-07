calc = input("suma, resta, division o multip: ")
cont = 0

if calc == "suma":
    num = int(input("Ingresa un numero: "))
    while num != 0:
        cont = cont + num
        num = int(input("Ingresa un numero: "))
    print("Numero final(suma):", cont)
    
elif calc == "resta":
    num = int(input("Ingresa un numero: "))
    while num != 0:
        cont = cont - num
        num = int(input("Ingresa un numero: "))
    print("Numero final(resta):", cont)
    
elif calc == "division":
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))  
    print("Division:", num1 / num2)

elif calc == "multip":
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))  
    print("Multip:", num1 * num2)

else:
    print("Elije un metodo valido.")
