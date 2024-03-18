import numpy as np
import matplotlib.pyplot as plt

K = 60
num_r = 1000
num_N0 = 100
num_iterations = 100000
transient_iterations = 1000

r_values = np.linspace(0.1, 4, num_r)
equilibrium_populations = np.zeros((num_r, num_N0))
N0_values = np.linspace(0, K, num_N0)

for j, N0 in enumerate(N0_values):
    N = np.full_like(r_values, N0)   

    for _ in range(transient_iterations):
        N = N * np.exp(r_values * (1 - N / K))

    for _ in range(num_iterations):
        N = N * np.exp(r_values * (1 - N / K))

    equilibrium_populations[:, j] = N

plt.figure(figsize=(10, 6))
plt.plot(r_values, equilibrium_populations, '.', markersize=1)
plt.xlabel('r')
plt.ylabel('Equilibrium Population Size')
plt.title('Bifurcation Diagram')
plt.show()
