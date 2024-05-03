import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the Lotka-Volterra equations
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    x, y, z = y
    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y
    dzdt = -z + delta*y*z
    return [dxdt, dydt, dzdt]

# Parameters
alpha = 0.1  # Sheep growth rate
beta = 0.02  # Sheep predation rate
delta = 0.03  # Wolf reproduction rate
gamma = 0.1  # Wolf death rate

# Initial conditions
x0 = 40  # Initial sheep population
y0 = 9  # Initial grass population
z0 = 50  # Initial wolf population
initial_conditions = [x0, y0, z0]
t = np.linspace(0, 2000, 1000)

# Solve the differential equations
solution = odeint(lotka_volterra, initial_conditions, t, args=(alpha, beta, delta, gamma))
sheep, grass, wolves = solution[:, 0], solution[:, 1], solution[:, 2]

# Plot the population dynamics
plt.figure(figsize=(10, 6))
plt.plot(t, sheep, label='Sheep')
plt.plot(t, grass, label='Grass')
plt.plot(t, wolves, label='Wolves')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model')
plt.legend()
plt.grid(True)
plt.show()
