import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lotkaVolterraSystem(populations, time, growthRateGrass, consumptionRateGrassBySheep,
                        sheepDeathRate, sheepBirthRateFromGrass, sheepConsumptionRateByWolves,
                        wolfDeathRate, wolfBirthRateFromSheep):
    """
    Define the Lotka-Volterra system of differential equations for wolves, sheep, and grass.
    """
    grass, sheep, wolves = populations
    dGrassDt = growthRateGrass * grass - consumptionRateGrassBySheep * grass * sheep
    dSheepDt = -sheepDeathRate * sheep + sheepBirthRateFromGrass * grass * sheep \
               - sheepConsumptionRateByWolves * sheep * wolves
    dWolvesDt = -wolfDeathRate * wolves + wolfBirthRateFromSheep * sheep * wolves
    return [dGrassDt, dSheepDt, dWolvesDt]

# Initial populations
initialGrassPopulation = 1250
initialSheepPopulation = 100.0
initialWolfPopulation = 50.0
initialPopulations = [initialGrassPopulation, initialSheepPopulation, initialWolfPopulation]

# Time points for simulation
simulationTime = np.linspace(0, 150, 150 * 20)  # Simulate for 1000 time units with 20 points per unit time

# Parameters for the Lotka-Volterra model


# grass grows back after 30 generations one it has been eaten
# Therefore the grass groweth rate is 
growthRateGrass = 0.033

# The grass is consumed by the sheep whenever they reach it. 
# The rate at which the grass is consumed
# is proportional to the amount of grass and the number of sheep
# so, the consumption rate should be - 
# consumptionRateGrassBySheep = k * grass * sheep

consumptionRateGrassBySheep = 0.01

# The sheep die due to predation by wolves and natural causes (will act as carrying capacity)
# The death rate of sheep is -
sheepDeathRate = 0.5
sheepBirthRateFromGrass = 0.04

# The sheep are consumed by the wolves. The rate at which the sheep are consumed is
sheepConsumptionRateByWolves = 0.3
wolfDeathRate = 0.4 # Lower due to the number of sheep a wolf can eat being higher (energy gain)
wolfBirthRateFromSheep = 0.05

# Solve the system of differential equations using odeint
solution = odeint(lotkaVolterraSystem, initialPopulations, simulationTime,
                  args=(growthRateGrass, consumptionRateGrassBySheep, sheepDeathRate,
                        sheepBirthRateFromGrass, sheepConsumptionRateByWolves,
                        wolfDeathRate, wolfBirthRateFromSheep))

# Plot the population dynamics over time
plt.plot(simulationTime, solution[:, 0], label='Grass')
plt.plot(simulationTime, solution[:, 1], label='Sheep')
plt.plot(simulationTime, solution[:, 2], label='Wolves')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model: Wolves, Sheep, and Grass Population Dynamics')
plt.legend()
plt.grid(True)
plt.show()

