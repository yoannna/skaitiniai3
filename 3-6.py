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
    sol = np.linalg.solve(np.array([eq1, eq2, eq3]), eq)
    e1 = 2*sol[0]*x[index+1] + sol[1]
    return sol, e1

split()

fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('xkcd:black')

xPlot = np.linspace(start, stop, 1000)
ax.plot(xPlot, f(xPlot))

sol = []
e = 0
for i in range(0, n):
    currentSol, e = getE(i, e)
    sol.append(currentSol)

    xPlot = np.linspace(start + step*i, start + step*(i+1), 1000)
    fCurrent = lambda x: currentSol[0]*x*x + currentSol[1]*x + currentSol[2]
    ax.plot(xPlot, fCurrent(xPlot))

plt.show()
