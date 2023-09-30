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
       


class Burbuja(OrdenableIterativoAbstractClass):

    def ordenar(self, elementos):                       #O(n^2)
        for i in range(len(elementos)):                 #O(n)
            for j in range(len(elementos)-1):           #O(n-1) ~ O(n)
                if elementos[j] > elementos[j+1]:
                    self.intercambiar(elementos,j,j+1)
                    

class BurbujaMejorado(OrdenableIterativoAbstractClass):
    
    def ordenar(self, elementos):
        i = 0
        cambios = True
        while cambios and i < len(elementos):
            cambios = False
            for j in range(len(elementos)-i-1):
                if elementos[j] > elementos[j+1]:
                    self.intercambiar(elementos, j, j+1)
                    cambios = True
            i += 1
       


class Seleccion(OrdenableIterativoAbstractClass):
    
    def ordenar(self, elementos):                       #O(n^2)
        for i in range(len(elementos)):                 #O(n)
            for j in range(i+1, len(elementos)):        #O(n-1) ~ O(n)
                if elementos[i] > elementos[j]:
                    self.intercambiar(elementos, i, j)
                    
                    

class Insercion(OrdenableIterativoAbstractClass):

    def ordenar(self, elementos):                           #(n^2)
        for i in range(1,len(elementos)):                   #O(n-1) ~ O(n)
            aux = elementos[i]
            indice = i
            while indice > 0 and aux < elementos[indice-1]: 
                elementos[indice] = elementos[indice-1]
                indice -= 1
            elementos[indice] = aux             
                    
          
                    