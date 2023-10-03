
def burbuja(arreglo):
    tamaño = len(arreglo)  # Obtenemos el tamaño de la lista
    for i in range(tamaño):  # Iteramos a través de todos los elementos de la lista
        intercambio = False  # Creamos una variable para rastrear si se han realizado intercambios en esta pasada
        for j in range(0, tamaño-i-1):  # Iteramos a través de los elementos no ordenados
            if arreglo[j] > arreglo[j+1]:  # Si el elemento actual es mayor que el siguiente elemento
                # Realizamos el intercambio de elementos
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True  # Marcamos que se ha realizado un intercambio en esta pasada
        # Si no se ha realizado ningún intercambio en esta pasada, la lista está ordenada
        if not intercambio:
            break

arreglo = [64, 34, 25, 12, 22, 11, 90]
print('lista: ',arreglo)
burbuja(arreglo)
print("Lista ordenada:",arreglo)

