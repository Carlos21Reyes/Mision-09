#Autor: Carlos Alberto Reyes Ortiz
#Matricula: A01376349
#Programa con 6 ejercicios sobre listas



def extraerPares(listaNumEnteros): #Extrae los pares de la lista dada y los coloca en una lista nueva

    listaNumPares = []

    for k in listaNumEnteros:
        if k %2 == 0:
            listaNumPares.append(k)
    return listaNumPares



def extraerMayoresPrevio(lista): #Extrae los valores que son mayores a un elemento previo y los coloca en una lista nueva

    listaMayoresPrevio = []

    for k in range(1, len(lista)):
        if lista[k] > lista[k-1]:
            listaMayoresPrevio.append(lista[k])
    return listaMayoresPrevio



def intercambiarParejas(lista): # De la lista dada intercambia las posiciones de los numeros por parejas en una lista nueva

    listaIntercambiada = []

    for k in range(len(lista)):
        if k %2 == 0:
            listaIntercambiada.append(lista[k])
        else: listaIntercambiada.insert(k-1, lista[k])
    return listaIntercambiada



def intercambiarMM(lista): #De la lista dada intercambia los el dato mayor y menor de posición

    if lista == []:
        pass

    else:
        minimo = min(lista)
        maximo = max(lista)

        posMin = lista.index(minimo)
        posMax = lista.index(maximo)

        lista.remove(lista[posMin])
        lista.remove(lista[posMax])

        lista.insert(posMin, maximo)
        lista.insert(posMax, minimo)

    return lista



def promediarCentro(lista): #De una lista dada regresa el promedio entero

    if len(lista) <= 2:
        return 0

    else:
        listaNueva = lista.copy()
        listaNueva.remove(min(listaNueva))
        listaNueva.remove(max(listaNueva))
        promedio = sum(listaNueva) // len(listaNueva)

        return promedio



def calcularEstadistica(lista): # De una lista dada regresa la media y la desviación estándar

    if len(lista) == 0:
        return (0, 0)

    else:
        media = sum(lista) / len(lista)

        distancia = []

        for k in lista:
            distancia.append((k - media) ** 2)

        desviacionEstandar = (sum(distancia) / (len(lista) - 1)) ** 0.5

        return (media, desviacionEstandar)




