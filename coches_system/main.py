from CarpetaCoches import coches

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("Presiona una tecla para continuar...")

    def menuAcciones(self, tipo):
        print(f"\n--- Menu de {tipo} ---")
        opcion = input(
            "1.- Agregar\n"
            "2.- Borrar\n"
            "3.- Modificar\n"
            "4.- Mostrar\n"
            "5.- Regresar\n"
            "Elige una opción: "
        ).strip()
        return opcion

    def Respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t...¡Accion Realizada con Exito!...")

        else:
            input("\n\t...¡Esta Accion no pudo realizarse en este momento!...")

    def datos_coches(self, tipo):
        print(f"\n--- Registrar Nuevo {tipo} ---")

        cochecitos = {}

        cochecitos['marca'] = input("Introduce la marca: ").strip()
        cochecitos['color'] = input("Introduce el color: ").strip()
        cochecitos['modelo'] = input("Introduce el modelo: ").strip()
        cochecitos['velocidad'] = int(input("Introduce la velocidad: "))
        cochecitos['potencia'] = int(input("Introduce la potencia: "))
        cochecitos['plazas'] = int(input("Introduce el número de plazas: "))

        return cochecitos

    def datos_camiones(self, tipo):
        print(f"\n--- Registrar Nuevo {tipo} ---")

        marca = input("Introduce la marca: ").strip()
        color = input("Introduce el color: ").strip()
        modelo = input("Introduce el modelo: ").strip()
        velocidad = int(input("Introduce la velocidad: "))
        potencia = int(input("Introduce la potencia: "))
        plazas = int(input("Introduce el número de plazas: "))
        eje = int(input("Introduce el número de ejes: "))
        capacidad = int(input("Introduce la capacidad de carga: "))

        return marca, color, modelo, velocidad, potencia, plazas, eje, capacidad

    # ==========================
    # MENU COCHES
    # ==========================

    def menu_coches(self):
        opcion = True

        while opcion:
            self.borrarPantalla()

            opcion = self.menuAcciones("Coches")

            match opcion:

                case '1':

                    datos = self.datos_coches("Coche")

                    coche1 = coches.Coches(
                        datos['marca'],
                        datos['color'],
                        datos['modelo'],
                        datos['velocidad'],
                        datos['potencia'],
                        datos['plazas']
                    )

                    respuesta = coche1.insertar()

                    self.Respuesta_sql(respuesta)

                    del coche1

                case '2':

                    id = input(
                        "Ingresa el ID del coche a eliminar: "
                    ).strip()

                    respuesta = coches.Coches.eliminar(id)

                    self.Respuesta_sql(respuesta)

                case '3':

                    id = input(
                        "Ingresa el ID del coche a modificar: "
                    ).strip()

                    datos = self.datos_coches("Coche")

                    coche1 = coches.Coches(
                        datos['marca'],
                        datos['color'],
                        datos['modelo'],
                        datos['velocidad'],
                        datos['potencia'],
                        datos['plazas']
                    )

                    respuesta = coche1.actualizar(id)

                    self.Respuesta_sql(respuesta)

                    del coche1

                case '4':

                    registros = coches.Coches.consultar()

                    if len(registros) > 0:

                        num_coches = 1

                        for fila in registros:

                            print(
                                f"\nCoche # {num_coches}"
                                f"\n\tID: {fila[0]}"
                                f"\n\tMarca: {fila[1]}"
                                f"\n\tColor: {fila[2]}"
                                f"\n\tModelo: {fila[3]}"
                                f"\n\tVelocidad: {fila[4]}"
                                f"\n\tPotencia: {fila[5]}"
                                f"\n\tPlazas: {fila[6]}"
                            )

                            num_coches += 1

                    else:

                        print(
                            "\n\n\t¡No existen datos a mostrar por el momento!"
                        )

                    self.esperarTecla()

                case '5':

                    opcion = False

                case _:

                    input(
                        "\n\t ... Opción inválida, vuelve a intentarlo ..."
                    )

    # ==========================
    # MENU CAMIONES
    # ==========================

    def menu_camiones(self):

        opcion = True

        while opcion:

            self.borrarPantalla()

            opcion = self.menuAcciones("Camiones")

            match opcion:

                case '1':

                    marca, color, modelo, velocidad, potencia, plazas, eje, capacidad = self.datos_camiones("Camión")

                    camion1 = coches.Camiones(
                        marca,
                        color,
                        modelo,
                        velocidad,
                        potencia,
                        plazas,
                        eje,
                        capacidad
                    )

                    respuesta = camion1.insertar()

                    self.Respuesta_sql(respuesta)

                    del camion1

                case '2':

                    id = input(
                        "Ingresa el ID del camión a eliminar: "
                    ).strip()

                    respuesta = coches.Camiones.eliminar(id)

                    self.Respuesta_sql(respuesta)

                case '3':

                    id = input(
                        "Ingresa el ID del camión a modificar: "
                    ).strip()

                    marca, color, modelo, velocidad, potencia, plazas, eje, capacidad = self.datos_camiones("Camión")

                    camion1 = coches.Camiones(
                        marca,
                        color,
                        modelo,
                        velocidad,
                        potencia,
                        plazas,
                        eje,
                        capacidad
                    )

                    respuesta = camion1.actualizar(id)

                    self.Respuesta_sql(respuesta)

                    del camion1

                case '4':

                    registros = coches.Camiones.consultar()

                    if len(registros) > 0:

                        num_camiones = 1

                        for fila in registros:

                            print(
                                f"\nCamión # {num_camiones}"
                                f"\n\tID: {fila[0]}"
                                f"\n\tMarca: {fila[1]}"
                                f"\n\tColor: {fila[2]}"
                                f"\n\tModelo: {fila[3]}"
                                f"\n\tVelocidad: {fila[4]}"
                                f"\n\tPotencia: {fila[5]}"
                                f"\n\tPlazas: {fila[6]}"
                                f"\n\tEjes: {fila[7]}"
                                f"\n\tCapacidad: {fila[8]}"
                            )

                            num_camiones += 1

                    else:

                        print(
                            "\n\n\t¡No existen datos a mostrar por el momento!"
                        )

                    self.esperarTecla()

                case '5':

                    opcion = False

                case _:

                    input(
                        "\n\t ... Opción inválida, vuelve a intentarlo ..."
                    )

    # ==========================
    # MAIN
    # ==========================

    def main(self):

        opcion = True

        while opcion:

            self.borrarPantalla()

            print("\n--- MENU PRINCIPAL ---")
            print("1.- Coches")
            print("2.- Camiones")
            print("3.- Salir")

            opcion = input(
                "Elige una opción: "
            ).strip()

            match opcion:

                case '1':
                    self.menu_coches()

                case '2':
                    self.menu_camiones()

                case '3':
                    print("Saliendo del sistema...")
                    opcion = False

                case _:
                    input(
                        "\n ...Opción inválida, intenta de nuevo..."
                    )

if __name__ == "__main__":
    app = App()