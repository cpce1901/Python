def ruta(url_base, inicio, fin):
    urls = []
    for i in range(inicio, fin):
        valor = url_base.format(i)
        urls.append(valor)

    return urls
