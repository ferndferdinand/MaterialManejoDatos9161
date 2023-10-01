# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:04:18 2023

@author: Fernando
"""

from abc import ABC, abstractmethod


class OrdenableIterativoAbstractClass(ABC):

    @abstractmethod
    def ordenar(elementos):
        pass

    def intercambiar(self, elementos, i, j):
        elementos[i], elementos[j] = elementos[j], elementos[i]


class QuickSort(OrdenableIterativoAbstractClass):

    def dividir_elementos(self, elementos):
        pivote = elementos[0]
        menores = []
        mayores = []

        for i in range(1, len(elementos)):
            if elementos[i] < pivote:
                menores.append(elementos[i])
            else:
                mayores.append(elementos[i])

        return menores, pivote, mayores

    def ordenar(self, elementos):
        if len(elementos) < 2:
            return elementos
        menores, pivote, mayores = self.dividir_elementos(elementos)

        return self.ordenar(menores) + [pivote] + self.ordenar(mayores)


class Merge(OrdenableIterativoAbstractClass):

    def merge(self, izq, der):
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

    def ordenar(self, elementos):
        if len(elementos) < 2:
            return elementos

        medio = len(elementos) // 2
        izq = elementos[:medio]
        der = elementos[medio:]

        izq = self.ordenar(izq)
        der = self.ordenar(der)

        return self.merge(izq, der)
