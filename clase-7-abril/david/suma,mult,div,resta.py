print("usted puede dividir,restar,suma,multiplicar")
o=input("elija una opcion")
n=int(input("ingrese un numero"))
if o=="suma":
    conta=0
    while n!=0:
        n=int(input("ingrese un numero"))
        conta=conta+n
    else:
        print("el resultado es:",conta)
elif o=="resta":
    conta2=0
    while n!=0:
        n=int(input("ingrese un numero"))
        conta2=n-conta2
    else:
        print("el resultado es:",conta2)
elif o=="division":
    n=int(input("ingrese un numero"))
    n2=int(input("ingrese un numero"))
    div=n/n2
    print("el resultado de la division es:",div)
elif o=="multiplicacion":
    n=int(input("ingrese un numero"))
    n2=int(input("ingrese un numero"))
    mult=n*n2
    print("el resultado de la mult es:",div)
    
    
    
