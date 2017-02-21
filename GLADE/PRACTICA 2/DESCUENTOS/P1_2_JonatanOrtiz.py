#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk

#CREAMOS LA FUNCION PRINCIPAL,QUE SU FUNCION DEPENDE DEL DESCUENTO SELECCIONADO
def lista(button):
        if descuentos.get_active_text()=='5':
        
            tasa=float(5/100)
            pre=float(precio.get_text())
            total=float(tasa*pre)
            etiqueta_descuento.set_text(str(total))
            preciofinal=float(pre-total)
            etiqueta_precio.set_text(str(preciofinal))
        
        elif descuentos.get_active_text()=='10':
        
            tasa=float(10/100)
            pre=float(precio.get_text())
            total=float(tasa*pre)
            etiqueta_descuento.set_text(str(total))
            preciofinal=float(pre-total)
            etiqueta_precio.set_text(str(preciofinal))
        
        else:
            tasa=float(20/100)
            pre=float(precio.get_text())
            total=float(tasa*pre)
            etiqueta_descuento.set_text(str(total))
            preciofinal=float(pre-total)
            etiqueta_precio.set_text(str(preciofinal))
#CREAMOS LA FUNCION PARA QUE CUANDO PONGAMOS UNA LETRA NOS SALTE UN
#MENSAJE DE ERROR, (NO FUNCIONA)
def verificacion(button):
    if precio.get_text()!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
        error=builder.get_object("error")
        error.show_all()
    else:
        lista(descuentos)
    
        
#CUANDO PULSAMOS EL BOTON, NOS SALTA LA VENTANA DE DIALOGO        
def dialogo(button):
    window2=builder.get_object("dialogo")
    window2.show_all()

#CUANDO PULSAMOS EL BOTON, NOS SALTA LA VENTANA DE DIALOGO     
def personal(button):
    window3=builder.get_object("ventana2")
    window3.show_all()
    
#CUANDO PULSAMOS EL BOTON, LA VENTANA DE ACERCA DE, PASA A SEGUNDO PLANO
def cerrar_personal(button):
    window4=builder.get_object("ventana2")
    window4.hide()
    
#CUANDO PULSAMOS EL BOTON, LA VENTANA DE DIALOGO, PASA A SEGUNDO PLANO
def cerrar_dialogo(button):
    dialogo=builder.get_object("dialogo")
    dialogo.hide()
    
def error(button):
    error=builder.get_object("error")
    error.hide()

#CREO EL OBJETO DEL BUILDER
builder= Gtk.Builder()
#INDICO EL FICHERO DE GLADE
builder.add_from_file("P1_2_Jonatanortiz.glade")
#INDICO LOS EVENTOS Y COMO SE VAN A LLAMAR SUS FUNCIONES
handlers ={
    "salir":Gtk.main_quit,
    "Terminar":Gtk.main_quit,
    "cerrar":Gtk.main_quit,
    "cerrar_todo":Gtk.main_quit,
    "cerrar_personal":cerrar_personal,
    "cerrar_dialogo":cerrar_dialogo,
    "cambio":lista,
    "enlazar": dialogo,
    "creditos":personal,
    "mensaje":error,
}
#CONECTO LOS EVENTOS
builder.connect_signals(handlers)

#CREA LA VENTANA INICIAL CON TODOS SUS COMPONENTES
window=builder.get_object("ventana1")

#AQUI CREO LAS VARIABLES
precio=builder.get_object("entrada_precio")
descuentos=builder.get_object("lista_descuentos")
etiqueta_precio=builder.get_object("resultado_precio")
etiqueta_descuento=builder.get_object("resultado_descuento")

#PARA VER TODO LO QUE CONTIENE LA VENTANA
window.show_all()
#PARA INICIAR EL MAIN
Gtk.main()
