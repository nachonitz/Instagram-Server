import random

def es_lista_nula(lista):
	for i in range(len(lista)):
		if (lista[i]!=0):
			return False
	return True


'''
Recibe una lista con los usuarios a etiquetar y la cantidad de etiquetados por comentario
Devuelve una lista con todas las combinaciones posibles de comentarios
'''
def combinatoria_random(lista, x):
	n = len(lista)
	combinacion_actual = []
	for i in range(x):
		combinacion_actual.append(0)

	tabla = {}
	comentarios = []

	iteraciones = 0

	while((not es_lista_nula(combinacion_actual)) or (iteraciones == 0)):
		repetido = False

		#Con esto siguiente hago backtracking
		for i in range(1,x):
			if repetido:
				break
			for j in range(i):
				if combinacion_actual[i] == combinacion_actual[j]:
					aumentar_1(combinacion_actual,i+1,n)
					repetido = True
					break
		if repetido:
			continue

		#ACA ESTAS ADENTRO DEL "FOR"
		indices = combinacion_actual[:]
		comentarios_actuales = []
		indices.sort()
		valores_actuales = ""
		for l in range(x):
			valores_actuales+="{}".format(indices[l])
			comentarios_actuales.append(lista[indices[l]])

		if (not valores_actuales in tabla):
			tabla[valores_actuales] = True
				
			random.shuffle(comentarios_actuales)
			comentarios.append(comentarios_actuales)



		#ACA TERMINA EL FOR
		aumentar_1(combinacion_actual,x,n)
		iteraciones+=1
	#print(iteraciones)
	#print(len(tabla))
	#print(tabla.keys())
	random.shuffle(comentarios)
	#print(comentarios)


	return comentarios

#FUNCION PARA SIMULAR LOS FORS ANIDADOS
def aumentar_1(combinacion_actual, x, n):
	if combinacion_actual[x-1] == n-1:
		for j in range(x):
			if combinacion_actual[x-1-j] < n-1:
				combinacion_actual[x-1-j] += 1
				break

			else:
				combinacion_actual[x-1-j] = 0
	else:
		combinacion_actual[x-1] += 1
