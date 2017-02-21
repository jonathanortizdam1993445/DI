#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk

#ESTE METODO PASA LOS DATOS INTRODUCIDOS A LA VENTANA DE DIALOGO
def aceptar_registro(button):
	window2.show_all()

	resultado_usuario.set_text(usuario.get_text())
	resultado_password.set_text(password.get_text())
	resultado_correo.set_text(correo.get_text())
	resultado_nombre.set_text(nombre.get_text())
	resultado_apellido.set_text(apellido.get_text())
	resultado_direccion.set_text(direccion.get_text())
	
#CUANDO EN EL DIALOGO PULSAMOS CANCELAR, ESTA SE QUEDA EN SEGUNDO PLANO
def cancelar_dialogo(button):
        dialogo=builder.get_object("dialogo")
        dialogo.hide()
        
#CUANDO EN EL DIALOGO PULSAMOS ACEPTAR, ESTA SE QUEDA EN SEGUNDO PLANO        
def aceptar_dialogo(button):
        dialogo=builder.get_object("dialogo")
        dialogo.hide()
#creamos el manipulador
builder=Gtk.Builder()
#INDICAMOS EL FICHERO DE GLADE
builder.add_from_file("P1_2_JonatanOrtiz.glade")
#INDICAMOS LOS EVENTOS Y LOS RELACIONAMOS
handlers ={
	"Terminar": Gtk.main_quit,
	"reposo":Gtk.main_quit,
	"aceptar_registro": aceptar_registro,
        "aceptar_dialogo":aceptar_dialogo,
        "cancelar_dialogo":cancelar_dialogo
}
#CONECTAMOS LOS EVENTOS
builder.connect_signals(handlers)

#CREAMOS LAS VARIABLES DE LOS OBJETOS QUE NECESITAMOS
window=builder.get_object("ventana")
window2=builder.get_object("dialogo")

usuario=builder.get_object("entrada_usuario")
password=builder.get_object("entrada_contra")
#PARA QUE NO SE VEA LA CONTRASEÑA INTRODUCIDA
password.set_visibility(False)
correo=builder.get_object("entrada_correo")
nombre=builder.get_object("entrada_nombre")
apellido=builder.get_object("entrada_apellido")
direccion=builder.get_object("entrada_direccion")

resultado_usuario=builder.get_object("etiqueta_resultado_usuario")
resultado_password=builder.get_object("etiqueta_resultado_contr")
resultado_correo=builder.get_object("etiqueta_resultado_correo")
resultado_nombre=builder.get_object("etiqueta_resultado_nombre")
resultado_apellido=builder.get_object("etiqueta_resultado_apellido")
resultado_direccion=builder.get_object("etiqueta_resultado_direccion")

#MOSTRAMOS LA VENTANA PRINICPAL
window.show_all()

#MOSTRAMOS EL MAIN
Gtk.main()

