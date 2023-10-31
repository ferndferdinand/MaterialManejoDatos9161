# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:02:34 2023

@author: HP
"""


class NodoABB:

    def __init__(self, raiz):
        self.raiz = raiz
        self.izquierdo = None
        self.derecho = None


def recorrido_inorden(arbol):
    if arbol is not None:
        recorrido_inorden(arbol.izquierdo)
        print(arbol.raiz)
        recorrido_inorden(arbol.derecho)


arbol = NodoABB(5)
arbol.izquierdo = NodoABB(4)
arbol.izquierdo.izquierdo = NodoABB(2)
arbol.izquierdo.izquierdo.izquierdo = NodoABB(1)
arbol.izquierdo.izquierdo.derecho = NodoABB(3)

arbol.derecho = NodoABB(8)
arbol.derecho.izquierdo = NodoABB(7)
arbol.derecho.izquierdo.izquierdo = NodoABB(6)
arbol.derecho.derecho = NodoABB(9)

recorrido_inorden(arbol)
