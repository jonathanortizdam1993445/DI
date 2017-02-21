#!usr/bin/env python
print("Dime un numero")
numero=int(input())

if numero > 0:
    listanumeros=[]
    #RECORREMOS EL RANGO DE NUMERO, ENTRE EL 1 Y EL INTRODUCIDO
    for i in range(1,numero + 1):
        #SI EL RESTO DE LA DIVISION ES 0
        if(numero%i == 0):
            #GUARDAMOS EL DIVISOR EN LA LISTA
            listanumeros+=[i]
    print("los divisores de ",numero," son los siguientes ",listanumeros)           
else:
    print("Error. Número mayor que 0")
