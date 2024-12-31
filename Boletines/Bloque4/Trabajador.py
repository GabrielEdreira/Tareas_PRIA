import datetime

class Trabajador:
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, NumeroColegiado:int = None):
        """Constructor

        Args:
            NIF (str): NIF del Trabajador
            Nombre (str): Nombre del Trabajador
            FechaNacimiento (datetime): Fecha de Nacimiento del Trabajador
            Sexo (str): Sexo del Trabajador
            NumeroColegiado (int, optional): Numero de colegiado del Trabajador. Defaults to None.
        """        
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
        """Método get para NumeroColegiado

        Returns:
            int: Número de Colegiado de un Trabajador
        """        
        return self._NumeroColegiado
    @property
    def set_NumeroColegiado(self, nuevo_NumeroColegiado):
        """Método set de NumeroColegiado

        Args:
            nuevo_NumeroColegiado (int): Número de colegiado de un trabajador

        Raises:
            ValueError: Lanza error si el valor a settear es nulo
        """        
        if not nuevo_NumeroColegiado:
            raise ValueError("El número de colegiado no puede estar vacío.")
        self._NumeroColegiado = nuevo_NumeroColegiado


class Medico(Trabajador):
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, Especialidad:str, FechaInicioCarrera:datetime, NumeroColegiado:float = None):
        """Constructor
        """           
        super().__init__(NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado)
        self._Especialidad = Especialidad
        self._FechaInicioCarrera = FechaInicioCarrera

    def getNumeroAnhos(self):
        """Método para la obtención del número de años que lleva ejerciciendo un médico

        Returns:
            int: Número de años ejerciciendo
        """        
        current_date = datetime.datetime.now()
        date = self._FechaInicioCarrera
        
        dif = (current_date.year - date.year)
        if (current_date.month, current_date.day) < (date.month, date.day):
            dif -= 1
        return dif
    
    def __str__(self):
        """Método str sobreescrito

        Returns:
            str: Una cadena con una estructura en concreto
        """   
        colegiado = self._NumeroColegiado if self._NumeroColegiado else ""
        return (f"Médico: {self._Nombre} [{self._NIF}], Sexo: {self._Sexo}, " +
                f"Fecha de nacimiento: {self._FechaNacimiento.strftime('%d/%m/%Y')}, " +
                f"Especialidad: {self._Especialidad}, Fecha inicio carrera: {self._FechaInicioCarrera.strftime('%d/%m/%Y')}" +
                f", Número de colegiado: {colegiado}")


class Enfermera(Trabajador):
    _PersonasCargo = 0
    def __init__(self, NIF:str, Nombre:str, FechaNacimiento:datetime, Sexo:str, AreaTrabajo:str, PersonasCargo:int, NumeroColegiado:float = None):
        """Constructor
        """        
        super().__init__(NIF, Nombre, FechaNacimiento, Sexo, NumeroColegiado)
        self._AreaTrabajo = AreaTrabajo
        self._PersonasCargo = PersonasCargo

    def getPersonasCargo(self):
        """Método para la obtención del parámetro PersonasCargo de una enfermera

        Returns:
            int: Número de personas a cargo de la enfermera
        """
        return self._PersonasCargo

    def AñadirPersonaCargo(self):
        """Este método podría gestionar personas en si pero por ahora no
        """        
        # NIF = input("¿NIF? ")
        # Nombre = input("¿Nombre? ")

        # self._PersonasCargo[NIF] = Persona(NIF, Nombre)
        self._PersonasCargo += 1
        print(f"Se ha añadido una persona. {self._PersonasCargo}\n")

    def BorrarPersonaCargo(self):
        """Este método podría gestionar personas en si pero por ahora no
        """
        # NIF = input("¿NIF? ")

        # if (self._PersonasCargo_.keys().__contains__(NIF)):
        #     self._PersonasCargo_.pop(NIF)
        self._PersonasCargo -= 1
        print(f"Se ha eliminado una persona. {self._PersonasCargo}\n")

    def __str__(self):
        """Método str sobreescrito

        Returns:
            str: Una cadena con una estructura en concreto
        """        
        colegiado = self._NumeroColegiado if self._NumeroColegiado else ""
        return (f"Enfermera: {self._Nombre} [{self._NIF}], Sexo: {self._Sexo}, " +
                f"Fecha de nacimiento: {self._FechaNacimiento.strftime('%d/%m/%Y')}, " +
                f"Área de trabajo: {self._AreaTrabajo}, Personas a cargo: {self._PersonasCargo}" +
                f", Número de colegiado: {colegiado}")


class Persona():
    def __init__(self, NIF, Nombre):
        self.NIF = NIF
        self.Nombre = Nombre