#Xt+1 = r * Xt * (1 - Xt). n0 = 0.1 and r  = 2.5 for 100 iterationss

import numpy as np
import matplotlib.pyplot as plt

n0 = 0.1
r = 2.5
X = np.zeros(100)

X[0] = n0

for i in range(1,100):
    X[i] = r * X[i-1] * (1 - X[i-1])

plt.plot(X)
plt.show()







r = [0.5, 2.5, 3.1, 3.5, 3.8]

for j in range(5):
    X = np.zeros(100)
    X[0] = n0
    for i in range(1,100):
        X[i] = r[j] * X[i-1] * (1 - X[i-1])
    plt.plot(X)
    plt.show()

#bifurcation diagram for the scaled logistic map
    
n = 10000
r = np.linspace(2.5, 4.0, n)

iterations = 1000
last = 100

x = 1e-5 * np.ones(n)

for i in range(iterations):
    x = r * x * (1-x)
    if i >= (iterations - last):
        plt.plot(r, x, ',k', alpha=0.25)
#plt.show()


#integerize the values of r and x

gen = 500
k = 60 #carrying capacity

r_list = []
n_list = []

r = 0.1
while r< 4.0:
    x = 0.5
    for i in range(gen):
        x = int(r * x * (1-x/k))
        if i>400:
            r_list += [r]
            n_list += [x]
    r+=0.005

plt.plot(r_list, n_list, ',k')
plt.show()

