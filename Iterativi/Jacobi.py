import time
import numpy as np

# max iteration of the algorithm
ITERATION_LIMIT = 100000

def Jacobi(A, B, TOLL, ITERATION_LIMIT = ITERATION_LIMIT):
    DIM = A.shape[0]
    Solution = np.zeros(DIM, float)
    # does max number of iteration
    for i in range(ITERATION_LIMIT):
        x_temp = Solution.copy()
        for j in range(DIM):

            sum = 0
            #calculation of the 
            for z in range(DIM):
                if z != j:
                    sum += A[j, z] * x_temp[z]
            Solution[j] = (B[j] - sum) / A[j, j]
        
        err = np.abs(np.max(np.subtract(Solution, x_temp)))
        if err < TOLL:
            break
    return (Solution, i)