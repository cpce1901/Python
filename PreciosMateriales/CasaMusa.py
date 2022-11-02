import bs4
import requests
from datos import ruta

# pagina de busqueda
url_base = 'https://www.casamusa.cl/cotizacion-online/series-domiciliarias.html?p={}'

# Creamos lista para filtrar datos
valores = []

# lista de productos
producto = []

# LLamamos a todas las rutas y pasamos hasta que pagina queremos revisar
direcciones = ruta(url_base, 0, 10)

# iterar paginas
for i in direcciones:

    # creamos la sopa de cada pagina
    resultado = requests.get(i)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    print(i)

    # buscamos la clase titulo su descipcion y su valor
    titulo = sopa.select('.product-name a')
    precio = sopa.select('.price span')

    # iteramos en todos los tiyulos encontrados
    for a in titulo:
        descripcion = a.get_text()
        producto.append(descripcion)

    # creamos una cuenta para verificar cuales son los valores pares e inpares y diferenciar de normal o internet
    cuenta = 0

    # iteramos en todos los precios
    for e in precio:
        leer = e.get_text().strip()

        # condicionamos para limpiar precios
        if leer.lower() == 'normal:' or leer.lower() == '+ iva' or leer.lower() == 'internet:':
            pass
        else:
            leer = leer.replace('\t', "")
            leer = leer.replace('\n', "")
            leer = leer.replace('+ IVA', "")

            # separamos entre pares e impares
            if cuenta % 2 == 0:
                valores.append(leer)
            else:
                pass

            # aumentamos la cuenta para diferenciar par de impar
            cuenta += 1

# creamos un diccionario con toda la info
entrega = dict(zip(producto, valores))

# imprimimos el diccionario
for i in entrega.keys():
    print(f'{i} \t\tel valor es de: {entrega[i]}')
