__author__ = 'Daniel'


#utilizamos operaciones booleanas

def maximo_de_tres(n1,n2,n3):
    if n1<n2 and n3<n2:
        print n2
        print'es mayor'
    if n2<n1 and n3<n1:
        print n1
        print 'es mayor'
    if n1<n3 and n2<n3:
        print n3
        print'es mayor'
    else:
        print 'son iguales'

maximo(3,2)