#!usr/bin/env python
print("Introduce un numero")
numero = int(input())
lista=[]
#RECORRE TODOS LOS NUMEROS HASTA QUE ENCUENTRE TODOS LOS NUMEROS PRIMOS
for i in range(numero+1):
	acumulador=0
	num=1#CALCULAR LOS DIVISORES QUE INTRODUCIMOS
#SI NUMERO ES MENOR QUE I, HACE EL BUCLE
	while (num <=i):
		if (i%num==0):
			acumulador+=1
			num+=1
		else:
			num+=1
	#SI NUMERO NO ES MENOR QUE I Y DISTINTO DE 0, LO AÑADE A LA LISTA		
	if(i !=0):
		if(acumulador <= 2):
			lista.append(i)

print("Los numeros primos de ",numero," son: ",lista)