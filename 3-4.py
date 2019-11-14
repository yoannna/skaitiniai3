import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

start = 0.0
stop = 40.0
n = 20
step = (stop - start) / n
x = []
y = []

f = lambda x: (2+x)*(np.sin(2*x))
f1 = lambda x, x1: (f(x1) - f(x)) / (x1 - x)
f2 = lambda x, x1, x2: (f1(x1, x2) - f1(x, x1)) / (x2 - x)
f3 = lambda x, x1, x2, x3: (f2(x1, x2, x3) - f2(x, x1, x2)) / (x3 - x)
f4 = lambda x, x1, x2, x3, x4: (f3(x1, x2, x3, x4) - f3(x, x1, x2, x3)) / (x4 - x)
f5 = lambda x, x1, x2, x3, x4, x5: (f4(x1, x2, x3, x4, x5) - f4(x, x1, x2, x3, x4)) / (x5 - x)

def split():
    for i in range (0, n+1):
        xi = start + step*i
        x.append(xi)
        y.append(f(xi))

# i - intervalo numeris
def getL(x, x1, x2, x3, x4):
    l1 = f1(x, x1)
    l2 = f2()


split()
