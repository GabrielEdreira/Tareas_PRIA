import Trabajador

class Clinica():
    _Medicos_ = dict()
    _Enfermeras_ = dict()

    def __init__(self):
        pass

    @property
    def get_Medicos(self):
        return self._Medicos_.items()
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
        if self._Medicos_.values().__contains__(nuevoMedico.getNIF()):
            raise ValueError("El médico ya existe.")
        
        self._Medicos_[nuevoMedico.get_NIF()] = nuevoMedico
        
    def delete_Medico(self, NIF_Medico:str):
        if not NIF_Medico:
            raise ValueError("El NIF del médico no puede ser vacío.")
        if not self._Medicos_.values().__contains__(NIF_Medico):
            raise ValueError("No existe ese médico.")
        
        self._Medicos_.pop(NIF_Medico)

    @property
    def get_Enfermeras(self):
        return self._Enfermeras_.items()
    
        return self._Medicos_.items()
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
        if self._Enfermeras_.values().__contains__(nuevaEnfermera.getNIF()):
            raise ValueError("La enfermera ya existe.")
        
        self._Enfermeras_[nuevaEnfermera.get_NIF()] = nuevaEnfermera
        
    def delete_Enfermera(self, NIF_Enfermera:str): 
        if not NIF_Enfermera:
            raise ValueError("El NIF de la enfermera no puede ser vacío.")
        if not self._Enfermeras_.values().__contains__(NIF_Enfermera):
            raise ValueError("No existe esa enferemera.")
        
        self._Enfermeras_.pop(NIF_Enfermera)