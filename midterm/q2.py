import matplotlib.pyplot as plt
import numpy as np
import random 
r=3
K=1000
for K in [500, 1500, 3000]:
    
    Nt=100 #initial popn

    dull_p = 0.05
    dull_popn = Nt * dull_p
    bright_popn = Nt * (1 - dull_p)
    bright_mortality = 0.30
    dull_mortality = 0.05

    popn = ['D']*int(dull_p*Nt) + ['B']*int((1-dull_p)*Nt)
    random.shuffle(popn)

    #run the simulation until 80% of the popn is dull colored
    l1 = [];l2 = []

    count=0
    while popn.count('D')/len(popn) < 0.8:
        N_next= r*Nt * (1 - Nt/K)

        dull_popn = int(N_next * dull_p);bright_popn = int(N_next * (1 - dull_p))

        popn = ['D']*dull_popn + ['B']*bright_popn;random.shuffle(popn);newgeneration = []
        for i in (popn):
            if i == 'D':
                if random.random() > dull_mortality:
                    newgeneration.append('D')
            else:
                if random.random() > bright_mortality:
                    newgeneration.append('B')
        popn = newgeneration;random.shuffle(popn);Nt = len(popn);dull_p = popn.count('D')/len(popn)
        l1.append(popn.count('B'));l2.append(popn.count('D'))
        count+=1
    print(f"No of generations with carrying capacity {K} to reach 80% dull colored population : {count}")

    #plotting the graph
    plt.plot(l1, label='Bright pop. ')
    plt.plot(l2, label='Dull pop. ')
    plt.xlabel('Generations')
    plt.ylabel('popn')
    plt.title(f"Population model with carrying capacity = {K}")
    plt.legend()
    plt.show()