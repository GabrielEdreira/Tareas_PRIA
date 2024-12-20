import Trabajador

class Clinica():
    _Medicos_ = dict()
    _Enfermeras_ = dict()

    def __init__(self):
        pass

    @property
    def get_Medicos(self):
        return self._Medicos_
    def print_Medicos(self):
        aux = self._Medicos_.items()
        print(" -------- Clínica: -------- ")

        if (len(aux) == 0):
            print("   No hay médicos ")

        for _, medico in aux:
            print(f" - {medico}")
        print(" --------------------------\n")
    
    def insert_Medico(self, nuevoMedico:Trabajador.Medico):
        if not nuevoMedico:
            raise ValueError("El médico no puede ser inválido.")
        if self._Medicos_.keys().__contains__(nuevoMedico.getNIF()):
            raise ValueError("El médico ya existe.")
        
        self._Medicos_[nuevoMedico.get_NIF()] = nuevoMedico
        
    def delete_Medico(self, NIF_Medico:str):
        if not NIF_Medico:
            raise ValueError("El NIF del médico no puede ser vacío.")
        if not self._Medicos_.keys().__contains__(NIF_Medico):
            raise ValueError("No existe ese médico.")
        
        self._Medicos_.pop(NIF_Medico)

    @property
    def get_Enfermeras(self):
        return self._Enfermeras_
    def print_Enfermeras(self):
        aux = self._Enfermeras__.items()
        print(" -------- Clínica: -------- ")

        if (len(aux) == 0):
            print("   No hay enfermeras ")

        for _, medico in aux:
            print(f" - {medico}")
        print(" --------------------------\n")
    
    def insert_Enfermera(self, nuevaEnfermera:Trabajador.Enfermera):
        if not nuevaEnfermera:
            raise ValueError("La enfermera no puede ser inválida.")
        if self._Enfermeras_.keys().__contains__(nuevaEnfermera.getNIF()):
            raise ValueError("La enfermera ya existe.")
        
        self._Enfermeras_[nuevaEnfermera.get_NIF()] = nuevaEnfermera
        
    def delete_Enfermera(self, NIF_Enfermera:str): 
        if not NIF_Enfermera:
            raise ValueError("El NIF de la enfermera no puede ser vacío.")
        if not self._Enfermeras_.keys().__contains__(NIF_Enfermera):
            raise ValueError("No existe esa enferemera.")
        
        self._Enfermeras_.pop(NIF_Enfermera)


    def AñadirTrabajador(self):
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
                FechaCarrera = input("¿Cuando empezó a ejercer? ")

                self._Medicos_[NIF] = Trabajador.Medico(NIF, Nombre, FechaNac, Sexo, Especialidad, FechaCarrera, NumeroColegiado)

            case "Enfermera":
                Area = input("¿Area? ")
                NumPersonas = input("¿Nº Personas? ")

                self._Enfermeras_[NIF] = Trabajador.Enfermera(NIF, Nombre, FechaNac, Sexo, Area, NumPersonas, NumeroColegiado)

    def BorrarTrabajador(self):
        NIF = input("¿NIF? ")

        if NIF in self._Medicos_.keys(): 
            self._Medicos_.pop(NIF)
        elif NIF in self._Enfermeras_.keys(): 
            self._Enfermeras_.pop(NIF)
        else:
            print("No existen el Trabajador.\n")


    def GetTrabajador(self) -> Trabajador:
        NIF = input("¿NIF? ")

        trabajador = None
        if NIF in self._Medicos_.keys(): 
            trabajador = self._Medicos_[NIF]
        elif NIF in self._Enfermeras_.keys(): 
            trabajador = self._Enfermeras_[NIF]
        else:
            print("No se encuentra el trabajador.\n")
            return

        return trabajador
    
    def printTrabajadores(self):
        trabajadores = list()
        if (len(self._Medicos_) > 0):
            trabajadores.append(self._Medicos_)
        if (len(self._Enfermeras_) > 0):
            trabajadores.append(self._Enfermeras_)

        print(" -------- Clínica: -------- ")

        if (len(trabajadores) == 0):
            print("    No hay trabajadores ")

        for trabajador in trabajadores:
            print(f" - {str(trabajador)}")
        print(" --------------------------\n")