import usuario
import combinatoria
import random as rnd
import time
import funciones_auxiliares as fa
import os #Para crear directorio

class Sorteo:
	RUTA_COMENTARIOS = 'Sorteos/Comentarios/'
	RUTA_IDS = 'Sorteos/Ids/'
	def __init__(self,api,yo,pagina):
		self.api = api
		self.pagina = usuario.Usuario(api,pagina)
		self.yo = usuario.Usuario(api,yo)


		self.crear_directorio()
		self.id_post = self.buscar_id_post() #Busca en Ids, y si no esta lo crea

		self.archivo_todos = "{}{}/{}/todos.txt".format(Sorteo.RUTA_COMENTARIOS,self.yo.get_nombre(),self.pagina.get_nombre())
		self.archivo_comentados = "{}{}/{}/comentados.txt".format(Sorteo.RUTA_COMENTARIOS,self.yo.get_nombre(),self.pagina.get_nombre())

		if not os.path.exists(self.archivo_todos): #Si no existe el archivo con todos los comentarios --> lo crea
			self.hacer_archivo_comentarios()

	def crear_directorio(self):
		nombre_yo = self.yo.get_nombre()
		nombre_pagina = self.pagina.get_nombre()

		if not os.path.exists('Sorteos/Comentarios/{}'.format(nombre_yo)):
			os.makedirs('Sorteos/Comentarios/{}'.format(nombre_yo), exist_ok=True)

		ruta = 'Sorteos/Comentarios/{}/{}'.format(nombre_yo,nombre_pagina)

		if not os.path.exists(ruta):
			print('creando')
			
			os.makedirs(ruta, exist_ok=True)


	def buscar_id_post(self):
		directorio = Sorteo.RUTA_IDS+self.pagina.get_nombre()
		if os.path.exists(directorio):
			with open(directorio,'r') as file:
				id_post = file.readline()
				return id_post

		fila = int(input("Ingrese numero de fila: "))
		columna = int(input("Ingrese numero de columna: "))

		id_post = self.pagina.get_media(fila,columna).get_id()

		with open(directorio,'w') as file:
			file.write(str(id_post))

		return id_post

	'''
	Devuelve la lista con todos los comentarios
	'''
	def dar_comentarios_totales(self):
		todos_los_comentarios = []
		with open(self.archivo_todos,'r') as file:
			todos_los_comentarios = file.readlines()
			fa.aplicar_splits(todos_los_comentarios)

		return todos_los_comentarios


	'''
	Devuelve la lista con los comentarios restantes
	'''
	def dar_comentarios_restantes(self):
		restantes = self.dar_comentarios_totales()
		with open(self.archivo_comentados,'r') as file:
			lineas = file.readlines()
			fa.aplicar_splits(lineas)
			fa.sacar_ya_comentados(restantes,lineas)
		return restantes

	def hacer_archivo_comentarios(self):
		archivo_usuarios = "usuarios_nachonn.txt"
		comentados = []
		with open (archivo_usuarios,'r') as file:
			comentados = file.readlines()
			comentados = fa.sacar_fin(comentados)
			cantidad_de_comentados = len(comentados)
		cantidad_por_comentario = int(input("Ingrese la cantidad de etiquetados por comentario: "))
		comentarios = combinatoria.combinatoria_random(comentados,cantidad_por_comentario)
		
		with open(self.archivo_todos,'w') as file:
			cantidad = len(comentarios)
			for i in range(cantidad):
				for j in range(cantidad_por_comentario):
					if (i == cantidad-1 and j == cantidad_por_comentario-1):#SI ESTAS EN EL ULTIMO COMENTARIO, EN EL ULTIMO COMENTADO
						file.write('{}'.format(comentarios[i][j]))
					if (j == cantidad_por_comentario-1 and i != cantidad-1):# SI ESTAS EN CUALQUIER COMENTARIO, EN EL ULTIMO COMENTADO
						file.write('{}\n'.format(comentarios[i][j]))
					if (j != cantidad_por_comentario-1):#SI ESTAS EN CUALQUIER COMENTADO
						file.write('{} '.format(comentarios[i][j]))

		with open(self.archivo_comentados,'w') as file:
			pass


	def spamear(self,cantidad,sleep):
		cantidad_total = len(self.dar_comentarios_totales())
		restantes = self.dar_comentarios_restantes()
		cantidad_restante = len(restantes)
		n_comentario = cantidad_total - cantidad_restante

		tiempos = 0

		if len(restantes) > 0:
			cantidad_por_comentario = len(restantes[0])
		with open(self.archivo_comentados,'a') as file:
			
			for i in range(cantidad):
				tiempo_restante = ((sleep+2.5)*(cantidad - i))/60
				comentados_con_arroba = ""
				comentados_sin_arroba = ""
				for j in range(cantidad_por_comentario):
					if j == cantidad_por_comentario-1:
						comentados_sin_arroba+= restantes[i][j]
						comentados_con_arroba+= '@' + restantes[i][j]
					else:
						comentados_sin_arroba+= restantes[i][j] + ' '
						comentados_con_arroba+= '@' + restantes[i][j] + ' '

				print('{}/{}\tComentario: {}\tTiempo restante promedio: {} minutos'.format(n_comentario+1,cantidad_total,comentados_con_arroba,tiempo_restante))

				tiempo_inicial =time.time()
				comento = self.api.comment(self.id_post,'{}'.format(comentados_con_arroba))
				tiempos += time.time()-tiempo_inicial
				if (not comento):
					print("Cortamos la ejecucion por spam")
					#fa.enviar_mail("Spam", n_comentario+1, cantidad_total,i+1,cantidad,tiempo_restante)
					return


				if (i%100 == 0 and i != 0):
					#fa.enviar_mail("Reporte",n_comentario+1,cantidad_total,i+1,cantidad,tiempo_restante)
					pass
				file.write('{}\n'.format(comentados_sin_arroba))



				if (i == cantidad - 1):
					#fa.enviar_mail("Fin",n_comentario+1,cantidad_total,i+1,cantidad,tiempo_restante)
					print(tiempos)
					return

				n_comentario += 1
				#tiempo = rnd.choice([sleep-1,sleep,sleep+1])
				#enviar_informacion(tiempo)
				time.sleep(sleep)
