import matplotlib.pyplot as plt

N0 = 15
K = 60
r_values = [1, 1.5, 2.8, 3.1, 3.4, 3.8]
gen = 100

for r in r_values:
    t_list = []
    n_list = []

    n = N0
    for t in range(gen):
        n = r * n * (1 - n / K)
        t_list.append(t)
        n_list.append(n)

    plt.plot(t_list, n_list, '-')
    plt.show()
plt.xlabel("Generations")
plt.ylabel("Scaled population size")
plt.ylim((0, K))
plt.legend([f"r = {r}" for r in r_values])
