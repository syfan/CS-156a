import numpy as np

c1_tot = 0
c_rand_tot = 0
c_min_tot = 0
trials = 100000
coins = np.zeros((1000,10))

for k in range(trials):
    for i in range(1000):
        for j in range(10):
            result = np.random.rand(1)
            if (result[0] > 0.5): # heads
                coins[i][j] = 1
            else: # tails
                coins[i][j] = 0
    
    heads_per_coin = np.sum(coins, axis = 1)
    c1_tot += float(heads_per_coin[0]) / 10
    c_rand_tot += float(heads_per_coin[np.random.randint(1000)]) / 10
    c_min_tot += float(heads_per_coin[np.argmin(heads_per_coin)]) / 10

v1 = c1_tot / trials
v_rand = c_rand_tot / trials
v_min = c_min_tot / trials
print "v1 " + str(v1) + " v_rand " + str(v_rand) + " v_min " + str(v_min)
