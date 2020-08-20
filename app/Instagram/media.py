class Media:
	def __init__(self,api,media_id):
		self.id = media_id
		self.api = api
		self.likes = None
		self.comentarios = None
	def get_id(self):
		return self.id

	def get_likes(self):
		if self.likes != None:
			return self.likes
		me_gustas = []
		info = self.api.getMediaLikers(str(self.id))
		info = self.api.LastJson
		for usuarios in info["users"]:
			me_gustas.append(usuarios["username"])
		self.likes = me_gustas
		return me_gustas

	def get_comments(self):
		if self.comentarios != None:
			return self.comentarios
		comentarios = {}
		next_max_id = ''
		while 1:
			self.api.getMediaComments(str(self.id), next_max_id)
			temp = self.api.LastJson
			for dicc in temp['comments']:
				comentador = dicc['user']['username']
				if comentador not in comentarios:
					comentarios[comentador] = 1
				else:
					comentarios[comentador] += 1
			if temp['has_more_comments'] is False:
				break
			next_max_id = temp["next_max_id"]
			print(temp)
		self.comentarios = comentarios
		return comentarios


'''
			for item in temp["users"]:
				followers.append(item)

'''