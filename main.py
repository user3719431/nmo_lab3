from cv2 import transpose
import numpy as np
import math as m

def main():
    e = m.pow(10, -5)
    
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
    
    a_new, b_new = transpose
    

if __name__ == '__main__':
    main()