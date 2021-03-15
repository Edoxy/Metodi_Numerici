import time
import numpy as np
t1 = time.perf_counter()

# max iteration of the algorithm
ITERATION_LIMIT = 10000

def Gauss_Seidel(A, B, TOLL, ITERATION_LIMIT = ITERATION_LIMIT):
    Solution = np.zeros_like(B)
    DIM = A.shape[0]
    # does max number of iteration
    for i in range(ITERATION_LIMIT):
        x_temp = Solution.copy()

        for j in range(DIM):
            sum = 0
            #calculation of the 
            for z in range(DIM):
                if z != j:
                    sum += A[j, z] * Solution[z]
            Solution[j] = (B[j] - sum) / A[j, j]
        err = np.abs(np.max(np.subtract(Solution, x_temp)))
        if err < TOLL:
            break
    return (Solution, i)