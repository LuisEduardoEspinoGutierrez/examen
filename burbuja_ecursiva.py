
# Función de utilidad para intercambiar valores en dos índices de la lista
def intercambio(arreglo, i, j):
 
    temp = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = temp
 
 
# Función para realizar la ordenación 
def burbujaRecursiva(arreglo):
 
    for k in range(len(arreglo) - 1):
        # Los últimos elementos de k ya están ordenados, por lo que el ciclo interno puede
        # evitar mirar los últimos elementos de k
        for i in range(len(arreglo) - 1 - k):
            if arreglo[i] > arreglo[i + 1]:
                intercambio(arreglo, i, i + 1)
    # el algoritmo se puede terminar si el bucle interno no hizo ningún intercambio

arreglo = [3, 5, 8, 4, 1, 9, -2]
print('lista: ',arreglo)
burbujaRecursiva(arreglo)
# imprime la lista 
print('lista ordenados: ',arreglo)