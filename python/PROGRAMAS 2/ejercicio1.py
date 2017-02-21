#!/usr/bin/env python
#CREAMOS LA FUNCION
def iterPower(base,exp):
	#CREAMOS LA VARIABLE PARA GUARDAR EL RESULTADO
	acumulador=1;
	#MIENTRAS EL EXPONENTE SEA MAYOR QUE 0, PUEDE REALIZAR LA OPERACION
	while exp>0:

		acumulador*=base;
		exp-=1;
	#DEVUELVE EL RESULTADO
	return acumulador;

print(iterPower(3,2));