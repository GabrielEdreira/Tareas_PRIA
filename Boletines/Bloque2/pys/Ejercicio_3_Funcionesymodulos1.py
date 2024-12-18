import argparse

parser = argparse.ArgumentParser(description="usage: fibonacci_generate.py [-h] [--number NUMBER]")
parser.add_argument('--number', type=int, help='Valor de números a generar.', required=False)

args = parser.parse_args()

def fibonacci_generate(number:int = 0):
    array = []
    a, b = 0, 1

    if (number == None):
        return array

    if (number > 0):
        array.append(a)
    if (number > 1):
        array.append(b)
    if (number > 2):
        for _ in range(number - 2):
            array.append(a+b)
            a, b = b, a + b
    return array


def main():
    try:
        num = args.number
    except:
        num = 0

    aux = fibonacci_generate(num)
    if (len(aux) > 0):
        print(aux)
    else:
        print("El valor introducido tiene un formato incorrecto.")
if (__name__ == "__main__"):
    main()