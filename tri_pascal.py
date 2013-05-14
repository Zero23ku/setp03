
def tri_pascal(n):      #Funcion que retorna un nivel n del triangulo de pascal
	if n==0:        #Si el nivel es 0, retorna una lista con un 1
		
		return [1]
	else:           #Si el nivel no es 0
		nivel=[1]       #Nivel actual se inicializa con una lista con un 1
		base_anterior=tri_pascal(n-1)   #Se calcula el nivel anterior del triangulo
		for i in range(len(base_anterior)-1):   #Se recorre el nivel anterior del triangulo hasta su penultimo elemento
			nivel.append(base_anterior[i]+base_anterior[i+1])       #El nuevo elemento del nivel actual del triangulo se construye tomando los dos valores del nivel anterior del triangulo que correspondan
		nivel.append(1) #Se le agrega un 1 al final del nivel actual del triangulo
		return nivel    #Se retorna el nivel actual del triangulo


n=eval(input("Ingrese el nivel del triangulo de pascal que desea ver: "))
print(tri_pascal(n))
