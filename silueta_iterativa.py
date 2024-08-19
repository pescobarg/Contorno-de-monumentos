import time

class Rectangle:
    def __init__(self, start, finish, height):
        self.start = start
        self.finish = finish
        self.height = height

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_silueta(piezas):
    critical_p = []
    altura_aux = 0
    width = 0
    num_piezas = len(piezas)

    for i in range(num_piezas):
        if (piezas[i].start < piezas[i - 1].finish and 
            piezas[i - 1].start < piezas[i].start and 
            piezas[i].finish > piezas[i - 1].finish and 
            piezas[i].height < altura_aux):
            critical_p.append(Punto(piezas[i - 1].finish, piezas[i].height))
            altura_aux = piezas[i].height
        elif piezas[i].start < piezas[i + 1].start if i < num_piezas - 1 else False:
            critical_p.append(Punto(piezas[i].start, piezas[i].height))
            altura_aux = piezas[i].height
        if (piezas[i].finish > piezas[i - 1].finish and 
            piezas[i].finish < piezas[i + 1].start if i < num_piezas - 1 else False):
            critical_p.append(Punto(piezas[i].finish, 0))
            altura_aux = 0
        if (piezas[i].finish < piezas[i - 1].finish and 
            piezas[i].height > altura_aux):
            critical_p.append(Punto(piezas[i].finish, piezas[i - 1].height))
            altura_aux = piezas[i - 1].height
        if piezas[i].finish == piezas[i + 1].start if i < num_piezas - 1 else False:
            critical_p.append(Punto(piezas[i].finish, piezas[i + 1].height))
            altura_aux = piezas[i + 1].height

        width = max_width(width, piezas[i].finish)

    critical_p.append(Punto(width, 0))
    return critical_p

def max_width(w1, w2):
    return max(w1, w2)

def leer_archivo_piezas(filename):
    piezas = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            start, finish, height = map(int, parts)
            piezas.append(Rectangle(start, finish, height))
    return piezas

def tiempo_ejecucion_iterativo(filename):
    start_time = time.perf_counter_ns()
    
    piezas = leer_archivo_piezas(filename)
    puntos_criticos = get_silueta(piezas)
    
    end_time = time.perf_counter_ns()
    return end_time - start_time
