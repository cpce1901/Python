import calculos

# Medidas de malla
l_malla = 10
a_malla = 4
filas = 2
columnas = 4


# Nombre curva Q -4
# Razon de resistividad
a = 1
b = 0.4
c = 0.2

# N° Curva
n_curva = 5
p1 = 480
e1 = 0.16
he = 0.6

Aditivo = True
# Diametro de conductor mts 2
Conductor = 0.0106

# Calculo de superficie y largo del conductor
superficie, largo_conductor = calculos.superficie(l_malla, a_malla, filas, columnas)

# Calculamos los valores de P
lista_p, largo = calculos.pes(p1, a, b, c)

# Calculamos los valores de E
lista_e = calculos.es(e1, n_curva, largo)

# Calculamos R
r = calculos.erre(superficie)

# Calculamos RO
ro = calculos.ro(r, he)

# Calculamos Q
q = calculos.qu(r, he)

# Calculamos Y
lista_y = []
for i in lista_e:
    ye = calculos.ye(q, i, ro)
    lista_y. append(ye)

# Calculamos V
lista_v = []
for i in lista_y:
    ve = calculos.ve(i, q, ro)
    lista_v.append(ve)

# Calculamos F
lista_f = [0]
for i in lista_v:
    efe = calculos.efe(i, ro)
    lista_f.append(efe)

# Calculamos R equivalente
erre_equivalente = calculos.requi(lista_f, lista_p, Aditivo)

# Comprobacion Shuars
k1, k2 = calculos.k_12(he, superficie, l_malla, a_malla)

# Calculamos R de salida
r_salida = calculos.r_final(erre_equivalente, largo_conductor, he, k1, k2, superficie, Conductor)

print(lista_p)
print(lista_e)
print(r)
print(ro)
print(q)
print(lista_y)
print(lista_v)
print(lista_f)
print(erre_equivalente)
print(k1)
print(k2)
print(round(r_salida, 3))
