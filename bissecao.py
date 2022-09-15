import numpy as np
import math

def bissecao(f,a,b,maxiter,epsilon,delta):
    a_v = [a]
    b_v = [b]
    x = (a+b)/2
    x_v = [x]
    if f(x)==0:
        return x_v, a_v, b_v,0,True
    if np.sign(f(x))*np.sign(f(a)) < 0:
        b = x
    else:
        a = x
    if abs(f(x))<= delta:
        return x_v, a_v, b_v, 0, True
    maxiter = maxiter -1
    for i in range(1,maxiter) :
        a_v.append(a)
        b_v.append(b)
        x = (a+b)/2
        x_v.append(x)
        if f(x_v[i])==0:
            return x_v, a_v, b_v, i, True
        if np.sign(f(x))*np.sign(f(a)) < 0:
            b = x
        else:
            a = x
        if abs(x_v[i]-x_v[i-1]) <= epsilon and abs(f(x))<= delta:
             return x_v, a_v, b_v, i,True
    return x_v, a_v, b_v, i,False

def function(x):
    return x**3-x-1

def printResults(f,a,b,maxiter,epsilon,delta):
    x,a,b,i,bool = bissecao(f,a,b,maxiter,epsilon,delta)
    f_v = list(map(f,x))
    if bool:
        string = "Método convergiu em " + str(i+1)+ " iterações.\n"
        print(string)
    else:
        string = "Método não convergiu em " + str(i+1)+ " iterações.\n"
        print(string)
    print("Valores de a:")
    print(a)
    print("Valores de b:")
    print(b)
    print("Valores de x:")
    print(x)
    print("Valores de f(x):")
    print(f_v)
    print("Erro em x:")
    e = x[i]-x[i-1]
    e = abs(e)
    print(e)

printResults(function,1,2,50,math.pow(10,-12),math.pow(10,-12))
