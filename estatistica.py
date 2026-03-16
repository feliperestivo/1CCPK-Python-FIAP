import ntpath
def get_filename(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def media(lista):    return sum(lista) / len(lista)
def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2
    else:
        return lista_ordenada[n//2]