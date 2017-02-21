#!usr/bin/env python
print("Dime cuantas palabras contiene la lista")
numero = int(input())
flag= 0;
if numero > 0 :
	lista=[]
	#RELLENAMOS LA LISTA
	for i in range(numero):
		print("Dime las palabras")
		palabra=input()
		lista+=[palabra]
	print("La lista creada es ",lista)
	#RECORREMOS LA LISTA 
	for i in range(len(lista)-1,-1,-1):
		#LUEGO COMPARAMOS SI HAY PALABRAS REPETIDAS, Y SI LAS HAY LAS ELIMINAMOS
		if lista[i] in lista[:i] :
			del(lista[i])
	#COMPROBAMOS
	print("la lista sin repeticiones es ",lista)
else:
	print("Imposible. lista vacia")
