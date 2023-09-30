# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:22:18 2023

@author: Fernando
"""

#%%
#----------------------------------------QuickSort---------------------------------
def dividir_elementos(elementos):
    
    pivote = elementos[0]
    menores = []
    mayores = []
    
    for i in range(1,len(elementos)):
        if elementos[i] < pivote:
            menores.append(elementos[i])
        else:
            mayores.append(elementos[i])
            
    return menores, pivote, mayores


def quicksort_lista_aux(elementos):
    if len(elementos) < 2:
        return elementos
    
    menores, pivote, mayores = dividir_elementos(elementos)
    
    return quicksort_lista_aux(menores) + [pivote] + quicksort_lista_aux(mayores)



#%%
# -------------------------------------------Merge------------------------------------
def merge(izq,der):
    elementos_merged = []
    while len(izq) and len(der):
        if izq[0] <= der[0]:
            elementos_merged.append(izq[0])
            izq.pop(0)
        else:
            elementos_merged.append(der[0])
            der.pop(0)
     
    elementos_merged.extend(izq)
    elementos_merged.extend(der)
    
    return elementos_merged
    
def merge_sort(elementos):
    if len(elementos) < 2:
        return elementos
    
    medio = len(elementos)//2
    izq = elementos[:medio]
    der = elementos[medio:]

    izq = merge_sort(izq)
    der = merge_sort(der)
    
    return merge(izq,der)
        
        
        