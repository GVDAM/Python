# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:41:38 2020

@author: Gabriel Vargas Dambroski
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

''' Importing DataSet '''
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1:].values


''' Splitting the dataset in train set e test set '''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

''' Fitting Simple Linear Regression to the Training set '''
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

''' Predicting the Test set results ''' 
y_predict = regressor.predict(X_test)


''' Visualising the Training set results '''
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # Reta criada de acordo com a predição no treinamento
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()


''' Visualising the Test set results '''
plt.scatter(X_test, y_test, color = 'red') # Pontos no gráfico representando a base de teste
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # Reta criada de acordo com a predição no treinamento
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()