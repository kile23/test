import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Dialogo_error(Gtk.Dialog):
    def __init__(self,parent):
	Gtk.Dialog.__init__(self,"Error",parent,0,(Gtk.STOCK_OK, Gtk.ResponseType.OK))
	self.set_modal(1)
	self.set_default_size(150,100)
	label = Gtk.Label("Se ha producido un error en la operacion")
	box = self.get_content_area()
	box.add(label)
	self.show_all()


class Dialogo_borrar(Gtk.Dialog):
    def __init__(self,parent):
	Gtk.Dialog.__init__(self,"Confirmar borrado",parent,0,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))
	self.set_modal(1)
	self.set_default_size(150,100)
	label = Gtk.Label("Seguro que quieres borrar la pelicula")
	box = self.get_content_area()
	box.add(label)
	self.show_all()
	

class Dialogo_agregar(Gtk.Dialog):
    def __init__(self,parent):
	Gtk.Dialog.__init__(self,"Agregar pelicula",parent,0,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))
	self.set_modal(1)
	self.set_default_size(150,100)
	label = Gtk.Label("Inserte los datos de la pelicula")
	box = self.get_content_area()
	box.add(label)
	
	self.titulo = Gtk.Entry()
	self.titulo.set_text("Titulo...")
	self.titulo.set_editable(1)
	box.add(self.titulo)
	
	self.genero = Gtk.Entry()
	self.genero.set_text("Genero...")
	self.genero.set_editable(1)
	box.add(self.genero)

	self.estado = Gtk.Entry()
	self.estado.set_text("Estado...")
	self.estado.set_editable(1)
	box.add(self.estado)
	self.show_all()


class Dialogo_editar(Gtk.Dialog):
    def __init__(self,parent,ntitulo,ngenero,nestado):
	Gtk.Dialog.__init__(self,"Editar pelicula",parent,0,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))
	self.set_modal(1)
	self.set_default_size(150,100)
	label = Gtk.Label("Inserte los datos de la pelicula")
	box = self.get_content_area()
	box.add(label)
	
	self.titulo = Gtk.Entry()
	self.titulo.set_text(ntitulo)
	self.titulo.set_editable(1)
	box.add(self.titulo)
	
	self.genero = Gtk.Entry()
	self.genero.set_text(ngenero)
	self.genero.set_editable(1)
	box.add(self.genero)

	self.estado = Gtk.Entry()
	self.estado.set_text(nestado)
	self.estado.set_editable(1)
	box.add(self.estado)
	self.show_all()
	

class peliculas(Gtk.Window):
    def __init__(self,handler):
        Gtk.Window.__init__(self, title="Peliculas")
        self.set_border_width(10)
	self.handler = handler

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)
	#Crear el modelo
	self.store = self.create_model(self.handler.Get_list())

        #Crear treeview y permitir la seleccion de elementos
        self.treeview = Gtk.TreeView(self.store)
	self.create_columns(self.treeview)
	select = self.treeview.get_selection()
	select.connect('changed',self.on_select_change)

	#Botones de Agregar,Borrar y Editar
        self.buttons = list()        
	button = Gtk.Button("Agregar")
        self.buttons.append(button)
        button.connect("clicked", self.handler.Agregar)

	button = Gtk.Button("Borrar")
        self.buttons.append(button)
        button.connect("clicked", self.handler.Borrar)

	button = Gtk.Button("Editar")
        self.buttons.append(button)
        button.connect("clicked", self.handler.Editar)
	
	#Crear Scroll y aagregar los botones debajo
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
        self.scrollable_treelist.add(self.treeview)
	self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def create_columns(self, treeview):
	 for i, column_title in enumerate(["Titulo", "Genero", "Estado"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)


    def create_model(self,lista):
	store = Gtk.ListStore(str,str,str)
	for movie_ref in lista:
            store.append(list(movie_ref))
	return store


    def on_select_change(self,select):
	(model, pathlist) = select.get_selected_rows()
	for path in pathlist:
		tree_iter = model.get_iter(path)
		self.titulo_seleccionado = model.get_value(tree_iter,0)
		self.genero_seleccionado = model.get_value(tree_iter,1)
		self.estado_seleccionado = model.get_value(tree_iter,2)


    def dialogo_borrar(self):
	diag = Dialogo_borrar(self)
	response = diag.run()
	if response == Gtk.ResponseType.OK: 
		diag.destroy()
		return [self.titulo_seleccionado]
	else:
		diag.destroy()
		return []

    def dialogo_agregar(self):
	diag = Dialogo_agregar(self)
	response = diag.run()
	if response == Gtk.ResponseType.OK: 
		peli= [diag.titulo.get_text(),diag.genero.get_text(),diag.estado.get_text()]
		diag.destroy()
		return peli
	else:
		diag.destroy()
		return []
		

    def dialogo_editar(self):
	diag = Dialogo_editar(self,self.titulo_seleccionado,self.genero_seleccionado,self.estado_seleccionado)
	response = diag.run()
	if response == Gtk.ResponseType.OK: 
		peli= [self.titulo_seleccionado,diag.titulo.get_text(),diag.genero.get_text(),diag.estado.get_text()]
		diag.destroy()
		return peli
	else:
		diag.destroy()
		return []
	
	
    def dialogo_error(self):
	diag = Dialogo_error(self)
	response = diag.run()
	if response == Gtk.ResponseType.OK: 
		diag.destroy()
	else:
		diag.destroy()
