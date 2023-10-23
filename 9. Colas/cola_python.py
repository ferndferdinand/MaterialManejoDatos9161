# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 07:01:42 2023

@author: HP
"""
from abc import ABC, abstractmethod


class ColaABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def agregar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass

    @abstractmethod
    def tamanio(self):
        pass

    @abstractmethod
    def vacio(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass


class Cola(ColaABC):

    def __init__(self):
        self.cola = []

    def agregar(self, elemento: int):
        self.cola.append(elemento)

    def eliminar(self):
        if not self.vacio():
            return self.cola.pop(0)

    def tamanio(self):
        return len(self.cola)

    def vacio(self):
        return len(self.cola) == 0
    
    def imprimir(self):
        return self.cola

cola = Cola()
while True:
    print("1. Agregar elmento")
    print("2. Eliminar elemento")
    print("3. Obtener tamaño")
    print("4. Vacío")
    print("5. Imprimir")
    print("6. Salir", end = "\n\n")
    op = int(input("Elige una opción: "))
    print()
    
    if op == 1:
        cola.agregar(int(input("Agrega un valor: ")))
    elif op == 2:
        valor = cola.eliminar()
        print(f"Se eliminó {valor} de la cola")
    elif op == 3:
        print(f"El tamaño de la cola es: {cola.tamanio()}")
    elif op == 4:
        print(f"La cola está vacía: {cola.vacio()}")
    elif op == 5:
        print(f"La cola es: {cola.imprimir()}")
    else:
        break

        