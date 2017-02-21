#!usr/bin/env python
print("Dime cuantas palabras tiene la 1º lista")
numeros1 =int(input());

if numeros1 > 0:
		lista1=[]
		#RELLENAMOS LA LISTA1
		for i in range(numeros1):
			print("Dime la palabra");
			palabra1=[str(input())];
			lista1+=[palabra1];
		print("La 1º lista creada es ",lista1)	
		print("Dime cuantas palabras tiene la 2º lista")
		numeros2=int(input());
		if numeros2 > 0:
			lista2=[]
		#RELLENAMOS LA LISTA2
			for i in range(numeros2):
				print("Dime la palabra");
				palabra2=[str(input())];
				lista2+=[palabra2];
			print("La 2º lista creada es ",lista2)
			#RECORREMOS LAS 2 LISTA DESDE EL FINAL
			for i in lista2:
				for a in range(len(lista1)-1,-1,-1):
					if lista1[a]==i:
						#ELIMINAMOS LAS PALABRAS DE LAS LISTA 2 EN LA LISTA 1
						del(lista1[a])
#COMPROBAMOS LA LISTA 1
			print("Ahora la lista es ",lista1);
else:
	print("imposible.lista vacia")


