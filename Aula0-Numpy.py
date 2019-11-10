# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:38:18 2019

@author: isac_
"""
import numpy as np
## AND
entradas = np.array([1, 1])
pesos = np.array([0.0, 0.0])  

def soma (e, p):
   return e.dot(p)
#dot product = produto escalar
   
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)



