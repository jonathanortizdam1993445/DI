#!/usr/bin/env python
def gcdIter(numero1,numero2):
	if numero2==0: 
		return numero1
	else:
		#sustituye valores hasta que el modulo de la division es 0
		#y el numero2 se convierta en el maximo comun divisor
		return gcdIter(numero2, numero1 % numero2)
	
# solicitamos los dos números

num1 = int(input("Introduce el primer numero: "))

num2 = int(input("Introduce el segundo numero: "))

print("El máximo común divisor de ", num1," y ", num2," es ", gcdIter(num1, num2))