import datetime

class Trabajador:
    def __init__(self, NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado = None):
        self._NIF = NIF
        self._Nombre = Nombre
        self._FechaNacimiento = FechaNacimiento
        self._Sexo = Sexo
        self._NumeroColegiado = NumeroColegiado

    @property
    def get_NIF(self):
        return self._NIF
    @property
    def set_NIF(self, nuevo_NIF):
        if not nuevo_NIF:
            raise ValueError("El NIF no puede estar vacío.")
        self._NIF = nuevo_NIF

    @property
    def get_Nombre(self):
        return self._Nombre
    @property
    def set_Nombre(self, nuevo_Nombre):
        if not nuevo_Nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._Nombre = nuevo_Nombre
    
    @property
    def get_Sexo(self):
        return self._Sexo
    @property
    def set_Sexo(self, nueva_Sexo):
        if not nueva_Sexo:
            raise ValueError("La Fecha de Nacimiento no puede estar vacía.")
        self._Sexo = nueva_Sexo

    @property
    def get_NumeroColegiado(self):
        return self._NumeroColegiado
    @property
    def set_NumeroColegiado(self, nuevo_NumeroColegiado):
        if not nuevo_NumeroColegiado:
            raise ValueError("El número de colegiado no puede estar vacío.")
        self._NumeroColegiado = nuevo_NumeroColegiado


class Medico(Trabajador):
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, AreaTrabajo:str, PersonasCargo:int, NumeroColegiado:float = None):
        super.__init__(NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado)
        self._AreaTrabajo = AreaTrabajo
        self._PersonasCargo = PersonasCargo


    def __str__(self):
        return f"{self._Nombre}[{self._NIF}] {self._Sexo} {{ Area:{self._AreaTrabajo}, Nº Personas:{self._PersonasCargo} }} {self._FechaNacimiento}"

class Enfermera(Trabajador):
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, Especialidad:str, FechaInicioCarrera:int, NumeroColegiado:float = None):
        super.__init__(NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado)
        self._Especialidad = Especialidad
        self._FechaInicioCarrera = FechaInicioCarrera


    def __str__(self):
        return f" {self._Nombre}[{self._NIF}] {self._Sexo} {{ Area:{self._Especialidad}, Fecha Inicio Carrera:{self._FechaInicioCarrera} }} {self._FechaNacimiento} \n"