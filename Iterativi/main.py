from Jacobi_Parallel import Jacobi_Parallel
from Gauss_Seidel import Gauss_Seidel
from Jacobi import Jacobi
from magic import magic
import numpy as np
import time

# A = np.array([[4, -1, 0, -1, 0, 0],
#             [-1, 4, -1, 0, -1, 0],
#             [0, -1, 4, 0, 0, -1],
#             [-1, 0, 0, 4, -1, 0],
#             [0, -1, 0, -1, 4, -1],
#             [0, 0, -1, 0, -1, 4]], float)



# # vector of know terms
# B = np.array([2, 1, 2, 2, 1, 2], float)
A = magic(20)
A = np.dot(np.transpose(A), A)
x = np.ones(20)
B = np.dot(A, np.transpose(x))

TOLL = 1.0e-5
IT =1000
#compilation of jacobi function
_ = Jacobi_Parallel(A, B, TOLL, 0)

t1 = time.perf_counter()
x = Jacobi(A, B, TOLL, IT)
t2 = time.perf_counter()
print('Jacobi in', t2-t1)
print(x)

t1 = time.perf_counter()
x = Jacobi_Parallel(A, B, TOLL, IT)
t2 = time.perf_counter()
print('Jacobi Parallel in', t2-t1)
print(x)

t1 = time.perf_counter()
x = Gauss_Seidel(A, B, TOLL, IT)
t2 = time.perf_counter()
print('Gauss Seidel in', t2-t1)
print(x)