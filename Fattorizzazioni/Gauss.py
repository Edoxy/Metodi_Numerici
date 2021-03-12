import numpy as np

dim = 4
DECIMAL = 2

# M = [[1.0, 22.0, 3.0, 7.0], [2.0, 3.0, 4.0, 45.0], [3.0, 4.0, 6.0, 5.0], [63.0, 5.3, 4.0, 7.0]]
M = np.random.rand(dim, dim)
print(M)

def Gauss(M, dim):
    # Ciclo per ogni riga della matrice
    for i in range (0, dim -1):
        #reset dell'elemento pivot
        pivot = (0, 0)
        # Cicolo per ogni elemento sotto quello diagonale
        for j in range(i, dim):
            #saves and checks the element ofo the colomn
            value = M[j, i]
            if abs(value) > abs(pivot[0]):
                pivot = (value, j)

        #if it found a pivot, it swaps the lines
        if pivot[1] != i:
            temp = M[i].copy()
            M[i] = M[pivot[1]]
            M[pivot[1]] = temp
        #print(f'interation {i} result:\n', M)

        #changes the lines for every line under the pivot
        for j in range(i + 1, dim):

            #compute the factor for every line
            factor = M[j, i]

            #print(pivot[0], factor)
            
            #update avery element of the line
            for z in range(i, dim):
                M[j, z] =  round((M[j, z] * pivot[0] / factor) - M[i, z], DECIMAL)

    return M

print(Gauss(M, dim))