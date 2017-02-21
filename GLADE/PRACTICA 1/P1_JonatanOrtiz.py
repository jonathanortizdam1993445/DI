#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk

def insertar1(button):
        
        texto=builder.get_object("entrada_texto1")
        texto.set_max_length(15)
        texto.set_text(texto.get_text()+"1")

def insertar2(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"2")

def insertar3(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"3")

def insertar4(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"4")

def insertar5(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"5")

def insertar6(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"6")

def insertar7(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"7")

def insertar8(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"8")
def insertar9(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"9")

def insertar0(button):

	texto=builder.get_object("entrada_texto1")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"0")

def insertar11(button):
        
        texto=builder.get_object("entrada_texto2")
        texto.set_max_length(15)
        texto.set_text(texto.get_text()+"1")

def insertar22(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"2")

def insertar33(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"3")

def insertar44(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"4")

def insertar55(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"5")

def insertar66(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"6")

def insertar77(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"7")

def insertar88(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"8")
def insertar99(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"9")

def insertar00(button):

	texto=builder.get_object("entrada_texto2")
	texto.set_max_length(15)
	texto.set_text(texto.get_text()+"0")

def suma(button):
	texto=builder.get_object("entrada_texto1")
	texto2=builder.get_object("entrada_texto2")
	etiqueta=builder.get_object("etiqueta_resultado")

	oper1=int(texto.get_text())
	oper2=int(texto2.get_text())
	igual=oper1+oper2
	etiqueta.set_text("Resultado: "+str(igual))

def resta(button):
	texto=builder.get_object("entrada_texto1")
	texto2=builder.get_object("entrada_texto2")
	etiqueta=builder.get_object("etiqueta_resultado")

	oper1=int(texto.get_text())
	oper2=int(texto2.get_text())
	igual=oper1-oper2
	etiqueta.set_text("Resultado: "+str(igual))

def multi(button):
	texto=builder.get_object("entrada_texto1")
	texto2=builder.get_object("entrada_texto2")
	etiqueta=builder.get_object("etiqueta_resultado")

	oper1=int(texto.get_text())
	oper2=int(texto2.get_text())
	igual=oper1*oper2
	etiqueta.set_text("Resultado: "+str(igual))

def div(button):
	texto=builder.get_object("entrada_texto1")
	texto2=builder.get_object("entrada_texto2")
	etiqueta=builder.get_object("etiqueta_resultado")

	oper1=int(texto.get_text())
	oper2=int(texto2.get_text())
	igual=oper1/oper2
	etiqueta.set_text("Resultado: "+str(igual))

def eliminar(button):
        texto=builder.get_object("entrada_texto1")
        texto2=builder.get_object("entrada_texto2")
        texto.set_text("")
        texto2.set_text("")
        
#CREO EL OBJETO DEL BUILDER
builder= Gtk.Builder()
#INDICO EL FICHERO DE GLADE
builder.add_from_file("P1_JonatanOrtiz.glade")
#INDICO LOS EVENTOS Y COMO SE VAN A LLAMAR SUS FUNCIONES
handlers ={
	"Terminar": Gtk.main_quit,
	"1": insertar1,
        "11": insertar11,
	"2": insertar2,
        "22": insertar22,
	"3": insertar3,
        "33": insertar33,
	"4": insertar4,
        "44": insertar44,
	"5": insertar5,
        "55": insertar55,
	"6": insertar6,
        "66": insertar66,
	"7": insertar7,
        "77": insertar77,
	"8": insertar8,
        "88": insertar88,
	"9": insertar9,
        "99": insertar99,
	"0": insertar0,
        "00": insertar00,
	"sumar":suma,
        "restar":resta,
        "multiplicar":multi,
        "dividir": div,
        "borrar": eliminar
}
#CONECOTO LOS EVENTOS
builder.connect_signals(handlers)
#CREA LA VENTANA INICIAL CON TODOS SUS COMPONENTES
window=builder.get_object("ventana")
#PARA VER TODO LO QUE CONTIENE LA VENTANA
window.show_all()
#PARA INICIAR EL MAIN
Gtk.main()

