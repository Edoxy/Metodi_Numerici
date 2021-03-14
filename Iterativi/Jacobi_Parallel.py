import time
import numpy as np
import numpy.matlib
from numba import jit
from sparce_matrix import sprandsym


# max iteration of the algorithm
ITERATION_LIMIT = 500
# tollerance: il the approssimation of the current iteration changes by less than the toll, stops the loop
TOLL = 0.000000001
# coefficients matrix
A = np.array([[4, -1, 0, -1, 0, 0],
            [-1, 4, -1, 0, -1, 0],
            [0, -1, 4, 0, 0, -1],
            [-1, 0, 0, 4, -1, 0],
            [0, -1, 0, -1, 4, -1],
            [0, 0, -1, 0, -1, 4]], float)



# vector of know terms
B = np.array([2, 1, 2, 2, 1, 2], float)
DIM = 6


@jit(nopython=True, parallel=True)
def Jacobi(Solution, IM):
    for i in range(IM):
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

#FIRST COMPILATION OF THE FUNCTION
_ = Jacobi(np.zeros_like(B), 0)

start = time.perf_counter()

# vector of the solution approssimation
Solution = np.zeros_like(B)

print(Jacobi(Solution, ITERATION_LIMIT))

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 5)} second(s)')