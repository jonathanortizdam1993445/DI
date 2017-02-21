#!usr/bin/env python
print("Dime cuantas tiene la lista");
numero=int(input());
if numero>0:
	lista=[];
	#RELLENAMOS LA LISTA
	for i in range(numero):
		print("Dime la palabra")
		palabra=input();
		lista+=[palabra]
	print("la lista creada es ",lista);
	print("dime la posicion")
	pos=int(input());
	print("Indica la palabra a sustituir")
	nombre=input();
	print("por la palabra")
	sust=input();
	#SUSTITUIMOS LA PALABRA EN LA POSICION INDICADA ANTERIORMENTE
	lista[pos]=sust
	print("la lista es ahora: ",lista);
else:
	print("imposible.lista vacia")	
