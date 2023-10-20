# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 07:22:55 2023

@author: HP
"""

def palindromo(cadena: str):
    cadena = cadena.replace(" ", "").lower()
    pila = []
    
    for char in cadena:
        pila.append(char)
    
    cadena_inversa = ""
    
    while pila:
        cadena_inversa += pila.pop()
    
    return cadena == cadena_inversa

print(palindromo("rada"))