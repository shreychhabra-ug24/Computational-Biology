import matplotlib.pyplot as plt
#this is just a slightly modified version of the code from class.
p = 10
iterations = 500
k = 60
a = 0.3
rate = []
pop = []

r = 0.1
while r < 4:
    n = p
    for t in range(iterations):
        n = n * r * (1 - n / k) + a * n
        if t > 100:
            rate.append(r);pop.append(n)
    r += 0.005

plt.plot(rate, pop, 'k,', markersize=0.1);plt.ylabel("population for overlapping populations");plt.show()