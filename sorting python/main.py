import random

from selection import *

lista_elementos = []
max_elems = 10
rango_elems = 8

for elem in range(max_elems):
    lista_elementos.append(random.randint(1, rango_elems))

print("######## Implementacion Normal ########")
print("Unsorted = %s" % lista_elementos)

lista_elementos_ordRelativo = []
for elem in range(len(lista_elementos)):
    lista_elementos_ordRelativo.append((lista_elementos[elem], elem+1))

print("Unsorted w/ input order = %s" % lista_elementos_ordRelativo)
print("")

lista_elementos_2 = lista_elementos_ordRelativo.copy()

selection_sort(lista_elementos)
selection_sort_tuplas(lista_elementos_ordRelativo)

print("Sorted = %s" % lista_elementos)
print("Sorted w/ input order = %s" % lista_elementos_ordRelativo)

print("")
print("Conclusion: La implementacion mediante swaps no es estable")
print("")

print("######## Implementacion Modificada (inserciones) ########")
print("Unsorted = %s" % lista_elementos_2)

selection_sort_tuplas_estable(lista_elementos_2)

print("Sorted insertando w/ input order = %s" % lista_elementos_2)
print("")
print("Conclusion: La implementacion mediante insercion del primer minimo es estable, pero es mas costosa que insertion sort.")
print("Es O(2n*n) en peor caso mientras que insertion es O(n*n) en peor caso")
print("")
