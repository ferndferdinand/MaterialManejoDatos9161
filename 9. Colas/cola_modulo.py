# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 07:38:44 2023

@author: HP
"""

from queue import Queue

cola = Queue()

cola.put(5)
cola.put(6)
cola.put(8)
cola.put(3)
cola.put(4)

print(cola.full())
print(cola.get())
print(cola.get())
print(cola.get())
print(cola.get())
print(cola.get())

print(cola.qsize())
print(cola.empty())
