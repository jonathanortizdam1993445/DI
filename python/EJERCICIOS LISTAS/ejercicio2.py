#!usr/bin/env python
print("Digame las palabras que contiene la lista");
numero=int(input());

if numero>0:
	lista=[]
	#VAMOS AÑADIENDO PALABRAS A LA LISTA
	for i in range(numero):
		print("Dime la palabra");
		palabra=input();
		lista+=[palabra]
	print("La lista creada es: ",lista);
	print("Dime la palabra a buscar");
	buscar=input();
	#BUSCAMOS LA PALABRA DENTRO DE LA LISTA
	print("la palabra: ",buscar,"aparece :",lista.count(buscar)," veces");	
else:
	print("imposible.Lista vacia")


