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
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, Especialidad:str, FechaInicioCarrera:datetime, NumeroColegiado:float = None):
        super().__init__(NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado)
        self._Especialidad = Especialidad
        self._FechaInicioCarrera = FechaInicioCarrera

    def getNumeroAnhos(self):
        current_date = datetime.datetime.now()
        date = self._FechaInicioCarrera
        
        dif = (current_date.year - date.year)
        if (current_date.month, current_date.day) < (date.month, date.day):
            dif -= 1
        return dif
    
    def __str__(self):
        colegiado = self._NumeroColegiado if self._NumeroColegiado else ""
        return (f"Médico: {self._Nombre} [{self._NIF}], Sexo: {self._Sexo}, " +
                f"Fecha de nacimiento: {self._FechaNacimiento.strftime('%d/%m/%Y')}, " +
                f"Especialidad: {self._Especialidad}, Fecha inicio carrera: {self._FechaInicioCarrera.strftime('%d/%m/%Y')}" +
                f", Número de colegiado: {colegiado}")


class Enfermera(Trabajador):
    _PersonasCargo = 0
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, AreaTrabajo:str, PersonasCargo:int, NumeroColegiado:float = None):
        super().__init__(NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado)
        self._AreaTrabajo = AreaTrabajo
        self._PersonasCargo = PersonasCargo

    def getPersonasCargo(self):
        return self._PersonasCargo

    """
        Falta Modificarlo para empezar a gestionar personas realmente
    """
    def AñadirPersonaCargo(self):
        # NIF = input("¿NIF? ")
        # Nombre = input("¿Nombre? ")

        # self._PersonasCargo[NIF] = Persona(NIF, Nombre)
        self._PersonasCargo += 1
        print(f"Se ha añadido una persona. {self._PersonasCargo}\n")

    """
        Falta Modificarlo para empezar a gestionar personas realmente
    """
    def BorrarPersonaCargo(self):
        # NIF = input("¿NIF? ")

        # if (self._PersonasCargo_.keys().__contains__(NIF)):
        #     self._PersonasCargo_.pop(NIF)
        self._PersonasCargo -= 1
        print(f"Se ha eliminado una persona. {self._PersonasCargo}\n")

    def __str__(self):
        colegiado = self._NumeroColegiado if self._NumeroColegiado else ""
        return (f"Enfermera: {self._Nombre} [{self._NIF}], Sexo: {self._Sexo}, " +
                f"Fecha de nacimiento: {self._FechaNacimiento.strftime('%d/%m/%Y')}, " +
                f"Área de trabajo: {self._AreaTrabajo}, Personas a cargo: {self._PersonasCargo}" +
                f", Número de colegiado: {colegiado}")


class Persona():
    def __init__(self, NIF, Nombre):
        self.NIF = NIF
        self.Nombre = Nombre