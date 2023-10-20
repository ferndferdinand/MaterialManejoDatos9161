# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 07:04:00 2023

@author: HP
"""
import random

def eliminar_duplicados(elementos: list):
    elementos.sort()
    i = 0
    while i < len(elementos):
        aux = elementos[i]
        j = i + 1
        repetidos = True
        while j < len(elementos) and repetidos:
            if elementos[j] == aux:
                elementos.pop(j)
                j -= 1
            else:
                repetidos = False
            j += 1
        i += 1

elementos = [random.randint(0, 15) for i in range(30)]
print(elementos)

eliminar_duplicados(elementos)

print(elementos)