from matplotlib import pyplot as plt
import math
from random import random
import random


def rand_list(p):
    l = []
    for i in range(p):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        l.append([x, y])
    return l

def gingerbread_map(x, y):
    xn = 1 - y + math.fabs(x)
    yn = x
    return [xn, yn]


def gingerbread_plot(points, num_iter):
    #generate p amount of points [x,y], apply the function for n iterations
    #with u as the parameter value for the ikeda map
    x = []
    y = []
    xinit = []
    yinit = []
    l = rand_list(points)
    initial_list = l.copy()




    for i in range(num_iter):
        for coord in range(len(l)):
            l[coord] = gingerbread_map(l[coord][0], l[coord][1])


    for j in range(len(l)):
        x.append(l[j][0])
        y.append(l[j][1])

    for k in range(len(initial_list)):
        xinit.append(initial_list[k][0])
        yinit.append(initial_list[k][1])

    plt.subplot(121)
    plt.scatter(xinit, yinit)
    plt.title('initial values')
    plt.subplot(122)
    plt.scatter(x, y)
    plt.title('values after ' + str(num_iter) + ' iterations')
    plt.show()


gingerbread_plot(1500, 100)