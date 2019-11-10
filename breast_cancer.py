# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:08:30 2019

@author: isac_
"""
import numpy as np
from sklearn import datasets 

def sigmoid(soma):
    return 1/(1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

base = datasets.load_breast_cancer()
entradas = base.data
valoresSaida = base.target
saidas = np.empty([569, 1], dtype = int)
for i in range(569): #valor de registros
    saidas[i] = valoresSaida[i]


pesos0 = 2*np.random.random((30, 3)) - 1

pesos1 = 2*np.random.random((3, 1)) - 1

epocas = 10000
taxaAprendizagem = 0.3
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)  #E(xi * wi)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Acerto:" + str(1 - mediaAbsoluta) + "  Teste: " + str(j+1))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovos0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovos0 * taxaAprendizagem) 


quant = 0
quant1 = 0   
for i in range(569):
    if(valoresSaida[i] != 0):
        quant = quant + 1
    else:
        quant1 = quant1 + 1

print("Certos:" + str(quant))
print("Erros:" + str(quant1))








