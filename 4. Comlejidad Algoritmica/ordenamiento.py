# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 06:57:51 2023

@author: HP
"""

def sumarValor(lista, valor):
    for i in range(len(lista)):
        lista[i] += valor
        
    return 


def ordenar(lista):
    listaAuxiliar = lista.copy()
    listaOrdenada = []
    iteraciones = 0
    for i in range(len(lista)):                     #O(n)
        minimo = listaAuxiliar[0]
        for k in range(len(listaAuxiliar)):         #O(n-1)
            iteraciones += 1
            if minimo >= listaAuxiliar[k]:
                minimo = listaAuxiliar[k]
        listaAuxiliar.remove(minimo)
        listaOrdenada.append(minimo)
    
    print(iteraciones)
    return listaOrdenada
    
#(n*(n+1))/2
print(ordenar([4,8,3,2,-6,-10,4,10,90,-18]))

    
    
    
    
    
