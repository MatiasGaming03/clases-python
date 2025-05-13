import pymysql

conexion = pymysql.connect(
  user = "usuario",
  password = "contraseña",
  host = "localhost",
  database = "python"
)

print(conexion)
