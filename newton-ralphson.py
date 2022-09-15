def func(x): 
  return (x*math.log10(x)-1)

def derivfunc(x):
  return (math.log10(x)+(1/math.log(10)))
def metodoNewtonRhapson(x0, func, derivfunc, epsilon1, epsilon2):
    iter = 0
    listax = []
    listafx = []
    if (math.fabs(func(x0)) > epsilon1) :
        printer = '[x'+str(iter)+' = '+str(x0)+', f(x'+str(iter)+') = '+str(func(x0))+']'
        print(printer)
        listax.append(x0)
        listafx.append(func(x0))
        xk = x0 - (func(x0)/derivfunc(x0))
        iter = iter + 1
        if (math.fabs(func(x0)) < epsilon1 or (math.fabs(xk-x0) < epsilon2)):
            return;
        else:
            x0 = xk
    while (math.fabs(func(x0)) > epsilon1):
        resultado_fx = func(x0)
        diferenca = math.fabs(x0 - listax[iter-1])
        printer = '[x'+str(iter)+' = '+str(x0)+', f(x'+str(iter)+') = '+str(resultado_fx)+', Diferenca: '+str(diferenca)+']'
        print(printer)
        listax.append(x0)
        listafx.append(resultado_fx)
        xk = x0 - (func(x0)/derivfunc(x0))
        iter = iter + 1
        if (math.fabs(func(xk)) < epsilon2 or (math.fabs(xk-x0) < epsilon1)):
            break;
        else:
            x0 = xk
    listax.append(xk)
    listafx.append(func(xk))
    diferenca = math.fabs(xk - listax[iter-1])
    printer = '[x'+str(iter)+' = '+str(xk)+', f(x'+str(iter)+') = '+str(func(xk))+', Diferenca: '+str(diferenca)+']'
    print(printer)
    print('Numero de iteracoes: ',iter)
    print('Precisao |f(xk)|: ',math.fabs(func(xk)))
    print('Precisao |xk-x0|: ',math.fabs(xk-x0))
metodoNewtonRhapson(2.5, func, derivfunc, 10**(-12), 10**(-12))
