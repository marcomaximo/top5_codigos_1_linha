from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import random
import math


#Inverter valores em Python
cod1 = 10
cod2 = 50

cod1, cod2 = cod2, cod1
print (cod1, cod2)


#Operador ternário
celulares = 10
objetivo = 15

bonus_salario = 100 if celulares >= objetivo else 0
print (bonus_salario)


#Atribuição de valores
vendas1 = 100
vendas2 = 150
vendas3 = 200

vendas1, vendas2, vendas3 = 100, 150, 200
print (vendas1, vendas2, vendas3)


#Loop If-Else ou While
m = 50

if m == 1 or m == 2 or m == 3: 
    pass

if m in [1, 2, 3]: 
    pass


#Calcular o fatorial de determinado número
z = 3
print(math.factorial(z))