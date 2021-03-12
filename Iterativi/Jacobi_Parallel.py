import time
import numpy as np
import numpy.matlib
import concurrent.futures


# max iteration of the algorithm
ITERATION_LIMIT = 500
# tollerance: il the approssimation of the current iteration changes by less than the toll, stops the loop
TOLL = 0.001
DIM =20

def iteration(data):
    #print('Iteration thread: ',data)
    sum = 0
    j = data[0]
    x_temp = data[1]
    A = data[2]
    B = data[3]
    for z in range(DIM):
        if z != j:
            sum += A[z] * x_temp[z]
    return (B - sum) / A[j]




if __name__ == '__main__':

    # coefficients matrix
    A = np.random.rand(DIM, DIM)

    # vector of know terms
    B = np.random.rand(DIM)

    start = time.perf_counter()

    # vector of the solution approssimation
    Solution = B.copy()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # does max number of iteration
        for i in range(ITERATION_LIMIT):
            x_temp = Solution.copy()

            data = [(j, x_temp, A[j], B[j]) for j in range(A.shape[0])]
            results = executor.map(iteration, data)

            Solution = np.array([result for result in results])
            #print(Solution)

            err = np.abs(np.max(np.subtract(Solution, x_temp)))
            if err < TOLL:
                break

    print(Solution, i)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')