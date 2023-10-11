# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:27:51 2023

@author: Fernando
"""

"""
Ejercicio01
"""
def busqueda_binaria(elementos, elemento):
    izq = 0
    der = len(elementos) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if elementos[medio] == elemento:
            return medio
        elif elementos[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1

    return -1  # Si el elemento no se encuentra en el arreglo


"""
Ejercicio02
"""
def buscar_posicion_insercion(elementos, elemento):
    izq = 0
    der = len(elementos) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if elementos[medio] == elemento:
            return medio  # El elemento ya está en la lista en esta posición.
        elif elementos[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1
    # Cuando no se encuentra el elemento, izquierda apunta a la
    # posición de inserción.
    return izq


"""
Ejercicio03
"""
def encontrar_punto_fijo(elementos):
    izq = 0
    der = len(elementos) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if elementos[medio] == medio:
            return medio
        elif elementos[medio] < medio:
            izq = medio + 1
        else:
            der = medio - 1

    return -1  # Si no se encuentra ningún punto fijo en la lista


"""
Ejercicio04
"""
def encontrar_numero_minimo(elementos):
    izq = 0
    der = len(elementos) - 1

    while izq < der:
        # Si el segmento restante es completamente ordenado,
        # el mínimo es el primer elemento.
        if elementos[izq] < elementos[der]:
            return elementos[izq]

        medio = (izq + der) // 2

        # Compara el elemento del medio con los extremos para
        # decidir en qué mitad buscar.
        if elementos[medio] > elementos[der]:
            izq = medio + 1
        elif elementos[medio] < elementos[der]:
            der = medio
        else:
            # Si hay duplicados en la lista, disminuye
            # el extremo derecho en uno.
            der -= 1

    return elementos[izq]


"""
Ejercicio05
"""
def buscar_en_secuencia_bitonica(elementos, elemento):
    n = len(elementos)
    pico = encontrar_pico(elementos, 0, n - 1)

    # Si el elemento está en el pico de la secuencia bitónica
    if elementos[pico] == elemento:
        return pico

    # Realiza una búsqueda binaria en la primera mitad ascendente
    resultado = buscar_ascendente(elementos, elemento, 0, pico - 1)

    # Si no se encontró en la primera mitad, busca en la segunda
    # mitad descendente
    if resultado == -1:
        resultado = buscar_descendente(elementos, elemento, pico + 1, n - 1)

    return resultado


def encontrar_pico(elementos, izq, der):
    while izq < der:
        medio = (izq + der) // 2

        if elementos[medio] > elementos[medio + 1]:
            der = medio
        else:
            izq = medio + 1

    return izq


def buscar_ascendente(elementos, elemento, izq, der):
    while izq <= der:
        medio = (izq + der) // 2

        if elementos[medio] == elemento:
            return medio
        elif elementos[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1

    return -1


def buscar_descendente(elementos, elemento, izq, der):
    while izq <= der:
        medio = (izq + der) // 2

        if elementos[medio] == elemento:
            return medio
        elif elementos[medio] < elemento:
            der = medio - 1
        else:
            izq = medio + 1

    return -1
