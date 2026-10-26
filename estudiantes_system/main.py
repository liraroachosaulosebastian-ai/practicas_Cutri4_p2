from CarpetaEstudiantes import estudiantes

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
            input("\n\t...¡Acción Realizada con Éxito!...")

        else:
            input("\n\t...¡Esta Acción no pudo realizarse en este momento!...")

    def datos_estudiantes(self, tipo):

        self.borrarPantalla()

        print(f"\n--- Registrar Nuevo {tipo} ---")

        nombre = input("Introduce el nombre: ").strip()
        nota = input("Introduce la nota: ").strip()

        return nombre, nota

    def menu_estudiantes(self):

        opcion = True

        while opcion:

            self.borrarPantalla()

            opcion = self.menuAcciones("Estudiantes")

            match opcion:

                case '1':

                    nombre, nota = self.datos_estudiantes("Estudiante")

                    estudiante1 = estudiantes.Estudiantes(
                        nombre,
                        nota
                    )

                    respuesta = estudiante1.insertar()

                    self.Respuesta_sql(respuesta)

                    del estudiante1

                case '2':

                    id = input(
                        "Ingresa el ID del estudiante a eliminar: "
                    ).strip()

                    respuesta = estudiantes.Estudiantes.eliminar(id)

                    self.Respuesta_sql(respuesta)

                case '3':

                    id = input(
                        "Ingresa el ID del estudiante a modificar: "
                    ).strip()

                    nombre, nota = self.datos_estudiantes("Estudiante")

                    estudiante1 = estudiantes.Estudiantes(
                        nombre,
                        nota
                    )

                    respuesta = estudiante1.actualizar(id)

                    self.Respuesta_sql(respuesta)

                    del estudiante1

                case '4':

                    registros = estudiantes.Estudiantes.consultar()

                    if len(registros) > 0:

                        num_estudiante = 1

                        for fila in registros:

                            print(
                                f"\nEstudiante # {num_estudiante}"
                                f"\n\tID: {fila[0]}"
                                f"\n\tNombre: {fila[1]}"
                                f"\n\tNota: {fila[2]}"
                            )

                            num_estudiante += 1

                        self.esperarTecla()

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

    def main(self):

        opcion = True

        while opcion:

            self.borrarPantalla()

            print("\n--- MENU PRINCIPAL ---")
            print("1.- Estudiantes")
            print("2.- Salir")

            opcion = input(
                "Elige una opción: "
            ).strip()

            match opcion:

                case '1':

                    self.menu_estudiantes()

                case '2':

                    print("Saliendo del sistema...")

                    opcion = False

                case _:

                    input(
                        "\n ...Opción inválida, intenta de nuevo..."
                    )

if __name__ == "__main__":
    app = App()