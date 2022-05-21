from matplotlib import pyplot as plt
from matplotlib.cbook import flatten
import numpy as np
import smallest
import flatten

e = 2.71828
pi = 3.14159

def run():

    print(smallest.smallestModelParamClass.m)
    print(flatten.flattenModelParamClass.m)

    x = np.linspace(0,1)
    y2 = eval(smallest.smallestModelParamClass.m)
    yy = eval(flatten.flattenModelParamClass.m)
    # y1 = 1 - 0.5 * np.cos(2*pi*x)

    # plot the rho distribution of two models
    plt.plot(x, y2, label='smallest')
    plt.plot(x, yy, label='flatten')
    plt.xlabel('x')
    plt.ylabel('m')
    plt.title('rho vs x')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    run()