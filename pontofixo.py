import numpy as np
import math

# func e derivfunc devem ser funcoes
# Exemplo de chamada: metodoNewtonRhapson(1.5, func, derivfunc, 0.1, 0.1)
# ou seja, o código da para ser testado para qualquer função, basta passar as entradas corretamente. 
# No fim desse código ja esta chamando a função do enunciado então basta clicar em run e ver as iterações. 
def func(x): 
  return x**3-x-1

def phi(x):
  return ((x+1)**(1/3))
def metodopontofixo(x0, func, phi,maxiter, epsilon1, epsilon2):
    iter = 0
    listax = []
    listafx = []
    if (math.fabs(func(x0)) > epsilon1) :
        printer = '[x'+str(iter)+' = '+str(x0)+', f(x'+str(iter)+') = '+str(func(x0))+']'
        print(printer)
        listax.append(x0)
        listafx.append(func(x0))
        xk = phi(x0)
        iter = iter + 1
        if (math.fabs(func(x0)) <= epsilon1 and (math.fabs(xk-x0) <= epsilon2)):
            return;
        else:
            x0 = xk
        for i in range(1,maxiter):
            resultado_fx = func(x0)
            printer = '[x'+str(iter)+' = '+str(x0)+', f(x'+str(iter)+') = '+str(resultado_fx)+']'
            print(printer)
            #print('[x',iter,' = ',x0,', f(x',iter,') = ',resultado_fx,']') 
            #xk = x0 - (func(x0)/phi(x0))
            listax.append(x0)
            listafx.append(resultado_fx)
            xk = phi(x0)
            diferenca = abs(xk-x0)
            print("Erro em x: ", diferenca)
            #  lista.append(xk)
            iter = iter + 1
            if (abs(func(xk)) <= epsilon2 and (diferenca <= epsilon1)):
                break;
            else:
                x0 = xk
                listax.append(xk)
                listafx.append(func(xk))
                #diferenca = math.fabs(xk - listax[iter-1])
                #printer = '[x'+str(iter)+' = '+str(xk)+', f(x'+str(iter)+') = '+str(func(xk))+', Diferenca: '+str(diferenca)+']'
                #print(printer)
    #print('[x',iter,' = ',xk,' f(x',iter,') = ',resultado_fx,']')
    print('Numero de iteracoes: ',iter)
    print('Precisao |f(xk)|: ',math.fabs(func(xk)))
    print('Precisao |xk-x0|: ',diferenca)
metodopontofixo(1, func, phi,50, 10**(-12), 10**(-12))
