#!usr/bin/env python
print("Introduce el valor de a")
a=int(input())

print("Introduce el valor de b")
b=int(input())

print("Introduce el primer termino de la sucesion")
termino1=int(input())

print("Dime cuantos terminos de la sucesion quieres")
cantidad=int(input())

lista=[]#CREAMOS UNA LISTA VACIA
lista.append(termino1)#AÑADIMOS A LA LISTA EL 1º TERMINO 

for i in range(cantidad):#RECORREMOS LA CANTIDAD DE TERMINOS
	termino1=a*termino1+b#TERMINO1 VA CAMBIANDO DE VALOR Y LOS 
	#ALMACENA EN LA LISTA, HASTA QUE SE ACABE LA CANTIDAD DE TERMINOS
	lista.append(termino1)
print("Los terminos de la sucesión son ",lista)	

