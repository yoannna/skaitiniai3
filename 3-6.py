import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

start = -2.0
stop = 4.0
n = 10
step = (stop - start) / n
x = []
y = []
f = lambda x: (2+x)*(np.sin(2*x))

def split():
    for i in range (0, n+1):
        xi = start + step*i
        x.append(xi)
        y.append(f(xi))

def getE(index, e = 0):
    eq1 = [x[index]*x[index], x[index], 1]
    eq2 = [x[index + 1]*x[index + 1], x[index + 1], 1]
    eq3 = [2*x[index],  1, 0]
    eq = np.array([y[index], y[index + 1], e])
    coef = np.linalg.solve(np.array([eq1, eq2, eq3]), eq)
    e1 = 2*coef[0]*x[index+1] + coef[1]
    return coef, e1

split()

fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('xkcd:black')

xPlt = np.linspace(start, stop, 1000)
ax.plot(xPlt, f(xPlt))

e = 0
for i in range(0, n):
    coef, e = getE(i, e)
    xPlt = np.linspace(start + step*i, start + step*(i+1), 1000)
    fi = lambda x: coef[0]*x*x + coef[1]*x + coef[2]
    ax.plot(xPlt, fi(xPlt))

plt.show()
