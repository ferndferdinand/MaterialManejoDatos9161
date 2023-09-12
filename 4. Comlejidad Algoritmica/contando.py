# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:18:26 2023

@author: HP
"""

#%%
def sumar_menor_cant_elementos(lista):
    listaAuxiliar = lista.copy()
    listaOrdenada = []
    iteraciones = 0                                         #(n*(n-1))/2
    for i in range(len(lista)):                             #O(n)         
        maximo = listaAuxiliar[0]
        for k in range(len(listaAuxiliar)):                 #O(n-1)                    
            iteraciones += 1
            if maximo <= listaAuxiliar[k]:
                maximo = listaAuxiliar[k]
        listaAuxiliar.remove(maximo)
        listaOrdenada.append(maximo)
        
        if sum(listaOrdenada) > len(lista)**2:
            return listaOrdenada
    return listaOrdenada


print(sumar_menor_cant_elementos([2,5,7,4,-6,39,49,-50,40,93,12,19]))

#%%

def contar_valores(lista:list):
    contador = {}
    listaAux = lista.copy()
    
    i = 0
    iteraciones = 0
    while i < len(listaAux):                    #O(n)
        elemento = listaAux[i]
        contador[elemento] = 1
        listaAux.remove(elemento)
        j = 0
        while j < len(listaAux):                #O(n-1)
            iteraciones += 1
            if listaAux[j] == elemento:
                contador[elemento] += 1
                listaAux.remove(elemento)
                j -= 1
            j +=1 
        
    print(iteraciones)
    
    return contador




        
        
        
def contar_elementos(lista:list):
    contador = {}  # Creamos un diccionario para almacenar las ocurrencias de cada elemento
    
    i = 0
    for elemento in lista:                  #O(n)
        i += 1
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    print(i)
    return contador


mi_lista = [1, 2, 2, 3, 4, 4, 5, 8]
resultados_1 = contar_elementos(mi_lista)
print(resultados_1)


resultados_2 = contar_valores(mi_lista)
print(resultados_2)

#%%


def suma_de_numeros(lista:list):
    suma_maxima = lista[0] 
    n = len(lista)
    for i in range(n):                          #O(n)   
        for j in range(i, n):                   #O(n)
            suma_actual = 0;
            for k in range(i, j+1):             #O(n)
                suma_actual += lista[k]
            
            if suma_actual > suma_maxima:
                suma_maxima = suma_actual
    return suma_maxima
                

print(suma_de_numeros([1, 2, 2, 3, 4, 4, 5, 8]))

#O(n**3)

#%%
#O(log(n))
"""
Aquí, siempre sabemos que el número tiene que estar en el intervalo [l,r], 
que vamos disminuyendo a la mitad de longitud en cada iteración.
"""

def buscar_valor(lista:list, numero:int):
    encontrado = False
    l = 0;
    n = len(lista)
    r = n-1;
    
    while r > l and not encontrado:
        m = (l + r)//2
        if lista[m] > numero:
            r = m-1
        elif lista[m] == numero:
            encontrado = True
        else:
            l = m+1
    
    if lista[l] == numero: 
      encontrado = True
      
    return encontrado
     

print(buscar_valor([1, 2, 2, 3, 4, 4, 5, 8],3))



#%%