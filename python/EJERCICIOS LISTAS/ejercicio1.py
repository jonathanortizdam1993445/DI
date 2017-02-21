#!usr/bin/env python
print("Dime el número de palabras a introducir en la lista")
numero =int(input());

if int(numero)>0:
	lista=[]
	#VAMOS RELLENANDO LA LISTA TANTAS VECES COMO HEMOS INDICADO ARRIBA
	for i in range(numero):
			print ("Digame la palabra");
			palabra=input();
			lista+=[palabra]	
	print("La lista creada es: ",lista)	
else:
	print("Imposible")
	

