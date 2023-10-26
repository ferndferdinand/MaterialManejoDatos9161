# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 07:22:55 2023

@author: HP
"""
from abc import ABC, abstractmethod

class PilaABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def apilar(self):
        pass

    @abstractmethod
    def desapilar(self):
        pass

    @abstractmethod
    def tamanio(self):
        pass

    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def __str__(self):
        return self.pila


class Pila(PilaABC):

    def __init__(self):
        self.pila = []
        self.elementos = 0

    def apilar(self, elemento: int):
        self.pila.append(elemento)
        self.elementos += 1

    def desapilar(self):
        if not self.esta_vacia():
            self.elementos -= 1
            return self.pila.pop(self.elementos)

    def tamanio(self):
        return self.elementos

    def esta_vacia(self):
        return self.elementos == 0


# Script de prueba Pila
pila = Pila()
while True:
    print("1. Apilar elmento")
    print("2. Desapilar elemento")
    print("3. Obtener tamaño")
    print("4. Vacío")
    print("5. Imprimir")
    print("6. Salir", end = "\n\n")
    op = int(input("Elige una opción: "))
    print()
    
    if op == 1:
        pila.apilar(int(input("Agrega un valor: ")))
    elif op == 2:
        valor = pila.desapilar()
        print(f"Se eliminó {valor} de la cola")
    elif op == 3:
        print(f"El tamaño de la cola es: {pila.tamanio()}")
    elif op == 4:
        print(f"La cola está vacía: {pila.esta_vacia()}")
    elif op == 5:
        print(f"La cola es: {pila}")
    else:
        break
        
"""
Ejemplo de aplicación de la pila.
"""
def palindromo(cadena: str):
    cadena = cadena.replace(" ", "").lower()
    pila = Pila()
    
    for char in cadena:
        pila.apilar(char)
    
    cadena_inversa = ""
    
    while not pila.esta_vacia():
        cadena_inversa += pila.desapilar()
    
    return cadena == cadena_inversa

print(palindromo("rada"))
