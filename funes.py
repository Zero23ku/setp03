import re   #modulo contiene la funcion popitem, que elimina un elemento de un diccionario y lo asignas a variables 
import sys  #modulo que contiene la funcion setrecursionlimit que limita la cantidad de llamadas recursivas de una funcion, evitando overflows

sys.setrecursionlimit(100000)	#se define la cantidad maxima de llamadas recursivas

def cuenta_palabras(diccionario):       #funcion que cuenta las palabras totales de un archivo de texto a partir del diccionario previamente creado
	if (len(diccionario)==0):       #Si el largo del diccionario es 0, se retorna 0
		return(0)
	else:                           #Si el largo del diccionario no es 0
		palabra,veces=diccionario.popitem()      #Se quita un elemento del diccionario, guardando su key es la variable 'palabra' y su valor asociado en la variable 'veces'
		return(cuenta_palabras(diccionario)+int(veces)) #Se vuelve llamar a la funcion enviando el diccionario con un elemento menos, sumandole la variable 'veces' a lo que retorne dicha llamada
      
diccionario_texto={} #Se genera el diccionario vacio para ser llenado

archivo=open('funes.txt',encoding='utf-8') #Archivo abierto
texto=archivo.read()   #guarda todo el texto en forma de String en la variable "texto"
archivo.close()         #cierra el archivo
texto=texto.lower()   #Deja el string solo con minisculas
lista_texto = texto.split()   #Genera una lista con todas las palabras, incluso repetidas
diccionario_texto = dict.fromkeys(lista_texto,0)  #crea un diccionario a partir de la lista previamente creada, cada valor asociado al key del diccionario es inicializada con el valor 0

#Recorre la lista con las palabras del texto
for i in lista_texto:

    #Si la palabra que está en la lista se encuentra en el diccionario se suma 1 al valor de la respectiva 'key' en el diccionario
    if i in diccionario_texto:
        diccionario_texto[i] = int(diccionario_texto[i]+1)

#Se crea una lista que contiene tuplas de cada 'key' del diccionario con su respectivo valor, ordenadas por su valor de mayor a menor
from operator import itemgetter
diccionario_listo=sorted(diccionario_texto.items(), key=itemgetter(1), reverse=True)  #reverse ordena las palabras de mayor a menor

#Imprime la lista de tuplas ya ordenada


for i in diccionario_listo:
    print(i)

print("La cantidad de palabras es:",cuenta_palabras(diccionario_texto))    #imprime la cantidad de palabras que contiene el archivo
