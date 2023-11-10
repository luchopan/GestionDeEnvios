import pyodbc

# Configuración de la conexión a la base de datos Access
connection = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=app\TasksDB.accdb;'
)

cursor = connection.cursor()