n1=int(input("ingrese un numero:"))
n2=int(input("ingrese un numero:"))
n3=int(input("ingrese un numero:"))
if n1>n2 and n1>n3:
    print("el numero mayor es:",n1)
elif n2>n1 and n2>n3:
    print("el numero mayor es:",n2)
elif n3>n1 and n3>n2:
    print("el numero mayor es:",n3)
elif n1==n2 and n1>n3:
    print("los numeros mayores son el N*1 y el N*2")
elif n1==n3 and n1>n2:
    print("los numeros mayore son el N*1 y el N*3")
elif n1==n2 and n2==n3:
    print("los numeros son iguales")
elif n2==n3 and n2>n1:
    print("los numeros mayores son el N*2 y el N*3")    
    
