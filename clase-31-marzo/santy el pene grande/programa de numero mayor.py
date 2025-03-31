a= int(input("introduzca un numero por favor"))
b= int(input("introduzca un numero por favor"))
c= int(input("introduzca un numero por favor"))
if a>b and a>c:
    print("el numero mayor es",a)
elif a==b and a>c:
    print("el numero mayor es",a)
elif a==c and a>b:
    print("el numero mayor es",a)
elif b>a and b>c:
    print("el numero mayor es",b)
elif b==c and b>a:
    print("el numero mayor es",b)
elif c>a and c>b:
    print("el numero mayor es",c)
else:
    print("los numeros son iguales")
