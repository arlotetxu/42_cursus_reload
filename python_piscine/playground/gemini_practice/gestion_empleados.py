class ErrorSalario(Exception):
    pass


class ErrorNombre(Exception):
    pass

#=============================================================================
class Empleado:
    def __init__(self, nombre: str, salario: float) -> None:
        if not nombre or nombre.isspace():
            raise ErrorNombre("El nombre no puede estar vacío")
        self.nombre = nombre
        self.salario = salario


    @property
    def salario(self) -> float:
        return self._salario


    @salario.setter
    def salario(self, nuevo_salario: float) -> None:
        if nuevo_salario < 0:
            raise ErrorSalario("El salario no puede ser negativo")
        else:
            self._salario = nuevo_salario


    def trabajar(self) -> None:
        print(f"{self.nombre} está realizando sus tareas generales")


    def mostrar_info(self) -> str:
        return f"Nombre: {self.nombre}, Salario: {self.salario:.2f}"


#=============================================================================
class Gerente(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str) -> None:
        super().__init__(nombre, salario)
        self.departamento = departamento


    def trabajar(self) -> None:
        print(f"El gerente {self.nombre} está supervisando el departamento "
              f"{self.departamento}")


#=============================================================================
class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario: float, lenguaje: str) -> None:
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje


    def trabajar(self) -> None:
        print(f"{self.nombre} está escribiendo código en {self.lenguaje}")


#===================================MAIN======================================
if __name__ == "__main__":
    try:
        gerente_1 = Gerente("Xabier Matute",
                             -3000.00,
                             "Logistica")
    except ErrorNombre as e:
        print(f"Error de registro: {e}")
    except ErrorSalario as e:
        print(f"Error financiero: {e}")
    else:
        gerente_1.trabajar()

    try:
        desarrollador_1 = Desarrollador("Xabier Matute",
                                        2000,
                                        "C")
    except ErrorNombre as e:
        print(f"Error de registro: {e}")
    except ErrorSalario as e:
        print(f"Error financiero: {e}")
    else:
        desarrollador_1.trabajar()

    try:
        gerente_1.salario = -1500.0
    except (ErrorSalario, NameError) as error_3:
        print(error_3)

