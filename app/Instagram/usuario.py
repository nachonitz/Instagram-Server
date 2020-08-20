from app.Instagram.InstagramAPI import InstagramAPI
import app.Instagram.media

class Usuario:
	def __init__(self, api, nombre_de_usuario):
		self.api = api
		self.nombre = nombre_de_usuario
		self.id = None
		self.id_posts = None
		self.medias = None

		self.seguidores = None
		self.seguidos = None

	def get_id(self):
		if self.id == None:
			id_usuario = self.api.searchUsername(self.nombre)
			id_usuario = str(self.api.LastJson['user']['pk'])
			self.id = id_usuario
		return self.id

	def get_nombre(self):
		return self.nombre

	def get_medias(self):
		if self.medias == None:
			self.get_id_posts()
		return self.medias
	def get_media(self,fila,columna): 
		numero_publicacion = 3*(fila-1) + columna
		return self.get_medias()[numero_publicacion-1]
	def get_id_posts(self):
		if self.id_posts != None:
			return self.id_posts

		fotos = []

		next_max_id = True

		while next_max_id:
			print('Buscando fotos...',flush = True, end = '\r')
			# first iteration hack
			if next_max_id is True:
				next_max_id = ''

			_ = self.api.getUserFeed(self.get_id(),maxid=next_max_id)
			fotos.extend(self.api.LastJson.get('items',[]))
			next_max_id = self.api.LastJson.get('next_max_id', '')
			
		ids=[]
		for x in fotos:
			ids.append(x["pk"])

		medias = []
		for id_media in ids:
			medias.append(media.Media(self.api,id_media))

		self.medias = medias

		self.id_posts = ids
		return ids

	def get_seguidores(self):
		if self.seguidores == None:
			seguidores = []
			tabla_followers = self.api.getTotalFollowers(self.get_id()) #Esto devuelve una lista de diccionarios con datos de los followers
			for usuario in tabla_followers: #recorro cada diccionario y me quedo solo con el username
				seguidores.append(usuario["username"])
			self.seguidores = seguidores

		return self.seguidores

	def get_seguidos(self):
		if self.seguidos == None:
			seguidos = []
			tabla_followings = self.api.getTotalFollowings(self.get_id()) #Esto devuelve una lista de diccionarios con datos de los followers
			for usuario in tabla_followings: #recorro cada diccionario y me quedo solo con el username
				seguidos.append(usuario["username"])
			self.seguidos = seguidos

		return self.seguidos

	def get_unfollowers(self):
		seguidores = self.get_seguidores()
		seguidos = self.get_seguidos()

		unfollowers = []

		for i in range(len(seguidos)):
			if not seguidos[i] in seguidores:
				unfollowers.append(seguidos[i])
		return unfollowers

	def get_fans(self):
		seguidores = self.get_seguidores()
		seguidos = self.get_seguidos()

		fans = []

		for i in range(len(seguidores)):
			if not seguidores[i] in seguidos:
				fans.append(seguidores[i])
		return fans