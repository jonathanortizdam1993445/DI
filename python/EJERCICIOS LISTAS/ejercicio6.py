#!usr/bin/env python
print("Dime cuantas palabras tiene la lista")
numero = int(input())

if numero > 0:
	lista1=[]
	#RECORREMOS LA LISTA
	for i in range(numero):
		print("Dime la palabra")
		palabra=input()
		lista1+=[palabra]
	print("la 1º lista es",lista1)
	#CREAMOS UNA VARIABLE EN LA CUAL CAMBIAMOS DE POSICION LAS PALABRAS 
	lista2=lista1[::-1]
	#COMPROBAMOS QUE SE HA REALIZADO CORRECTAMENTE
	print("la lista inversa es ",lista2)
	print	
else:
	pritn("Imposible. lista vacia")	
