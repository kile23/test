import json

class lista():

	def __init__(self):
		self.data = open('peliculas.json')
		self.peliculas = json.load(self.data) 

	def Actualizar(self):
		self.data = open('peliculas.json')
		self.peliculas = json.load(self.data)

	def Agregar(self, lista):
		with open('peliculas.json', mode='w') as add:
    			entry = {'Titulo': lista[0], 'Genero': lista[1],'Estado':lista[2]}
    			self.peliculas.append(entry)
    			json.dump(self.peliculas, add)
		self.Actualizar()
		
	def Get_list(self):
		lista_tmp = []
		for i in self.peliculas:
			element = (i['Titulo'],i['Genero'],i['Estado'])
			lista_tmp.append(element)
		return lista_tmp


	def Borrar(self, titulo):
		for i in xrange(len(self.peliculas)):
			if self.peliculas[i]['Titulo'] == titulo:
				self.peliculas.pop(i)
				break;
		open("peliculas.json", "w").write(
    json.dumps(self.peliculas, sort_keys=True, indent=0, separators=(',', ': ')))
		self.Actualizar()
		
	def Editar(self, lista):
		for i in xrange(len(self.peliculas)):
			if self.peliculas[i]['Titulo'] == lista[0]:
				self.peliculas[i]['Titulo'] = lista[1]
				self.peliculas[i]['Genero'] = lista[2]
				self.peliculas[i]['Estado'] = lista[3]
				break;
		open("peliculas.json", "w").write(
    json.dumps(self.peliculas, sort_keys=True, indent=0, separators=(',', ': ')))
		self.Actualizar()


	def Existe(self,titulo):
		for i in xrange(len(self.peliculas)):
			if self.peliculas[i]['Titulo'] == titulo:
				return True
				break;
		return False


	def Estado_incorrecto(self,estado):
		estados_posibles = {'Vista','Pendiente','Recomendada'}
		if estado in estados_posibles:
			return False
		else:
			return True
