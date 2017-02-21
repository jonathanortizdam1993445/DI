#!/usr/bin/env python
#PEDIMOS LA CANTIDAD DE PALABRAS
print("Dime cuantas palabras tiene la 1º lista")
numero1=int(input())

if numero1 > 0:
    lista1=[]
    #RELLENAMOS LA LISTA1
    for i in range(numero1):
        print("Dime la palabra")
        palabra1=input()
        lista1+=[palabra1]
    print("La 1º lista es ",lista1)
    #PEDIMOS LA CANTIDAD DE PALABRAS
    print("Dime cuantas palabras tiene la 2º lista")
    numero2= int(input())
     #RELLENAMOS LA LISTA2
    if numero2 > 0:
        lista2=[]
        for i in range(numero2):
            print("Dime la palabra")
            palabra2=input()
            lista2+=[palabra2]
            #CREAMOS UNA VARIABLE DONDE SE GUARDAN LAS PALABRAS
            #DE LAS 2 LISTAS SIN REPETICIONES
        combinado=list(set(lista1+lista2))
    print("palabras que aparecen en las 2 listas ",combinado)
    repetidas=[]
    #ALMACENAMOS LAS PALABRAS REPETIDAS DE LAS 2 LISTAS
    for i in lista1:
    	if i in lista2:
    		repetidas=[i] + repetidas
    print("palabras repetidas en las 2 listas",repetidas)
    #CREAMOS UN VARIABLE DONDE GUARDAR TODAS LAS PALABRAS 
    #DE LAS LISTAS CON REPETICIONES
    todas=repetidas+combinado
    print("la lista de todas las palabras son ",todas)
else:
	print("Imposible.lista vacia")    		
    
