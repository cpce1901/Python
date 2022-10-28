import math


# Funcion para calcular P
def pes(p1, *kargs):
    # Guardamos los valopres de la curva
    valores = [i for i in kargs]

    # Guardamos P1
    p1 = p1

    # Averiguamos la longitud de los valores
    largo = len(valores)

    if largo == 3:
        p2 = p1 * valores[1]
        p3 = p1 * valores[2]

        return [p1, p2, p3], largo

    elif largo == 4:
        p2 = p1 * valores[1]
        p3 = p1 * valores[2]
        p4 = p1 * valores[3]

        return [p1, p2, p3, p4], largo


# Funcion para calcular E
def es(e1, n_curva, largo):
    if largo == 3:
        e1 = e1
        e2 = e1 * n_curva
        e3 = 1000

        return [e1, e2, e3]

    elif largo == 4:
        e1 = e1
        e2 = e1
        e3 = e1 * n_curva
        e4 = 1000

        return [e1, e2, e3, e4]


def superficie(la, a, fil, col):
    s = la * a
    largo_conductor = (la * (fil + 1)) + (a * (col + 2))
    return s, largo_conductor


def erre(superf):
    r = math.sqrt(superf / math.pi)
    return r


def ro(ere, he):
    r = math.sqrt(math.pow(ere, 2) - math.pow(he, 2))
    return r


def qu(ere, he):
    q = math.sqrt(2 * math.pi * (ere + he))
    return q


def ye(q, e, rho):
    y = math.pow(q, 2) + math.pow(e, 2) + math.pow(rho, 2)
    return y


def ve(y, q, rho):
    v = math.sqrt(0.5 * (y - math.sqrt(math.pow(y, 2) - (4 * math.pow(q, 2) * math.pow(rho, 2)))))
    return v


def efe(v, rho):
    ef = math.sqrt(1 - (math.pow(v, 2) / math.pow(rho, 2)))
    return ef


def requi(lista_f, lista_p, aditivo):
    lar = len(lista_f)
    if lar == 4:
        a = (lista_f[1] - lista_f[0]) / lista_p[0]
        b = (lista_f[2] - lista_f[1]) / lista_p[1]
        c = (lista_f[3] - lista_f[2]) / lista_p[2]
        r_equi = lista_f[3] / (a + b + c)
        if aditivo:
            r_equi = r_equi * 0.5
            return r_equi
        else:
            return r_equi


def k_12(h, s, la, a):
    k1 = 1.43 - ((2.3 * h) / math.sqrt(s)) - 0.044 * (la / a)
    k2 = 5.5 - ((8 * h) / math.sqrt(s)) + (0.15 - (h / math.sqrt(s))) * (la / a)
    return k1, k2


def r_final(er_equi, l_conductor, he, k1, k2, superf, cable):
    a = er_equi / (math.pi * l_conductor)
    b = (2 * l_conductor) / math.sqrt(he * cable)
    c = math.log(b)
    d = (k1 * l_conductor) / math.sqrt(superf)
    e = c + d - k2
    salida = a * e
    return salida
