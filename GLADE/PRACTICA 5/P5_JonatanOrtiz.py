#!/usr/bin/python
from gi.repository import Gtk
import sqlite3

def ventana_estudiantes(button):
   #MUESTRO LA VENTANA 
   window2.show()
   
def aviso1(button):
    aviso.show()
    #PASO LOS DATOS DE UNA VENTANA A OTRA, CON USU CORRESPONDIENTES DATOS
    resultado_usuario.set_text(usuario.get_text())
    resultado_password.set_text(password.get_text())
    resultado_correo.set_text(email.get_text())
    resultado_nombre.set_text(nombre.get_text())
    resultado_apellido.set_text(apellido.get_text())
    resultado_direccion.set_text(direccion.get_text())
    
def guardar(button):
   #CREO VARIABLES Y GUARDO EN ELLAS LOS VALORES INTRODUCIDOS
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
   aviso.hide()
   
def no_guardar(button):
   #OCULTO LA VENTANA
   aviso.hide()

def autocompletar(button):
   treeview=builder.get_object("treeview1")
   #VAMOS A GUARDAR LO SELECCIONADO DEL TREEVIEW EN UNA VARIABLE
   selection=treeview.get_selection()
   #DECIMOS QUE EL MODELO Y LA POSICION SE GUARDEN 
   model,treeiter=selection.get_selected()
   #MIENTRAS HAYA ALGO SELECCIONADO, PASAMOS LOS PARAMETROS
   if treeiter != None:
         usuario.set_text(model[treeiter][0])
         password.set_text(model[treeiter][1])
         email.set_text(model[treeiter][2])
         nombre.set_text(model[treeiter][3])
         apellido.set_text(model[treeiter][4])
         direccion.set_text(model[treeiter][5])

def aviso2(button):
   #MUESTRO LA VENTANA E INDICO EL USUARIO A BORRAR
   aviso2.show()
   borrar.set_text(usuario.get_text())
   
def borrar(button):
   us=borrar.get_text()
   cursor.execute("DELETE FROM tusuario where usuario='"+us+"'")
   conexion.commit()
   #SI HAY UN ERROR, NO HACE EL DELETE
   conexion.rollback()
   aviso2.hide()
	
def no_borrar(button):
   #OCULTO LA VENTANA
   aviso2.hide()
   
def cerrar_ventana_estudiantes(button):
   #OCULTO LA VENTANA
   window2.hide()
   
def aviso3(button):
   #MUESTRO LOS LA VENTANA Y LOS DATOS NUEVOS QUE SE VAN A GUARDAR
   aviso3.show()
   mod_usuario.set_text(usuario.get_text())
   mod_password.set_text(password.get_text())
   mod_correo.set_text(email.get_text())
   mod_nombre.set_text(nombre.get_text())
   mod_apellido.set_text(apellido.get_text())
   mod_direccion.set_text(direccion.get_text())
   
def modificar(button):
   us=mod_usuario.get_text()
   ps=mod_password.get_text()
   co=mod_correo.get_text()
   no=mod_nombre.get_text()
   ap=mod_apellido.get_text()
   di=mod_direccion.get_text()
   #HE TOMADO EL USUARIO COMO IDENTIFICADOR,ASÍ QUE EL USUAIO NO SE PUEDE MODIFICAR
   cursor.execute("UPDATE tUsuario SET usuario='"+us+"',Contraseña='"+ps+"',Email='"+co+"',Nombre='"+no+"',Apellido='"+ap+"',Direccion='"+di+"'" +
   "WHERE usuario='"+us+"'");
   conexion.commit()
   #SI HAY UN ERROR EN ALGUN PARAMETRO, NO HACE EL UPDATE
   conexion.rollback()
   aviso3.hide()
   
def no_modificar(button):
   #OCULTO LA VENTANA
   aviso3.hide()
   
def actualizar(button):
   cursor.execute("SELECT * FROM tusuario")
   fila=cursor.fetchone()
        
   store=Gtk.ListStore(str,str,str,str,str,str)
   treeview=builder.get_object("treeview1")

   #MOSTRAMOS LOS DATOS
   for i in cursor.execute("SELECT * FROM tusuario"):
         us=str(fila[0])
         co=str(fila[1])
         em=str(fila[2])
         no=str(fila[3])
         ap=str(fila[4])
         di=str(fila[5])
         store.append(i)
                  
   #Asignamos la lista y la columna al TreeView
   treeview.set_model(store)
   
def vaciar(button):
   #LOS CAMPOS DE TEXTO SE VACIAN
   usuario.set_text("")
   password.set_text("")
   email.set_text("")
   nombre.set_text("")
   apellido.set_text("")
   direccion.set_text("")
   
   
#CREAMOS NUESTRO OBJECTO BUILDER
builder = Gtk.Builder()
#CREAMOS EL CONECTOR E INDICAMOS LA BASE DE DATOS
conexion=sqlite3.connect("tEjercicio")
cursor=conexion.cursor()
#INDICAMOS EL FICHERO .GLADE
builder.add_from_file("P5_JonatanOrtiz.glade")
#INDICAMOS LAS SEÑALES
handlers={
    "cerrar_programa": Gtk.main_quit,
    "abrir_estudiantes": ventana_estudiantes,
    "aviso": aviso1,
    "guardar_registro":guardar,
    "cancelar_registro": no_guardar,
    "seleccionar": autocompletar,
    "aviso2":aviso2,
    "borrar_registro":borrar,
    "cancelar_borrar":no_borrar,
    "cerrar_estudiantes":cerrar_ventana_estudiantes,
    "aviso3":aviso3,
    "cambiar":modificar,
    "no_cambiar":no_modificar,
    "refrescar":actualizar,
    "limpiar":vaciar
    
}
#CONECTAMOS LAS SEÑALES
builder.connect_signals(handlers)

#GUARDAMOS EN UNA VARIABLE LOS OBJETOS QUE VAMOS A NECESITAR DE GLADE
window = builder.get_object("ventana_principal")
window2 = builder.get_object("ventana_estudiantes")
aviso = builder.get_object("advertencia1")
aviso2 = builder.get_object("advertencia2")
aviso3 = builder.get_object("advertencia3")

#PARA EL REGISTRO
usuario = builder.get_object("entrada_usuario")
password = builder.get_object("entrada_contraseña")
#PARA QUE NO SE VEA LA CONTRASEÑA INTRODUCIDA
password.set_visibility(False)
email = builder.get_object("entrada_correo")
nombre = builder.get_object("entrada_nombre")
apellido = builder.get_object("entrada_apellido")
direccion = builder.get_object("entrada_direccion")

#PARA NUEVO
resultado_usuario=builder.get_object("etiqueta_usuario")
resultado_password=builder.get_object("etiqueta_password")
resultado_correo=builder.get_object("etiqueta_correo")
resultado_nombre=builder.get_object("etiqueta_nombre")
resultado_apellido=builder.get_object("etiqueta_apellido")
resultado_direccion=builder.get_object("etiqueta_direccion")

#PARA BORRAR
borrar=builder.get_object("borrar_usuario")

#PARA MODIFICAR
mod_usuario=builder.get_object("mod_usuario")
mod_password=builder.get_object("mod_password")
mod_correo=builder.get_object("mod_correo")
mod_nombre=builder.get_object("mod_nombre")
mod_apellido=builder.get_object("mod_apellido")
mod_direccion=builder.get_object("mod_direccion")

#-----AQUÍ ABAJO HACEMOS EL TREEVIEW INICIAL---------

cursor.execute("SELECT * FROM tusuario")
fila=cursor.fetchone()
        
store=Gtk.ListStore(str,str,str,str,str,str)
treeview=builder.get_object("treeview1")

#MOSTRAMOS LOS DATOS
for i in cursor.execute("SELECT * FROM tusuario"):
      us=str(fila[0])
      co=str(fila[1])
      em=str(fila[2])
      no=str(fila[3])
      ap=str(fila[4])
      di=str(fila[5])
      store.append(i)
                
      #CREO LAS COLUMNAS
      render=Gtk.CellRendererText()
      columna1=Gtk.TreeViewColumn("USUARIO",render,text=0)
      columna2=Gtk.TreeViewColumn("CONTRASEÑA",render,text=1)
      columna3=Gtk.TreeViewColumn("CORREO",render,text=2)
      columna4=Gtk.TreeViewColumn("NOMBRE",render,text=3)
      columna5=Gtk.TreeViewColumn("APELLIDO",render,text=4)
      columna6=Gtk.TreeViewColumn("DIRECCION",render,text=5)
        
#Asignamos la lista y la columna al TreeView
treeview.set_model(store)
treeview.append_column(columna1)
treeview.append_column(columna2)
treeview.append_column(columna3)
treeview.append_column(columna4)
treeview.append_column(columna5)
treeview.append_column(columna6)
#MOSTRAMOS EL TREEVIEW
treeview.show()

#---------SE TERMINA EL TREEVIEW INICIAL-----------------

#MOSTRAMOS VENTANA PRINCIPAL Y EL PROGRAMA
window.show_all()
Gtk.main()
