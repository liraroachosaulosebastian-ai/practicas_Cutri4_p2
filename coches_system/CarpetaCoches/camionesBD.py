# from conexionBD import conexion, cursor

# class CamionesBD:
#     def __init__(self, marca, color, modelo, velocidad, potencia, plazas, eje, capacidadCarga):
#         self._marca = marca
#         self._color = color
#         self._modelo = modelo
#         self._velocidad = velocidad
#         self._potencia = potencia
#         self._plazas = plazas
#         self._eje = eje
#         self._capacidadCarga = capacidadCarga

#     def insertar(self):
#         try:
#             cursor.execute(
#                 "INSERT INTO camiones VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)",
#                 (self._marca, self._color, self._modelo, self._velocidad,
#                  self._potencia, self._plazas, self._eje, self._capacidadCarga)
#             )
#             conexion.commit()
#             return True
#         except:
#             return False

#     def consultar(self):
#         try:
#             cursor.execute("SELECT * FROM camiones")
#             return cursor.fetchall()
#         except:
#             return []

#     def eliminar(self, id):
#         try:
#             cursor.execute("DELETE FROM camiones WHERE id=%s", (id,))
#             conexion.commit()
#             return True
#         except:
#             return False

#     def actualizar(self, id):
#         try:
#             cursor.execute(
#                 "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, plazas=%s, eje=%s, capacidadCarga=%s WHERE id=%s",
#                 (self._marca, self._color, self._modelo, self._velocidad,
#                  self._potencia, self._plazas, self._eje, self._capacidadCarga, id)
#             )
#             conexion.commit()
#             return True
#         except:
#             return False

    