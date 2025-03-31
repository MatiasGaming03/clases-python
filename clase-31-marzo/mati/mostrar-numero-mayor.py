n1 = int(input("Ingrese, por favor, un primer numero: "))
n2 = int(input("Ingrese, por favor, un segundo numero: "))
n3 = int(input("Ingrese, por favor, un tercer numero: "))

if n1 > n2 and n1 > n3:
    print("El numero mas grande es el numero 1:", n1)
elif n2 > n1 and n2 > n3:
    print("El numero mas grande es el numero 2:", n2)
elif n3 > n1 and n3 > n2:
    print("El numero mas grande es el numero 3:", n3)
    
elif n1 == n2 and n2 > n3:
    print("Los numeros mas grandes son el numero 1 y 2:", n1)
elif n1 == n3 and n3> n2:
    print("Los numeros mas grandes son el numero 1 y 3:", n1)
elif n2 == n3 and n3 > n1:
    print("Los numeros mas grandes son el numero 2 y 3:", n2)
    
else:
    print("Todos los numeros son iguales:", n1)
