import random
import matplotlib.pyplot as plt

# Define target DNA sequence and other constants
seq = "ACTTGATTGG"
L = len(seq)
mu = 0.1  # Fixed mutation rate

def parent_seq(length):
    return ''.join(random.choice("ATGC") for _ in range(length))

def rep_seq(parental_seq, mutation_rate):
    offspring = ""
    for nucleotide in parental_seq:
        if random.random() < mutation_rate:
            offspring += random.choice("ATGC")
        else:
            offspring += nucleotide
    return offspring

def sim(f, num_rep):
    finalgen = 0
    for _ in range(num_rep):
        pseq = parent_seq(L)
        gen = 1
        while pseq != seq:
            c_seq = [rep_seq(pseq, mu) for _ in range(f)]
            choose = max(c_seq, key=lambda seq: sum(1 for base1, base2 in zip(seq, seq) if base1 == base2))
            pseq = choose
            gen += 1
        finalgen += gen
    return finalgen / num_rep

# Varying brood size (f)
f_values = [2, 5, 10, 20, 50, 100]
num_rep = 10  # Number of replicates for each f value

genlist = []
for f in f_values:
    avg = sim(f, num_rep)
    genlist.append(avg)

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(f_values, genlist, marker='o')
plt.title("Average Generations vs. Brood Size (Mutation rate = 0.1)")
plt.xlabel("Brood Size (f)")
plt.ylabel("Average Generations to Target")
plt.grid(True)
plt.show()
# Varying mutation rate (mu)
mu_values = [0.05, 0.1, 0.2, 0.5, 0.8]
f = 10  # Fixed brood size

avg_generations_mu = []
for mu in mu_values:
    avg = sim(f, num_rep)
    avg_generations_mu.append(avg)

#return the number of generations needed to reach the target sequence in 10 replicates
print(f"Average generations needed to reach target sequence (f=10, mu=0.1): {avg_generations_mu[1]}")

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(mu_values, avg_generations_mu, marker='o')
plt.title("Average generations needed to reach target sequence (f=10)")
plt.xlabel("variance of G with change in mutation rate")
plt.ylabel("Average Generations to Target")
plt.grid(True)
plt.show()

