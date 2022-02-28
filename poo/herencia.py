class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre.title()
        self._apellido = apellido.title()
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre.title()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido.title()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError('La edad no puede ser negativa')
        self._edad = edad


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, salario):
        super().__init__(nombre, apellido, edad)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        if salario < 0:
            raise ValueError('El salario no puede ser negativo')
        self._salario = salario


if __name__ == '__main__':
    # Instanciar un objeto de la clase Empleado
    empleado = Empleado('juan', 'perez', 30, 1000)
    print(empleado.nombre)
    print(empleado.apellido)
    print(empleado.edad)
    print(empleado.salario)