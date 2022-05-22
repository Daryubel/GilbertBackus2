
from random import random
import numpy as np
from sympy import Symbol, cos, integrate, solve
import smallest

e = 2.71828
pi = 3.14159

class flattenModelFunctionClass:

    x = Symbol('x')
    c = Symbol('c')
    f = 1
    def h(i,x):
        return (1-e**(-i*x)) / i
    hList = []
    hVal = []
    hList.append(x)
    hVal.append(1)
    for i in range(1,11):
        hList.append(h(i,x))
        hVal.append(h(i,1))
    print(hVal)


class flattenModelParamClass:
    
    # method for cartesian product of (gi, gj)
    def cartesianProduct(i, j):
        f = flattenModelFunctionClass.f
        gl = flattenModelFunctionClass.hList[i]
        gr = flattenModelFunctionClass.hList[j]
        x = flattenModelFunctionClass.x

        return integrate((gl/f) * (gr/f), (x, 0, 1))

    # method for deciding constant c
    def rhoVal(x, rho):
        c = flattenModelFunctionClass.c
        return eval(str(rho-0.5))

    xVec = np.linspace(0,1,11)
    y = np.zeros(11)
    for i in range(0,11):
        y[i] = 0.5 * flattenModelFunctionClass.hVal[i] - smallest.smallestModelParamClass.d[i]
    
    # generate interfered y vector
    yInterfered = np.zeros(11)
    for i in y:
        yInterfered = y + random()*0.1*y
    
    # H matrix
    matrixH = np.zeros((11,11))
    for j in range(0, 11):
        for i in range(0, 11):
            matrixH[i][j] = cartesianProduct(i, j)
    
    B = np.dot(np.linalg.inv(matrixH), y)

    h_over_f = []
    for i in range(0, 11):
        h_over_f.append(flattenModelFunctionClass.hList[i] / (flattenModelFunctionClass.f**2))
    x = flattenModelFunctionClass.x
        
    mMid = np.dot(B, h_over_f) + flattenModelFunctionClass.c
    c = solve(rhoVal(1, mMid), flattenModelFunctionClass.c)[0]

    ############################################
    # return the symbolized rho expression
    rho = str(np.dot(B, h_over_f) + c)