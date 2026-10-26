import mysql.connector

try:
    conexion=mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='',
    database='bd_estudiantes'
    )
    cursor=conexion.cursor(buffered=True)
except:
    print(f" ... !Por el momento no es posible conectarse con la base de datos intentelo mas tarde! ... ")


def insertar(self):
        try:
            cursor.execute("incert into estudiantes values (NULL, %s, %s,)",(self._nombre ,self._nota))
            conexion.commit()
            return True
        except:
            return False
def consultar(self):
        try:
            cursor.execute("select * from estudiantes")
            return cursor.fetchall()
        except:
            return[]
        
def eliminar(self, id):
        try:
            cursor.execute("delete from estudiantes where id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False
def actualizar(self):
        try:
            cursor.execute(" updatecoches set nombre=%s,nota=%s"(self._nombre,self._nota,))
            return True
        except:
            return False
