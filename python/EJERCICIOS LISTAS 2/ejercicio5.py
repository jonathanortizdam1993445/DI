#!usr/bin/env python
print("Introduce el 1º termino de la sucesion ")
termino1=int(input())

print("Dime cuantos terminos de la sucesion quieres")
cantidad=int(input())

lista=[]#CREAMOS LA LISTA
lista.append(cantidad)#AGREGAMOS EL TERMINO1
for i in range(cantidad):#RECORREMOS LA CANTIDAD DE TERMINOS
	if termino1%2!=0:#SI NUMERO INTRODUCIDO ES IMPAR, HACE LAFORMULA Y LO AÑADE
		termino1=int(3*termino1+1)
		lista.append(termino1)
	elif termino1%2==0:#CUANDO ACABA EL ANTERIOR COMPRUEBA SI 
	#EL NUEMRO ES IMPAR O PAR,SI ES IMPAR, HACE LAFORMULA Y LO AÑADE
		termino1=int(termino1/2)
		lista.append(termino1)
print("los terminos de la sucesion son: " ,lista)			