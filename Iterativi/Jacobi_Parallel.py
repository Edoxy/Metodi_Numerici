import time
import numpy as np
import numpy.matlib
from numba import jit
from sparce_matrix import sprandsym


# max iteration of the algorithm
ITERATION_LIMIT = 500
# tollerance: il the approssimation of the current iteration changes by less than the toll, stops the loop
TOLL = 0.0001
# coefficients matrix
# A = np.array([[4, -1, 0, -1, 0, 0],
#             [-1, 4, -1, 0, -1, 0],
#             [0, -1, 4, 0, 0, -1],
#             [-1, 0, 0, 4, -1, 0],
#             [0, -1, 0, -1, 4, -1],
#             [0, 0, -1, 0, -1, 4]], float)

A = sprandsym(400, 0.01).toarray()

# vector of know terms
#B = np.array([2, 1, 2, 2, 1, 2], float)
B = np.zeros(400)
DIM = 400

# @jit(nopython = True)
# def iteration(x_temp, j):
#     sum = 0
#     for z in range(DIM):
#         if z != j:
#             sum += A[j, z] * x_temp[z]
#     return (B[j] - sum) / A[j, j]

@jit(nopython=True , parallel = True)
def func(x_temp):
    results = np.zeros(DIM)
    for j in range(DIM):
        sum = 0
        for z in range(DIM):
            if z != j:
                sum += A[j, z] * x_temp[z]
        results[j] = (B[j] - sum) / A[j, j]
    
    return results



if __name__ == '__main__':
    _ = func(np.zeros_like(B)) #FIRST COMPILATION OF THE FUNCTION

    start = time.perf_counter()

    # vector of the solution approssimation
    Solution = np.zeros_like(B)
    
    # does max number of iteration
    
    for i in range(ITERATION_LIMIT):
        x_temp = Solution.copy()
        
        results = func(x_temp)

        Solution = results.copy()
        #print(Solution)

        err = np.abs(np.max(np.subtract(Solution, x_temp)))
        if err < TOLL:
            break

    print(Solution, i)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 5)} second(s)')