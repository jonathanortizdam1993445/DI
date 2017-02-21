#!usr/bin/env python
print("Dime cuantas palabras tiene la lista")
numero =int(input())

if numero > 0:
	lista=[];
	#RELLENAMOS LA LISTA
	for i in range(numero):
		print("Dime la palabra")
		palabra= input();
		lista+=[palabra]
	print("La lista creada es: ",lista)
	print("dime la palabra a eliminar")
	eliminar=input();
	#ELIMINAMOS LA PALABRA 
	lista.remove(eliminar)
	#COMPROBAMOS QUE SE HA ELIMINADO
	print("La lista ahora es ",lista);
else:
	print("imposible. lista vacia")
