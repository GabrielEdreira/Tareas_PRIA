import argparse

parser = argparse.ArgumentParser(description="usage: temperature_converter.py [-h] [--temp TEMP] [--scale {C,F}]")
parser.add_argument('--temp', type=str, help='Valor de temperatura a convertir.', required=False)
parser.add_argument('--scale', type=str, help='{C,F}  Escala de la temperatura de entrada (C or F). Opcional - Valor por defecto: C', required=False)

args = parser.parse_args()

def convertTemperature(temp:int, escala:str = "C") -> str:
    try:
        temp = int(temp)
    except:
        return "Formato incorrecto en el parámetro '--temp'; utilice '-h' o '--help' para obtener ayuda."

    match (escala):
        case "F":
            return (f"La conversión es: {((temp - 32) / (9/5)).__round__(2)} Cº")
        case _: # Por defecto 'C':
            return (f"La conversión es: {(temp * (9/5) + 32).__round__(2)} Fº")


def main():
    print(convertTemperature(args.temp, args.scale))
if (__name__ == "__main__"):
    main()