__author__ = 'Daniel'
#Definir una funcion maximo
#
#
#

def maximo(n1,n2):
    if n1<n2:
        print n2
        print'es mayor'
    if n2<n1:
        print n1
        print 'es mayor'
    if n1==n2:
        print 'son iguales'

maximo(3,2)