__author__ = 'Daniel'


def suma_lista(lista):
    cont=0
    for i in lista:
        cont+=i
    print cont

suma_lista([1,2,3,4,5])

def multi_lista(lista):
    cont=1
    for i in lista:
        cont*=i
    print cont

multi_lista([1,2,3,4,5])