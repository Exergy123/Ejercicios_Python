__author__ = 'Daniel'


#utilizamos dos funciones

def invertir(cadena):

    indice=len(cadena)-1
    invertida=""
    print indice
    while indice!=0:
        invertida+=cadena[indice]
        indice-=1
    print invertida

def es_palindromo(cadena):

    indice=len(cadena)-1
    invertida=""
    print indice

    print 'No es palindroma'
    while indice!=0:
        invertida+=cadena[indice]
        indice-=1


    print 'Es palindroma'


es_palindromo('radar')

es_palindromo('sonar')