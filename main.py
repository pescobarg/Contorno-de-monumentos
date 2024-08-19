from silueta_iterativa import tiempo_ejecucion_iterativo
from silueta_recursiva import tiempo_ejecucion_recursivo
import time
import sys
import random

def generar_piezas(filename, cantidad_datos):
    with open(filename, 'w') as file:
        for _ in range(cantidad_datos):
            x = random.randint(1, 100)
            d = random.randint(1, 100)
            h = random.randint(1, 100)
            file.write(f'{x},{d},{h}\n')

def medir_tiempos(filename, cantidad_datos):
    tiempo_iterativo = tiempo_ejecucion_iterativo(filename)
    tiempo_recursivo = tiempo_ejecucion_recursivo(filename)

    print(f'{cantidad_datos}, {tiempo_iterativo}, {tiempo_recursivo}')

def main():
    if len(sys.argv) != 4:
        print("Uso: python script.py [cantidad_minima_datos] [cantidad_maxima_datos] [diferencia_entre_datos]")
        sys.exit(1)

    cantidad_minima = int(sys.argv[1])
    cantidad_maxima = int(sys.argv[2])
    diferencia_datos = int(sys.argv[3])

    filename = 'piezas.txt'

    for cantidad_datos in range(cantidad_minima, cantidad_maxima + 1, diferencia_datos):
        generar_piezas(filename, cantidad_datos)
        medir_tiempos(filename, cantidad_datos)

if __name__ == "__main__":
    main()
