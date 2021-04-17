import numpy as np
import time


def horner(coef, value):
    t1 = time.perf_counter()
    result = 0
    for i in range(len(coef)):
        result = result * value + coef[i]
    t2 = time.perf_counter()
    print('Horner execution time : ', round(t2-t1, 5))
    return result

def normal(coef, value):
    t1 = time.perf_counter()
    result = 0
    for i in range(len(coef)):
        result = result + coef[i] * (value**i)
        t2 = time.perf_counter()
    print('Normal execution time : ', round(t2-t1, 5))
    return result

if __name__ == '__main__':
    value = 1
    coef = [i-100 for i in range(1000)]
    print(horner(coef, value))
    print(normal(coef, value))

    