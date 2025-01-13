import Trabajador
import datetime

class Clinica():
    _Medicos_ = dict()
    _Enfermeras_ = dict()

    def __init__(self):
        """Constructor
        """
        pass

    @property
    def get_Medicos(self):
        """Método get de los médicos

        Returns:
            list(Trabajador.Medico): Lista de médicos
        """        
        return self._Medicos_
    def print_Medicos(self):
        """Imprime solo los médicos de la clínica
        """        
        aux = self._Medicos_.items()
        print(" -------- Clínica: -------- ")

        if (len(aux) == 0):
            print("   No hay médicos ")

        for _, medico in aux:
            print(f" - {medico}")
        print(" --------------------------\n")
    
    def insert_Medico(self, nuevoMedico:Trabajador.Medico):
        """Método para la inserción de una medico en una clínica

        Args:
            nuevoMedico (Trabajador.Medico): Medico a insertar

        Raises:
            ValueError: Lanza un error si el parametro es núlo, es decir, tiene un formato erroneo
        """
        if not nuevoMedico:
            raise ValueError("El médico no puede ser inválido.")
        if self._Medicos_.keys().__contains__(nuevoMedico.getNIF()):
            raise ValueError("El médico ya existe.")
        
        self._Medicos_[nuevoMedico.get_NIF()] = nuevoMedico
        
    def delete_Medico(self, NIF_Medico:str):
        """Método para el borrado de una medico en una clínica

        Args:
            NIF_Medico (str): NIF de la medico a eliminar

        Raises:
            ValueError: Lanza un error si los parametros de búsqueda tienen un formato erroneo
        """
        if not NIF_Medico:
            raise ValueError("El NIF del médico no puede ser vacío.")
        if not self._Medicos_.keys().__contains__(NIF_Medico):
            raise ValueError("No existe ese médico.")
        
        self._Medicos_.pop(NIF_Medico)

    @property
    def get_Enfermeras(self):
        """Método get de Enfermeras

        Returns:
            list(Trabajador.Enfermera): Lista de enfermeras en la clínica
        """
        return self._Enfermeras_.items()
    def print_Enfermeras(self):
        """Imprime por pantalla solo las enfermeras
        """
        aux = self._Enfermeras__.items()
        print(" -------- Clínica: -------- ")

        if (len(aux) == 0):
            print("   No hay enfermeras ")

        for _, medico in aux:
            print(f" - {medico}")
        print(" --------------------------\n")
    
    def insert_Enfermera(self, nuevaEnfermera:Trabajador.Enfermera):
        """Método para la inserción de una enfermera en una clínica

        Args:
            nuevaEnfermera (Trabajador.Enfermera): Enfermera a insertar

        Raises:
            ValueError: Lanza un error si el parametro es núlo, es decir, tiene un formato erroneo
        """
        if not nuevaEnfermera:
            raise ValueError("La enfermera no puede ser inválida.")
        if self._Enfermeras_.keys().__contains__(nuevaEnfermera.getNIF()):
            raise ValueError("La enfermera ya existe.")
        
        self._Enfermeras_[nuevaEnfermera.get_NIF()] = nuevaEnfermera
        
    def delete_Enfermera(self, NIF_Enfermera:str): 
        """Método para el borrado de una enfermera en una clínica

        Args:
            NIF_Enfermera (str): NIF de la enfermera a eliminar

        Raises:
            ValueError: Lanza un error si los parametros de búsqueda tienen un formato erroneo
        """
        if not NIF_Enfermera:
            raise ValueError("El NIF de la enfermera no puede ser vacío.")
        if not self._Enfermeras_.keys().__contains__(NIF_Enfermera):
            raise ValueError("No existe esa enferemera.")
        
        self._Enfermeras_.pop(NIF_Enfermera)
    
    
    def AñadirTrabajadorAuto(self, NIF:str, Nombre:str, FechaNac:datetime, Sexo:str, optional1:str, optional2:any, option:str, NumeroColegiado:int = None) -> None:
        """Método para crear un trabajador de manera directa
        
        Args:
            NIF (str): El NIF de un trabajador
            Nombre (str): El nombre de un trabajador
            FechaNacimiento (datetime): La fecha de nacimiento de un trabajador
            optional1 (str): Puede ser la especialidad de un médico o el area de una enfermera.
            optional2 (datetime, str): Puede ser la fecha de carrera de un médico o el número de personas de una enfermera
            option (str): La opción depende de ser Médico, 1, o Enfermera, 2.
            NumeroColegiado (float, optional): Número de colegiado del trabajador. Defaults to None.
        """             
        match(option):
            case "1":
                self._Medicos_[NIF] = Trabajador.Medico(NIF, Nombre, FechaNac, Sexo, optional1, optional2, NumeroColegiado)

            case "2":
                self._Enfermeras_[NIF] = Trabajador.Enfermera(NIF, Nombre, FechaNac, Sexo, optional1, optional2, NumeroColegiado)                 
    def AñadirTrabajador(self) -> None:
        """Método para la creación de Trabajadores mediante la inserción de un usuario
        """        
        aux = None
        while(aux != "Medico" and aux != "Enfermera"):
            aux = input("¿Medico o Enfermera? ")
        
            if (aux != "Medico" and aux != "Enfermera"):
                print("Valor inválido.\n")
        
        NIF = input("¿NIF? ")
        Nombre = input("¿Nombre? ")
        FechaNac = input("¿Fecha de Nacimiento (dd/MM/yyyy)? ")
        NumeroColegiado = input("¿Número de colegiado (ENTER para dejarlo en blanco)? ")
        Sexo = input("¿Sexo (H/M)? ")

        print()
        match(aux):
            case "Medico":
                Especialidad = input("¿Especialidad? ")
                FechaCarrera = input("¿Cuando empezó a ejercer (dd/MM/yyyy)? ")

                self._Medicos_[NIF] = Trabajador.Medico(NIF, Nombre, FechaNac, Sexo, Especialidad, FechaCarrera, NumeroColegiado)

            case "Enfermera":
                Area = input("¿Area? ")
                NumPersonas = input("¿Nº Personas? ")

                self._Enfermeras_[NIF] = Trabajador.Enfermera(NIF, Nombre, FechaNac, Sexo, Area, NumPersonas, NumeroColegiado)

    def BorrarTrabajador(self):
        """Método para el borrado de un trabajador
        """        
        NIF = input("¿NIF? ")

        if NIF in self._Medicos_.keys(): 
            self._Medicos_.pop(NIF)
        elif NIF in self._Enfermeras_.keys(): 
            self._Enfermeras_.pop(NIF)
        else:
            print("No existen el Trabajador.\n")


    def GetTrabajador(self, option:str = None) -> Trabajador:
        """Método para la obtención de un trabajador, si el atributo "option" está cubierto con una string que sea 
           "Medico" o "Enfermera" entonces filtrará por esos trabajadores, en cualquier caso se ignorará

        Args:
            option (str, optional): Filtro entre médicos y enfermeras. Defaults to None.

        Returns:
            Trabajador: Trabajador encontrado con el NIF coincidente
        """        
        NIF = input("¿NIF? ")

        trabajador = None
        if NIF in self._Medicos_.keys() and (option == "Medico" or option == None): 
            trabajador = self._Medicos_[NIF]
        elif NIF in self._Enfermeras_.keys() and (option == "Enfermera" or option == None): 
            trabajador = self._Enfermeras_[NIF]
        else:
            print("No se encuentra el trabajador.\n")
            return

        return trabajador
    
    def printTrabajadores(self):
        """Muestra todos los trabajadores de la clínica
        """        
        
        trabajadores = list(self._Medicos_.values()) + list(self._Enfermeras_.values())

        print(" -------- Clínica: -------- ")

        if (len(trabajadores) == 0):
            print("    No hay trabajadores ")

        #print(trabajadores)
        for trabajador in trabajadores:
            print(f" - {trabajador}")
        print(" --------------------------\n")
        
        
    def Inicializar(self, ok:bool = True):
        """Método que crea una serie de trabajadores para una clínica

        Args:
            ok (bool, optional): Atributo que determina la ejecución o no de la inicialización. Defaults to True.
        """        
        if (ok):
            self.AñadirTrabajadorAuto('54128586H', 'Gabby', datetime.datetime(2000, 9, 9), 'H', 'Cirugia', datetime.datetime(2022, 9, 9), '1', 1)
            self.AñadirTrabajadorAuto('54128586M', 'Gabby', datetime.datetime(2000, 9, 9), 'M', 'Trato de Personas', 0, '2')