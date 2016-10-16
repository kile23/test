import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import Modelo
import Vista
class Handler():
	def __init__(self):
		self.modelo = Modelo.lista()
		self.vista = Vista.peliculas(self)


	def Get_list(self):
		lista = self.modelo.Get_list()
		return lista

	def Agregar_modelo(self,lista):
		if self.modelo.Existe(lista[0]) or self.modelo.Estado_incorrecto(lista[2]) == True:
			return False
		else:
			self.modelo.Agregar(lista)
			return True

	def Borrar_modelo(self,titulo):
		self.modelo.Borrar(titulo)

	def Editar_modelo(self,lista):
		if lista[0] == lista[1]:
			if self.modelo.Estado_incorrecto(lista[3]) == True:
				return False
			else:
				self.modelo.Editar(lista)
				return True
		else:
			if self.modelo.Estado_incorrecto(lista[3]) or self.modelo.Existe(lista[1]) == True:
				return False
			else:
				self.modelo.Editar(lista)
				return True
#----------SIGNALS-------
	def Agregar(self, widget):
		peli = self.vista.dialogo_agregar()
		if peli != []:
			if self.Agregar_modelo(peli) == True:
				self.vista.treeview.set_model(self.vista.create_model(self.modelo.Get_list()))
			else:
				self.vista.dialogo_error()

	def Editar(self,widget):
		peli = self.vista.dialogo_editar()
		if peli!= []:
			if self.Editar_modelo(peli) == True:
				self.vista.treeview.set_model(self.vista.create_model(self.modelo.Get_list()))
			else:
				self.vista.dialogo_error()

	def Borrar(self, widget):
		peli = self.vista.dialogo_borrar()
		if peli != []:
			self.Borrar_modelo(peli[0])
			self.vista.treeview.set_model(self.vista.create_model(self.modelo.Get_list()))
			

#----------MAIN----------
handler = Handler()

Gtk.main()
