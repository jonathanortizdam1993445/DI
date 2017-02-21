#!usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sqlite3

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
        
#CUANDO EN EL DIALOGO PULSAMOS ACEPTAR, PASA LOS DATOS A LA BASE DE DATOS        
def aceptar_dialogo(button):
        us=resultado_usuario.get_text()
        ps=resultado_password.get_text()
        co=resultado_correo.get_text()
        no=resultado_nombre.get_text()
        ap=resultado_apellido.get_text()
        di=resultado_direccion.get_text()
        cursor.execute("INSERT INTO tUsuario (Usuario,Contraseña,Email,Nombre,Apellido,Direccion)"+
                       "VALUES ('"+us+"','"+ps+"','"+co+"','"+no+"','"+ap+"','"+di+"')");
        conexion.commit()
        #SI HAY UN ERROR EN ALGUN PARAMETRO, NO HACE EL INSERT
        conexion.rollback()
        conexion.close()

def listar(button):
        ventana2=builder.get_object("ventana_listar")
        cursor.execute("SELECT * FROM tusuario")
        lista0=[]
        lista1=[]
        lista2=[]
        lista3=[]
        lista4=[]
        lista5=[]
        for row in cursor:
                lista0.append(row[0])
                lista1.append(row[1])
                lista2.append(row[2])
                lista3.append(row[3])
                lista4.append(row[4])
                lista5.append(row[5])
		
                resultado_lista_usuario.set_text(str(lista0))
                resultado_lista_contraseña.set_text(str(lista1))
                resultado_lista_correo.set_text(str(lista2))
                resultado_lista_nombre.set_text(str(lista3))
                resultado_lista_apellido.set_text(str(lista4))
                resultado_lista_direccion.set_text(str(lista5))
	
        conexion.commit()
        conexion.close()
        ventana2.show()
        
#creamos el manipulador
builder=Gtk.Builder()
#creamos el conector e indicamos la base de datos
conexion=sqlite3.connect("tEjercicio")
cursor=conexion.cursor()
#INDICAMOS EL FICHERO DE GLADE
builder.add_from_file("P1_3_JonatanOrtiz.glade")

#INDICAMOS LOS EVENTOS Y LOS RELACIONAMOS
handlers ={
	"Terminar": Gtk.main_quit,
	"reposo":Gtk.main_quit,
	"aceptar_registro": aceptar_registro,
        "aceptar_dialogo":aceptar_dialogo,
        "cancelar_dialogo":cancelar_dialogo,
        "boton_listar": listar
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

resultado_lista_usuario=builder.get_object("lista_us")
resultado_lista_contraseña=builder.get_object("lista_co")
resultado_lista_correo=builder.get_object("lista_em")
resultado_lista_nombre=builder.get_object("lista_no")
resultado_lista_apellido=builder.get_object("lista_ap")
resultado_lista_direccion=builder.get_object("lista_di")



#MOSTRAMOS LA VENTANA PRINICPAL
window.show_all()

#MOSTRAMOS EL MAIN
Gtk.main()

