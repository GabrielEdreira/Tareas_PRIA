import Ejercicio_2_Funcionesymodulos1 as ejercicio2
import Ejercicio_3_Funcionesymodulos1 as ejercicio3

def paint_menu() -> int:
    print(" 1. Calcular la secuencia de Fibonacci hasta un número\n 2. Convertir temperatura de ºC a ºF\n 3. Salir\n")

    try: 
        num = int(input("Inserte la elección: "))
    except:
        num = 0

    return num


def main():
    exit = False
    while(not exit):
        match (paint_menu()):
            case 1: # fibonacci_generate
                try: 
                    num = int(input("Ingrese un número: "))
                except:
                    print("Formato incorrecto en el número.")
                    continue
                    
                print(f"{ejercicio3.fibonacci_generate(num)} \n")

            case 2: # convertTemperature
                try: 
                    temp = int(input("Ingrese la temperatura: "))
                except:
                    print("Formato incorrecto en la temperatura.")
                    continue

                scale = input("Ingrese la escala:").strip()

                print(f"{ejercicio2.convertTemperature(temp, scale)} \n")

            case 3: # Exit
                print("Hasta pronto!") 
                exit = True
            case _: # Error
                print("Valor desconocido.")
if (__name__ == "__main__"):
    main()