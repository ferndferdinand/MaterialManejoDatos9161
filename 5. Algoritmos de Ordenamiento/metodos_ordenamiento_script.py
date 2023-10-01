# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:34:50 2023

@author: Fernando
"""

import random

lista = [random.randint(-20, 50) for i in range(20)]

print(lista)

lista = [8, 7, 43, 38, 30, 2, -11, 17, -10, -5]


# %%
# -------------------------Ordenamiento burbuja------------------------

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def burbuja_mejorado(lista):
    i = 0
    cambios = True
    while cambios and i < len(lista):
        cambios = False
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                cambios = True
        i += 1

# %%
# -------------------------Ordenamiento por selección------------------------


def seleccion_con_lista_aux(lista):
    listaOrdenada = []
    for i in range(len(lista)):  # O(n)
        menor = lista[0]
        for j in range(len(lista)):  # O(n-1)

            if menor >= lista[j]:
                menor = lista[j]

        lista.remove(menor)
        listaOrdenada.append(menor)
    return listaOrdenada


def seleccion1(lista):
    for i in range(len(lista)):  # O(n)
        menor = i
        for j in range(i + 1, len(lista)):  # O(n-1)
            if lista[menor] > lista[j]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]


def seleccion(lista):
    for i in range(len(lista)):  # O(n)
        for j in range(i + 1, len(lista)):  # O(n-1)
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


# %%
# -------------------------Ordenamiento por inserción------------------------
def insercion(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        indice = i

        while indice > 0 and aux < lista[indice - 1]:
            lista[indice] = lista[indice - 1]
            indice -= 1
        lista[indice] = aux
        """
        for j in range(i-1,-1,-1):
            if aux < lista[j]:
                lista[indice] = lista[j]
            else:
                break
            indice -= 1
            lista[j] = aux
        """
