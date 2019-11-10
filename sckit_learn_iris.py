# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:19:32 2019

@author: isac_
"""

from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
entradas = iris.data
saidas = iris.target

redeNeural = MLPClassifier(verbose = True,
                           max_iter = 10000,
                           tol = 0.000001,
                           activation = 'logistic',
                           learning_rate_init=0.001)
redeNeural.fit(entradas, saidas)
redeNeural.predict([[5.9, 3, 5.1, 1.8]])