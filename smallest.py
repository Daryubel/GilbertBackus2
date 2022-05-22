
from random import random, randrange
import numpy as np
from sympy import Symbol, cos, integrate

e = 2.71828
pi = 3.14159

class smallestModelFunctionClass:

    x = Symbol('x')
    f = 1
    def m(x):
        return 1 - 0.5 * cos(2*pi*x)
    def g(i, x):
        return e**(-(i-1)*x)
    gList = []
    for i in range(1,11+1):
        gList.append(g(i, x))


class smallestModelParamClass:
    
    # method for cartesian product of (gi, gj)
    def cartesianProduct(i, j):
        f = smallestModelFunctionClass.f
        gl = smallestModelFunctionClass.gList[i]
        gr = smallestModelFunctionClass.gList[j]
        x = smallestModelFunctionClass.x

        return integrate((gl/f) * (gr/f), (x, 0, 1))

    xVec = np.linspace(0,1,11)
    d = np.zeros(11)
    m = np.zeros(11)
    for i in range(0,11):
        m[i] = smallestModelFunctionClass.m(xVec[i])
        d[i] = integrate(smallestModelFunctionClass.m(smallestModelFunctionClass.x) * smallestModelFunctionClass.g(i+1, smallestModelFunctionClass.x), 
                        (smallestModelFunctionClass.x, 0, 1))
    
    # generate interfered d vector
    dInterfered = np.zeros(11)
    for i in d:
        dInterfered = d + random()*0.1*d

    # G matrix
    matrixG = np.zeros((11,11))
    for j in range(0, 11):
        for i in range(0, 11):
            matrixG[i][j] = cartesianProduct(i, j)
    
    a = np.dot(np.linalg.inv(matrixG), d)

    g_over_f = []
    for i in range(0, 11):
        g_over_f.append(smallestModelFunctionClass.gList[i] / (smallestModelFunctionClass.f**2))
    x = smallestModelFunctionClass.x
        

    # return the symbolized rho expression
    m = str(np.dot(a, g_over_f))