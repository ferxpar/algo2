#selection sort
def selection_sort(array):
    for i in range(1, len(array) - 1):
        min_index = _find_min(array, desde = i-1)
        array[min_index], array[i-1] = array[i-1], array[min_index]
    return array

def selection_sort_tuplas(array):
    for i in range(1, len(array) - 1):
        min_index = _find_min_tuplas(array, desde = i-1, pos_tupla = 0)
        array[min_index], array[i-1] = array[i-1], array[min_index]
    return array

def selection_sort_tuplas_estable(array):
    for i in range(1, len(array) - 1):
        min_index = _find_min_tuplas(array, desde = i-1, pos_tupla = 0)
        temp = array[min_index]
        for j in reversed(range(i-1, min_index)):
            array[j+1] = array[j]
        array[i-1] = temp
    return array

#encontrar minimo
def _find_min(array, desde):
    index = desde
    for elem in range(desde, len(array)):
        if array[elem] < array[index]:
            index = elem
    return index

def _find_min_tuplas(array, desde, pos_tupla):
    index = desde
    for elem in range(desde, len(array)):
        if array[elem][pos_tupla] < array[index][pos_tupla]:
            index = elem
    return index
