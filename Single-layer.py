# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:27:10 2019

@author: isac_
"""
import numpy as np
#NAND
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([1, 1, 1, 0])
#AND
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0, 0, 0, 1])
#OR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0, 1, 1, 1])
#XOR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])   -- NAO FUNCIONA COM ESSE ALGORITMO
#saidas = np.array([0, 1, 1, 0])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
 # NAND return 0
 #   return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada) ##para nao ficar com valor negativo
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * erro * entradas[i][j])
                print('Peso Atualizado:' + str(pesos[j]))
        print('total de erros:' + str(erroTotal))
treinar()
print("rede neural treinada")
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
