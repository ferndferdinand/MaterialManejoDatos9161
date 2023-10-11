# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:22:18 2023

@author: Fernando
"""

import random

elementos = [random.randint(-20, 50) for i in range(10)]
# print(elementos)


def dividir_elementos(elementos):

    pivote = elementos[0]
    menores = []
    mayores = []

    for i in range(1, len(elementos)):
        if elementos[i] < pivote:
            menores.append(elementos[i])
        else:
            mayores.append(elementos[i])

    return menores, pivote, mayores


def quicksort_lista_aux(elementos):
    if len(elementos) < 2:
        return elementos

    menores, pivote, mayores = dividir_elementos(elementos)

    return quicksort_lista_aux(
        menores) + [pivote] + quicksort_lista_aux(mayores)


def dividir_elementos_2(elementos, menor, mayor):
    pivote = elementos[menor]
    izq = menor + 1
    der = mayor

    while True:
        while izq <= der and elementos[izq] <= pivote:
            izq += 1
        while izq <= der and elementos[der] >= pivote:
            der -= 1

        if der < izq:
            break

        else:
            elementos[izq], elementos[der] = elementos[der], elementos[izq]
    elementos[menor], elementos[der] = elementos[der], elementos[menor]

    return der


def quicksort(elementos, menor, mayor):
    if menor < mayor:
        pivote = dividir_elementos_2(elementos, menor, mayor)
        quicksort(elementos, menor, pivote - 1)
        quicksort(elementos, pivote + 1, mayor)


def dividir_elementos_3(elementos):
    pivote = elementos[0]
    izq = 1
    der = len(elementos) - 1

    while True:
        while izq <= der and elementos[izq] <= pivote:
            izq += 1
        while izq <= der and elementos[der] >= pivote:
            der -= 1

        if der < izq:
            break

        else:
            elementos[izq], elementos[der] = elementos[der], elementos[izq]
    elementos[0], elementos[der] = elementos[der], elementos[0]

    return der


def quicksort2(elementos):
    if len(elementos) > 1:
        pivote = dividir_elementos_3(elementos)
        elementos[:pivote] = quicksort2(elementos[:pivote])
        elementos[pivote + 1:] = quicksort2(elementos[pivote + 1:])

    return elementos


def merge(izq, der):
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

    medio = len(elementos) // 2
    izq = elementos[:medio]
    der = elementos[medio:]

    izq = merge_sort(izq)
    der = merge_sort(der)

    return merge(izq, der)
