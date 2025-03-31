usuario = "matias"
contraseña = "micontra"

inputUsuario = input("Ingrese su nombre de usuario: ")
inputContraseña = input("Ingrese su contraseña: ")

if inputUsuario == usuario and inputContraseña == contraseña:
    print("Acceso valido, bienvenido", usuario)
else:
    print("Error: Usuario o contraseña incorrecta")
