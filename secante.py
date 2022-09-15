# -*- coding: utf-8 -*-

#import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
  return x*math.log10(x)-1

def secante(x0, x1, Erro, itMax):
  it = 0
  Er = False
  xa1 = x0
  x = x1
  while(Er == False and it < itMax):
    xa2 = xa1
    xa1 = x
    x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
    Er = np.abs(x - xa1) <= Erro and np.abs(f(x)) <= Erro
    print(Er)
    it = it + 1
    relError = np.abs(x-xa1)
  return (x, relError, it)

x0 = 2.3
x1 = 2.7
Erro = 10**(-12)
itMax = 50

res = secante(x0, x1, Erro, itMax)

print('O valor de x é: ', res[0])
print('O valor de f(x) é: ', f(res[0]))
print('O erro relativo foi: ', res[1])
print('O número de iterações realizadas foi: ', res[2])

#Apos execucao do codigo com as devidas informacoes obtem-se 
#O valor da funcao é:  1.324717957244746
#O erro relativo foi:  8.531680520275455e-14
#O número de iterações realizadas foi:  28


"""

# EXEMPLO 21 

import math
def f(x):
  return x*math.log10(x)-1

def secante(x0, x1, Erro, itMax):
  it = 0
  Er = 1
  xa1 = x0
  x = x1
  while(Er >= Erro and it < itMax):
    xa2 = xa1
    xa1 = x
    x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
    Er = np.abs((x - xa1)/x)
    it = it + 1
  return (x, Er, it)

x0 = 2.3
x1 = 2.7
Erro = 10**-12
itMax = 50

res = secante(x0, x1, Erro, itMax)

print('O valor da funcao é: ', res[0])
print('O erro relativo foi: ', res[1])
print('O número de iterações realizadas foi: ', res[2])

#Apos execucao do codigo com as devidas informacoes obtem-se 

#O valor da funcao é:  2.5061841455887692
#O erro relativo foi:  1.1677305907720475e-13
#O número de iterações realizadas foi:  5
"""
