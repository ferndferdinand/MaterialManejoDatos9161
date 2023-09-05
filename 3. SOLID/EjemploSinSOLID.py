# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:57:07 2023

@author: A19240
"""

from abc import ABC, abstractmethod

    
class Operadores(ABC):
    
    def __init__(self, racional:str):
        self.racional = racional

    @abstractmethod
    def sumar(self):
        pass
    
    @abstractmethod
    def restar(self):
        pass
    
    @abstractmethod
    def multiplicar(self):
        pass
    
    @abstractmethod
    def dividir(self):
        pass
    
class OperandoRacionales(Operadores):
    
    def __init__(self, racional:str):
        super().__init__(racional)

    
    def sumar(self, racional2:str, racional3 = None):
        
        racional = self.racional.split("/")
        num1 = int(racional[0])
        den1 = int(racional[1])
        racional2 = racional2.split("/")
        num2 = int(racional2[0])
        den2 = int(racional2[1])
        
        if den1 == den2:
            num = num1 + num2
            den = den1
        else:
            num = num1 * den2 + den1 * num2
            den = den1 * den2
            
        if racional3 != None:
            racional3 = racional3.split("/")
            num3 = int(racional3[0])
            den3 = int(racional3[1])
            
            if den1 == den2 == den3:
                num = num1 + num2 + num3
                den = den1
            else:
                den = den1 * den2 * den3
                num = int(den/den1 * num1 + den/den2 * num2 + den/den3 *num3)
    

        return f"{num}/{den}"
    
    
    def restar(self, racional2:str):
        racional = self.racional.split("/")
        num1 = int(racional[0])
        den1 = int(racional[1])
        racional2 = racional2.split("/")
        num2 = int(racional2[0])
        den2 = int(racional2[1])
        
        if den1 == den2:
            num = num1 - num2
            den = den1
        else:
            num = num1 * den2 - den1 * num2
            den = den1 * den2

        return f"{num}/{den}"
    
    
    def multiplicar(self, racional2:str):
        racional = self.racional.split("/")
        num1 = int(racional[0])
        den1 = int(racional[1])
        racional2 = racional2.split("/")
        num2 = int(racional2[0])
        den2 = int(racional2[1])
        
        num = num1 * num2
        den = den1 * den2

        return f"{num}/{den}"
    
    
    def dividir(self, racional2:str):
        racional = self.racional.split("/")
        num1 = int(racional[0])
        den1 = int(racional[1])
        racional2 = racional2.split("/")
        num2 = int(racional2[0])
        den2 = int(racional2[1])
    
        num = num1 * den2
        den = den1 * num2

        return f"{num}/{den}"
    
    
print(OperandoRacionales("2/5").sumar("3/5"))
print(OperandoRacionales("2/3").sumar("1/4","5/12"), end = "\n\n")

print(OperandoRacionales("2/5").restar("3/10"))
print(OperandoRacionales("2/5").multiplicar("3/4"))
print(OperandoRacionales("2/5").dividir("3/15"))
    









