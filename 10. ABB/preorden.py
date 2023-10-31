# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 02:14:36 2023

@author: Fernando
"""


class NodoABB:

    def __init__(self, raiz):
        self.raiz = raiz
        self.izquierdo = None
        self.derecho = None


def buscar_valor(arbol, raiz):
    if arbol is None:
        return False
    if arbol.raiz == raiz:
        return True
    if raiz < arbol.raiz:
        return buscar_valor(arbol.izquierdo, raiz)
    else:
        return buscar_valor(arbol.derecho, raiz)


arbol = NodoABB(5)
arbol.izquierdo = NodoABB(4)
arbol.izquierdo.izquierdo = NodoABB(2)
arbol.izquierdo.izquierdo.izquierdo = NodoABB(1)
arbol.izquierdo.izquierdo.derecho = NodoABB(3)

arbol.derecho = NodoABB(8)
arbol.derecho.izquierdo = NodoABB(7)
arbol.derecho.izquierdo.izquierdo = NodoABB(6)
arbol.derecho.derecho = NodoABB(9)

print(buscar_valor(arbol, 4))
print(buscar_valor(arbol, 10))
