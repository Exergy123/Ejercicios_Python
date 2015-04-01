__author__ = 'Daniel'


#muy interesante, utiliza punteros y gestion de memoria dinamica
#punteros enfoca desde la posicion 0  hasta x-1


def invertir(cadena):

    indice=len(cadena)-1
    invertida=""
    print indice
    while indice!=0:
        invertida+=cadena[indice]
        indice-=1
    print invertida

invertir('ola k hase')