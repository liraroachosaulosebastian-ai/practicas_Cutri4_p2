# from conexionBD import conexion, cursor

# class EstudiantesBD:
#     def __init__(self, nombre, nota):
#         self._nombre = nombre
#         self._nota = nota

#     def insertar(self):
#         try:
#             cursor.execute(
#                 "INSERT INTO estudiantes VALUES (NULL, %s, %s)",
#                 (self._nombre, self._nota)
#             )
#             conexion.commit()
#             return True
#         except Exception as e:
#             print("Error al insertar:", e)
#             return False

#     def consultar(self):
#         try:
#             cursor.execute("SELECT * FROM estudiantes")
#             return cursor.fetchall()
#         except Exception as e:
#             print("Error al consultar:", e)
#             return []

#     def eliminar(self, id):
#         try:
#             cursor.execute("DELETE FROM estudiantes WHERE id=%s", (id,))
#             conexion.commit()
#             return True
#         except Exception as e:
#             print("Error al eliminar:", e)
#             return False

#     def actualizar(self, id):
#         try:
#             cursor.execute(
#                 "UPDATE estudiantes SET nombre=%s, nota=%s WHERE id=%s",
#                 (self._nombre, self._nota, id)
#             )
#             conexion.commit()
#             return True
#         except Exception as e:
#             print("Error al actualizar:", e)
#             return False
