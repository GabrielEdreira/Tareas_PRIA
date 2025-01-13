import Trabajador
import Clinica

def printMenu():
    print("\nGestión de los trabajadores del hospital\n"
        + "1. Añadir trabajador\n"
        + "2. Borrar trabajador\n"
        + "3. Mostrar lista de trabajadores\n"
        + "4. Mostrar detalle de un trabajador\n"
        + "5. Mostrar número de años trabajados de un médico\n"
        + "6. Mostrar número de personas a cargo de una enfermera\n"
        + "7. Añadir personas a cargo de una enfermera\n"
        + "8. Reducir personas a cargo de una enfermera\n"
        + "9. Salir\n")

def main():
    Mi_Clinica = Clinica.Clinica()

    Mi_Clinica.Inicializar()

    res = None
    while (res != "9"):
        printMenu()
        
        res = input("Elección: ")
        print()
        match(res):
            case "1":
                Mi_Clinica.AñadirTrabajador()
            case "2":
                Mi_Clinica.BorrarTrabajador()
            case "3":
                Mi_Clinica.printTrabajadores()
            case "4":
                print(str(Mi_Clinica.GetTrabajador()))
            case "5":
                Medico = Mi_Clinica.GetTrabajador("Medico")
                if (Medico != None):
                    print(f"Ha trabajado un total de {Medico.getNumeroAnhos()} años.")
            case "6":
                Enfermera = Mi_Clinica.GetTrabajador("Enfermera")
                if (Enfermera != None):
                    print(f"Hay {Enfermera.getPersonasCargo()} personas a cargo.")
            case "7":
                Enfermera = Mi_Clinica.GetTrabajador("Enfermera")
                if (Enfermera != None):
                    Enfermera.AñadirPersonaCargo()
            case "8":
                Enfermera = Mi_Clinica.GetTrabajador("Enfermera")
                if (Enfermera != None):
                    Enfermera.BorrarPersonaCargo()
            case "9":
                print("¡Hasta pronto!\n")


if __name__ == "__main__":
    main()