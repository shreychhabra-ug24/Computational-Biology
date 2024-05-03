import random
import matplotlib.pyplot as plt

num_generations = 200  # Maximum number of generations per simulation
num_simulations = 100  # Number of simulations per population size
dark_survival_prob = 0.95  # Survival probability for dark-colored mice
light_survival_prob = 0.90  # Survival probability for light-colored mice
offspring_count = 3  # Number of offspring each surviving mouse produces

# List of population sizes to test
population_sizes = [10, 50, 100, 500]

# Function to run a single simulation until we reach either fixation or the maximum number of generations
def simulate_fixation(population_size):
    dark_percentage = 0.05
    population = ['D'] * int(population_size * dark_percentage) + ['L'] * int(population_size * (1 - dark_percentage))
    random.shuffle(population)
    
    for t in range(num_generations):    # Loop through generations
        offspring = []
        for i in population:
            prob = random.random()      # Generate a random number between 0 and 1
            if i == 'L':
                if prob < light_survival_prob:
                    offspring.extend(['L'] * offspring_count)   # Add offspring_count number of 'L' to the offspring list
            else:
                if prob < dark_survival_prob:
                    offspring.extend(['D'] * offspring_count)   # Add offspring_count number of 'D' to the offspring list
                    
        population = random.sample(offspring, population_size)
        dark_percentage = population.count('D') / len(population)   # Calculate the percentage of dark-colored mice
        
        # Check for fixation (100% of population)
        if dark_percentage == 1.0:
            return True
    
    return False  


fixation_probabilities = []     # List to store fixation probabilities for each population size

# Run simulations for each population size
for population_size in population_sizes:        
    fixation_count = 0
    for i in range(num_simulations):    # Run multiple simulations for each population size
        if simulate_fixation(population_size):
            fixation_count += 1
    
    # Calculate fixation probability across simulations
    fixation_probability = fixation_count / num_simulations
    fixation_probabilities.append(fixation_probability)

# Plotting the relationship between population size and fixation probability
plt.figure(figsize=(10, 8))
plt.plot(population_sizes, fixation_probabilities, marker='o')
plt.title('Population Size vs Fixation Probability for Dark-Colored Mice')
plt.xlabel('Population Size')
plt.ylabel('Fixation Probability')
plt.show()
