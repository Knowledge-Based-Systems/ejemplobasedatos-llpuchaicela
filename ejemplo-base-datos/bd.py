#Crear base de datos

# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="6537537.",
database = "practicaDatos"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
def crear_database():
    cursorObject.execute("CREATE DATABASE practicaDatos")
    print("\nBase de datos creada con exito\n")

def crear_tabla():
    print("\nTabla creada\n")

    # creaccion de tabla
    sql = """CREATE TABLE DOCENTES (
                   CEDULA VARCHAR(11)NOT NULL PRIMARY KEY,
                   NAME VARCHAR(20) NOT NULL,
                   LAST_NAME VARCHAR(50),
                   DIRECCION VARCHAR(100),
                   TELEFONO VARCHAR(20),
                   AGE INT
                   )"""
    # table created
    cursorObject.execute(sql)

# Insercion de un dato a la tabla
def insertar_Un_Dato():
    print("\nDato ingresado con exito\n")
    sql = "INSERT INTO DOCENTES (CEDULA,NAME,LAST_NAME,DIRECCION,TELEFONO,AGE)\
    VALUES (%s, %s, %s, %s, %s, %s)"
    val =[("1900032231","Rosario","Ocampo","Punzara", "0977362516","22")]
    cursorObject.executemany(sql, val)

# Insercion de varios datos a la tabla
def insertar_Varios_datos():
    print("\nTodos los datos fueron ingresados correctamente\n")
    sql = "INSERT INTO DOCENTES (CEDULA,NAME,LAST_NAME,DIRECCION,TELEFONO,AGE)\
    VALUES (%s, %s, %s, %s, %s, %s)"
    val = [("1103847263", "Fabricio", "Acaro", "Buenos Aires", "0866735245","37"),
            ("1728364715", "Roberto", "Romero", "Argentina y uruguay", "0953625142","64"),
            ("1955361927", "Maria", "Calva", "Motupe", "0998362525","54"),
            ("1109811234", "Carlos", "Abad", "Yanzatza", "0877253662","25")]    
    cursorObject.executemany(sql, val)

#Consulta de toda la tabla
def consultaTablaCompleta():
    print("\nConsulta de tabla completa\n")
    query = "SELECT * FROM DOCENTES"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    for i in myresult:
        print(i)


# Actualizar un dato de la tabla 
def actualizar_Undato():
    print("\nDato actualizado\n")
    query = """UPDATE DOCENTES SET CEDULA = 1103847203 WHERE CEDULA ='1103847263'"""
    cursorObject.execute(query)
    dataBase.commit()

# Consulta con WHERE
def consultasWhere():
    print("\nConsulta con clausula where\n")
    query = "SELECT * FROM DOCENTES where AGE >=50"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    for x in myresult:
        print(x)

def consultaOrderBy():
    print("\nConsulta con orders BY\n")
    query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    for x in myresult:
        print(x)
def eliminarDato():
    print("\nDato eliminado\n")

    query = "DELETE FROM DOCENTES WHERE TELEFONO = '0977362516'"
    cursorObject.execute(query)
    dataBase.commit()
#Invocar funciones
# crear_database()
# crear_tabla()
insertar_Un_Dato()
insertar_Varios_datos()
consultaTablaCompleta()
actualizar_Undato()
consultasWhere()
eliminarDato()
consultaTablaCompleta()



# disconnecting from server
dataBase.close()



