from InstagramAPI import InstagramAPI
import usuario

class Cuenta:
	def __init__(self, api, nombre_de_usuario):
		self.api = api
		self.mi_usuario = usuario.Usuario(api,nombre_de_usuario)

	def likear_foto_de(self, nombre_de_usuario, fila, columna):
		usuario_likeado = usuario.Usuario(self.api, nombre_de_usuario)
		media = usuario_likeado.get_media(fila,columna)
		id_media = media.get_id()
		self.api.like(id_media)

	def seguir_usuario(self, nombre_de_usuario):
		usuario_a_seguir = usuario.Usuario(self.api, nombre_de_usuario)
		id_usuario = usuario_a_seguir.get_id()
		self.api.follow(id_usuario)