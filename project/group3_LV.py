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

# Desired equilibrium ranges
desiredGrassRange = (200, 300)
desiredSheepRange = (160, 210)
desiredWolfRange = (20, 60)

# Initial populations
initialGrassPopulation = 200
initialSheepPopulation = 100.0
initialWolfPopulation = 50.0
initialPopulations = [initialGrassPopulation, initialSheepPopulation, initialWolfPopulation]

# Time points for simulation
simulationTime = np.linspace(0, 150, 150 * 20)  # Simulate for 150 time units with 20 points per unit time

# Parameters for the Lotka-Volterra model
growthRateGrass = 0.04
consumptionRateGrassBySheep = 0.01
sheepDeathRate = 0.5
sheepBirthRateFromGrass = 0.02
sheepConsumptionRateByWolves = 0.05
wolfDeathRate = 0.5
wolfBirthRateFromSheep = 0.02

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
