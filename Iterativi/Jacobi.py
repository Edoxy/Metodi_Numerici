import time
import numpy as np
import matplotlib.pyplot as plt

# max iteration of the algorithm
ITERATION_LIMIT = 500
#tollerance: il the approssimation of the current iteration changes by less than the toll, stops the loop
TOLL = 0.000000001
# coefficients matrix
#A = np.array(np.mat('10. -1. +2. +0.0; -1. +11. -1. +3.; +2. -1. +10. -1.; +0.0 +3. -1. +8.'))
# vector of know terms 
#B = np.array([6., 25., -11., 15.])

N = 6
# B = np.array([np.random.choice(range(i*3))*10 for i in range(N)])
# x = range(N)

# A = np.array([[x[i]**j for j in range(N +1)] for i in range(N)])
# print(A,'\n', B)
A = np.array([[4, -1, 0, -1, 0, 0],
            [-1, 4, -1, 0, -1, 0],
            [0, -1, 4, 0, 0, -1],
            [-1, 0, 0, 4, -1, 0],
            [0, -1, 0, -1, 4, -1],
            [0, 0, -1, 0, -1, 4]], float)
B = np.array([2, 1, 2, 2, 1, 2], float)

t1 = time.perf_counter()
# vector of the solution approssimation
Solution = np.zeros(N, float)
# does max number of iteration
for i in range(ITERATION_LIMIT):
    x_temp = Solution.copy()
    for j in range(N):

        sum = 0
        #calculation of the 
        for z in range(N):
            if z != j:
                sum += A[j, z] * x_temp[z]
        Solution[j] = (B[j] - sum) / A[j, j]
    
    err = np.abs(np.max(np.subtract(Solution, x_temp)))
    if err < TOLL:
        break

print(Solution, i)
t2 = time.perf_counter()

print(f'Finisched in {round(t2-t1, 5)} seconds ')

