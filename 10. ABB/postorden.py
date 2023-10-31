# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 02:14:37 2023

@author: Fernando
"""


class NodoABB:

    def __init__(self, raiz):
        self.raiz = raiz
        self.izquierdo = None
        self.derecho = None


def altura_arbol(arbol):
    if arbol is None:
        return 0
    altura_izq = altura_arbol(arbol.izquierdo)
    altura_der = altura_arbol(arbol.derecho)
    return max(altura_izq, altura_der) + 1


arbol = NodoABB(5)
arbol.izquierdo = NodoABB(4)
arbol.izquierdo.izquierdo = NodoABB(2)
arbol.izquierdo.izquierdo.izquierdo = NodoABB(1)
arbol.izquierdo.izquierdo.derecho = NodoABB(3)

arbol.derecho = NodoABB(8)
arbol.derecho.izquierdo = NodoABB(7)
arbol.derecho.izquierdo.izquierdo = NodoABB(6)
arbol.derecho.derecho = NodoABB(9)
print(altura_arbol(arbol))
