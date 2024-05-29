def quicksort(list, menor, mayor):
    # Si el índice menor es menor al índice mayor
    if menor < mayor:
        # Seleccionamos el pivote
        pivote = list[mayor]
        # Inicializamos el último menor
        ultimo_menor = menor - 1
        # Recorremos la lista
        for i in range(menor, mayor):
            # Si el elemento actual es menor o igual al pivote
            if list[i] <= pivote:
                # Incrementamos el último menor
                ultimo_menor += 1
                # Intercambiamos los elementos
                list[ultimo_menor], list[i] = list[i], list[ultimo_menor]
        # Intercambiamos el último menor + 1 con el pivote
        list[ultimo_menor + 1], list[mayor] = list[mayor], list[ultimo_menor + 1]
        # Obtenemos la posición del pivote
        posicion_pivote = ultimo_menor + 1
        # Orden de los elementos menores al pivote
        quicksort(list, menor, posicion_pivote - 1)
        # Orden de los elementos mayores al pivote
        quicksort(list, posicion_pivote + 1, mayor)

# Prueba de funcionamiento
list = [4,6,2,5,8,9,5,10]
print(list)
quicksort(list,0,len(list)-1)
print(list)