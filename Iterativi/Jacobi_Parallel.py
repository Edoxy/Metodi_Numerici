from numba import jit
import time
import numpy as np

MAX_IT = 1000

@jit(nopython=True, parallel=True)
def Jacobi_Parallel(A, B, TOLL, MAX_IT = MAX_IT):
    #A matrix, B Const, Tollerance, use = true
    Solution = np.zeros_like(B)
    DIM = A.shape[0]

    for i in range(MAX_IT):
        x_temp = Solution.copy()
        
        for j in range(DIM):
            sum = 0
            for z in range(DIM):
                if z != j:
                    sum += A[j, z] * x_temp[z]
            Solution[j] = (B[j] - sum) / A[j, j]
        #print(Solution)

        err = np.abs(np.max(np.subtract(Solution, x_temp)))
        if err < TOLL:
            break
    
    return (Solution, i)