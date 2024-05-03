import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

r = 0.2;K = 100;t = np.linspace(0, 10, 100)  # 100 different points of time
def logistic_growth(N, t):
    return r * N * (1 - N / K)

# Initial popN size
n = 10
popN = odeint(logistic_growth, n, t);popN = np.array(popN).flatten()
# Pop.Time Graph
plt.plot(t, popN, label='popN (N)')
plt.title('popN Growth over Time')
plt.xlabel('Time')
plt.ylabel('popN (N)')
plt.legend()
plt.grid(True)
plt.show()

#Log popN vs Time
log_population = np.log(popN)
plt.plot(t, log_population, label='Log popN (log(N))')
plt.title('Logarithmic Growth over Time')
plt.xlabel('Time');plt.ylabel('Log pop. (log(N))');plt.legend();plt.grid(True);plt.show()
#slope of logarithmic populati
slope_log_population = np.gradient(log_population, t)
# Slope of Log Pop. vs Time
plt.plot(t, slope_log_population, label='Slope of Log pop.')
plt.title('Logarithmic Growth vs Time');plt.xlabel('Time');plt.ylabel('Slope of Log pop.')
plt.legend();plt.grid(True);plt.show()

# Find and print the maximum slope of the log popN
slope = np.max(slope_log_population)
print(f"Maximum slope of Log popN: {slope:.4f}")
