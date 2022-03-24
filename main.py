import numpy as np
from numpy.core.fromnumeric import transpose
import math as m
from sub import sub
from multiply import multiply
from check import check

def main():
    epsilon = m.pow(10, -5)
    k = 1
    
    a = [
        [6.92, 1.28, 0.79, 1.15, -0.66],
        [0.92, 3.5, 1.3, -1.62, 1.02],
        [1.15, -2.46, 6.1, 2.1, 1.483],
        [1.33, 0.16, 2.1, 5.44, -18],
        [1.14, -1.68, -1.217, 9, -3]
    ]
    
    b = [11.172, 0.115, 0.009, 9.349, 5.172]
    
    a_new = np.array(a)
    b_new = np.array(b)
    
    a_new, b_new = transpose(a_new)@a_new, transpose(b_new)@b_new
    a = a_new.tolist()
    b = b_new.tolist()
    
    c = []
    d = []
    
    for i in range(len(a)):
        line = []
        for j in range(len(a[i])):
            if i == j:
                line.append(0)
            else:
                line.append(-a[i][j] / a[i][i])
        c.append(line)
        d.append(b[i] / a[i][i])
    
    xOld = [0, 0, 0, 0]
    xNew = [0, 0, 0, 0]
    
    while True:
        k += 1
        for i in range(len(xOld)):
            for j in range(len(xOld)):
                if i > j:
                    xNew[i] += c[i][j] * xNew[j]
                else:
                    xNew[i] += c[i][j] * xOld[j]
            xNew[i] += d[i]
        ax = multiply(a, xNew)
        if (k % 100) == 0:
            print('Iteration -- ', k)
            print('x: ')
            print(xNew)
            r = sub(b, ax)
            print('r: ')
            print(r)
        if (check(xNew, xOld, epsilon)):
            print('Iteration -- ', k)
            print('x: ')
            print(xNew)
            r = sub(b, ax)
            print('r: ')
            print(r)
            break
        xOld = xNew.copy()
        xNew = [0, 0, 0, 0]
    

if __name__ == '__main__':
    main()