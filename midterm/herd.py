import numpy as np

import matplotlib.pyplot as plt

def plot_population(k, proportion, title):
    population_size = 1000
    i_pop = int(proportion * population_size);S_pop = population_size - i_pop
    imx = np.random.rand(i_pop);imy = np.random.rand(i_pop)
    Sx = np.random.rand(S_pop);Sy = np.random.rand(S_pop)
    
    k.scatter(imx, imy, c='green', label='Immune');k.scatter(Sx, Sy, c='yellow', label='Susceptible')
    k.set_title(title)
    k.set_xticks([]);k.set_yticks([]);k.legend()

fig, k = plt.subplots(1, 3, figsize=(15, 5))
plot_population(k[0], proportion=0.1, title='fig1');plot_population(k[1], proportion=0.5, title= 'fig2');plot_population(k[2], proportion=0.8, title= 'fig3')

plt.show()
