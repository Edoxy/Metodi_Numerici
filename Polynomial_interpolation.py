import numpy as np

N = 10
Points = np.random.rand(N)
x = range(N)

A = np.array([[x[i]**j for j in range(N +1)] for i in range(N)])
print(A)