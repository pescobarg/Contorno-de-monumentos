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
    return get_silueta_aux(piezas, 0, len(piezas) - 1)

def get_silueta_aux(piezas, begin, end):
    if begin == end:
        critical_p = []
        critical_p.append(Punto(piezas[begin].start, piezas[begin].height))
        critical_p.append(Punto(piezas[begin].finish, 0))
        return critical_p

    mitad = (begin + end) // 2
    critical_pi = get_silueta_aux(piezas, begin, mitad)
    critical_pd = get_silueta_aux(piezas, mitad + 1, end)

    return juntar_siluetas(critical_pi, critical_pd)

def juntar_siluetas(critical_pi, critical_pd):
    critical_p = []
    i = j = 0
    hi = hd = 0

    while i < len(critical_pi) and j < len(critical_pd):
        if critical_pi[i].x < critical_pd[j].x:
            if critical_pi[i].y == critical_pd[j].y and critical_pi[i].y == 0:
                critical_p.append(critical_pd[j])
                hi = update_max(hi, critical_pi[i].y)
                hd = update_max(hd, critical_pd[j].y)
                i += 1
                j += 1
            else:
                critical_p.append(critical_pi[i])
                hi = update_max(hi, critical_pi[i].y)
                hd = update_max(hd, critical_pd[j].y)
                i += 1
        elif critical_pd[j].x < critical_pi[i].x:
            if critical_pi[i].y == critical_pd[j].y:
                if hd > hi:
                    critical_p.append(Punto(critical_pd[j].x, hi))
                critical_p.append(critical_pi[i])
                hi = update_max(hi, critical_pi[i].y)
                hd = update_max(hd, critical_pd[j].y)
                i += 1
                j += 1
            elif len(critical_p) > 0 and critical_pd[j].y < critical_p[-1].y and critical_p[-1].x < critical_pd[j].x:
                critical_p.append(Punto(critical_pi[i].x, critical_pd[j].y))
                hi = update_max(hi, critical_pi[i].y)
                hd = update_max(hd, critical_pd[j].y)
                i += 1
                j += 1
            else:
                critical_p.append(critical_pd[j])
                hi = update_max(hi, critical_pi[i].y)
                hd = update_max(hd, critical_pd[j].y)
                j += 1
        else:
            critical_p.append(critical_pd[j])
            hi = update_max(hi, critical_pi[i].y)
            hd = update_max(hd, critical_pd[j].y)
            j += 1
            i += 1

    for k in range(i, len(critical_pi)):
        critical_p.append(critical_pi[k])
    for k in range(j, len(critical_pd)):
        critical_p.append(critical_pd[k])

    return critical_p

def update_max(hmax, nh):
    if hmax < nh:
        hmax = nh
    return hmax

def leer_archivo_piezas(filename):
    piezas = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            start, finish, height = map(int, parts)
            piezas.append(Rectangle(start, finish, height))
    return piezas

def tiempo_ejecucion_recursivo(filename):
    start_time = time.perf_counter_ns()
    
    piezas = leer_archivo_piezas(filename)
    puntos_criticos = get_silueta(piezas)
    
    end_time = time.perf_counter_ns()
    return end_time - start_time
