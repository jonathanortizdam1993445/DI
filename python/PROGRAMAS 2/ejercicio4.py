#!usr/bin/env python
#CREAMOS LA FUNCION
def Item_order(pedido):
	#HACEMOS UN BUCLE PARA RECORRER EL PEDIDO Y QUE VAYA CONTANDO LAS PALABRAS REPETIDAS
	for i in lista:
		if "ensalada" :
			i.count("ensalada")
		if "agua" :
			i.count("agua")
		if "hamburguesa" :
			i.count("hamburguesa")
		pedido=print("ensalada: ",i.count("ensalada")," agua:",i.count("agua"),"hamburguesa: ",i.count("hamburguesa"))
		

lista=[]
cadenas=input("Dime lo que quieres de pedido ")
#INSERTA LAS PALABRAS EN LA LISTA
lista.append(cadenas)
#MUESTRA EL RESULTADO DE LA FUNCION
print(Item_order(lista))
