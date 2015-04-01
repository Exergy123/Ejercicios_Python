__author__ = 'Daniel'


#este ejercicio es interesante por la gestion dinamica de memoria de Python que no tiene C

def largo_lista(lista):
    cont=0
    for i in lista:
        cont+=1
    print cont

largo_lista([1,2,3,4,5])