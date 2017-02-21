#!usr/bin/env python
print("Dime cuantas palabras contiene la lista")
numero=int(input())

#SI NUMERO ES MAYOR QUE 0
if numero > 0:
    lista=[]#CREAMOS LA LISTA VACIA
    #RECORREMOS LOS NUMEROS
    for i in range(numero):
        print("Dime la palabra")
        palabra=input()
        #AÑADIMOS LAS PALABRAS DADAS
        lista+=[palabra]
    print("la lista creada es ",lista)
    #UTILIZAMOS EL METODO PARA ORDENAR
    lista.sort()
    #MOSTRAMOS LA LISTA ORDENADA
    print("la lista ordenada es ",lista)
else:
    print("Imposible, lista vacia")
