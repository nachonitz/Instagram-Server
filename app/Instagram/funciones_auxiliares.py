import smtplib, ssl
from app.Instagram.InstagramAPI import InstagramAPI
import pickle #PARA GUARDAR OBJETO
import os #Para crear directorio

def enviar_mail(asunto,n_comentario, cantidad_total, i,n_iter, tiempo_restante):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "nachonitz@gmail.com"  # Enter your address
	receiver_email = "nachonitz@gmail.com"  # Enter receiver address
	password = "NewtonLeibniz100710"

	if (asunto == "Reporte"):

		message = """\
Subject: Reporte de comentarios

Hola nacho, te informamos como vienen los comentarios:

Cantidad total de comentarios: {}/{}
En esta ejecucion venimos asi: {}/{}
Tiempo total restante: {}""".format(n_comentario,cantidad_total,i,n_iter,tiempo_restante)
	
	if (asunto == "Fin"):
		message = """\
Subject: Terminamos de comentar con exito

Hola nacho, te informamos que ya terminamos de comentar!
Todo salio segun lo esperado.

INFORME
Cantidad total de comentarios en la publicacion: {}/{}
En esta ejecucion: {}/{}""".format(n_comentario,cantidad_total,i,n_iter)

	if (asunto == "Spam"):
		message = """\
Subject: Nos han detectado spam!

Hola nacho, lamentamos informarte que nos han detectado spam en Instagram.
Hemos cortado la ejecucion del programa.

Cantidad de comentarios: {}/{}
En esta ejecucion se logro: {}/{}""".format(n_comentario,cantidad_total,i,n_iter)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)






'''
Recibe una lista de strings, la devuelve sin el \n
'''
def sacar_fin(lista):
	for i in range(len(lista)):
		if lista[i][-1] == '\n':
			lista[i] = lista[i][0:-1]
	return lista



def aplicar_splits(lista):
	for i in range(len(lista)):
		lista[i] = lista[i].split()



def sacar_ya_comentados(todos_los_comentarios,ya_comentados):
	for i in range(len(ya_comentados)):
		comentario_actual = ya_comentados[i]
		todos_los_comentarios.remove(comentario_actual)


def save_api(obj, filename):
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_api(filename):
	with open(filename, 'rb') as input:
		api = pickle.load(input)
		return api

def login(usuario):
	filename = "app/Instagram/Apis/{}".format(usuario)
	if os.path.exists(filename):
		api = load_api(filename)
		return api

	cuentas = []
	with open('app/Instagram/cuentas.txt','r') as file:
		cuentas = file.readlines()
		aplicar_splits(cuentas)

	for i in range(len(cuentas)):
		if (usuario == cuentas[i][0]):
			api = InstagramAPI(cuentas[i][0], cuentas[i][1])
			api.login()
			save_api(api,filename)
			return api
	raise Exception('No se pudo conectar a la cuenta especificada.')