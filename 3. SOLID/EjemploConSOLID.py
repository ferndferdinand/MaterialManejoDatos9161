# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 07:11:45 2023

@author: HP
"""

from abc import ABC, abstractmethod

class Racional:
    
    def __init__(self, racional:str):
        
        racional = racional.split("/")
        numerador = int(racional[0])
        if int(racional[1]) != 0:
            denominador = int(racional[1])
        
        for i in range(abs(min(numerador,denominador)),1,-1):
            if abs(min(numerador,denominador))%i == 0 and  abs(max(numerador,denominador))%i == 0:
                numerador /= i
                denominador /= i
        
        self.numerador = int(numerador)
        self.denominador = int(denominador)
        
        
    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        else:
            return f"{self.numerador}/{self.denominador}"
        
        
        
class Operadores(ABC):
    
    def __init__(self, racional:object):
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
    
    def __init__(self, racional:object):
        super().__init__(racional)

    def sumar(self, racional2:object):
        num = self.racional.numerador * racional2.denominador + self.racional.denominador * racional2.numerador
        den = self.racional.denominador * racional2.denominador
        return Racional(f"{num}/{den}")
    
    def restar(self, racional2:object):
        num = self.racional.numerador * racional2.denominador - self.racional.denominador * racional2.numerador
        den = self.racional.denominador * racional2.denominador
        return Racional(f"{num}/{den}")
    
    def multiplicar(self, racional2:object):
        num = self.racional.numerador * racional2.numerador
        den = self.racional.denominador * racional2.denominador
        return Racional(f"{num}/{den}")
    
    def dividir(self, racional2:object):
        num = self.racional.numerador * racional2.denominador
        den = self.racional.denominador * racional2.numerador
        return Racional(f"{num}/{den}")

print(OperandoRacionales(Racional("2/5")).sumar(Racional("3/5")))
print(OperandoRacionales(Racional("2/5")).restar(Racional("3/10")))
print(OperandoRacionales(Racional("2/5")).multiplicar(Racional("3/4")))
print(OperandoRacionales(Racional("2/5")).dividir(Racional("3/15")), end = "\n\n")



def sumar3Racionales(racional1:object, racional2:object, racional3:object):
    racionalAux = OperandoRacionales(racional1).sumar(racional2)
    return OperandoRacionales(racionalAux).sumar(racional3)
    

print(sumar3Racionales(Racional("2/3"),Racional("1/4"),Racional("5/12")))










