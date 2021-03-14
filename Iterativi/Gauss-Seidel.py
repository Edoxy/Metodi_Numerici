import time
import numpy as np
t1 = time.perf_counter()

# max iteration of the algorithm
ITERATION_LIMIT = 10000
#Dont know how to implemet tollerance
TOLL = 0.000000001
DIM = 6
# coefficients matrix
#A = np.array(np.mat('10. -1. +2. +0.0; -1. +11. -1. +3.; +2. -1. +10. -1.; +0.0 +3. -1. +8.'))
A = np.array([[4, -1, 0, -1, 0, 0],
            [-1, 4, -1, 0, -1, 0],
            [0, -1, 4, 0, 0, -1],
            [-1, 0, 0, 4, -1, 0],
            [0, -1, 0, -1, 4, -1],
            [0, 0, -1, 0, -1, 4]], float)
#print(A)
#A = np.random.rand(DIM, DIM)
# vector of know terms 
#B = np.array([6., 25., -11., 15.])
B = np.array([2, 1, 2, 2, 1, 2], float)
#print(B)
#B = np.random.rand(DIM)

# vector of the solution approssimation
Solution = np.zeros_like(B)
# does max number of iteration
for i in range(ITERATION_LIMIT):
    x_temp = Solution.copy()

    for j in range(A.shape[0]):

        sum = 0
        #calculation of the 
        for z in range(A.shape[0]):
            if z != j:
                sum += A[j, z] * Solution[z]
        Solution[j] = (B[j] - sum) / A[j, j]
    err = np.abs(np.max(np.subtract(Solution, x_temp)))
    if err < TOLL:
        break

print(Solution, i)
t2 = time.perf_counter()

print(f'Finisched in {round(t2-t1, 5)} seconds')