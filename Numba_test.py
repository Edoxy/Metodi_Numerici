from numba import jit
import numpy as np
import time

t1 = time.perf_counter()

@jit(nopython= True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = np.random.random()
        y = np.random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


print(monte_carlo_pi(1))#first compilation
print(monte_carlo_pi(10000000))#the secondo call is much more efficient because it's already compiled

t2 = time.perf_counter()

print(f'Finisched in {round(t2-t1, 5)} seconds')