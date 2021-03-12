import time
import numpy as np
t1 = time.perf_counter()

# max iteration of the algorithm
ITERATION_LIMIT = 5
#Dont know how to implemet tollerance
TOLL = 0.001
DIM = 100
# coefficients matrix
A = np.array(np.mat('10. -1. +2. +0.0; -1. +11. -1. +3.; +2. -1. +10. -1.; +0.0 +3. -1. +8.'))
#A = np.random.rand(DIM, DIM)
# vector of know terms 
B = np.array([6., 25., -11., 15.])
#B = np.random.rand(DIM)

# vector of the solution approssimation
Solution = B.copy()
# does max number of iteration
for i in range(ITERATION_LIMIT):

    for j in range(A.shape[0]):

        sum = 0
        #calculation of the 
        for z in range(A.shape[0]):
            if z != j:
                sum += A[j, z] * Solution[z]
        Solution[j] = round((B[j] - sum) / A[j, j], 2)
    

print(Solution, i)
t2 = time.perf_counter()

print(f'Finisched in {round(t2-t1, 5)} seconds')