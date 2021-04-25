from GenerativeFunction import *
import random
import math

def write_array(arr):
    return ' '.join(map(str, arr))

def swap(u, v):
    return v, u

def writeToFile(f):
    line = random_int(800, 1000)
    for _ in range(line):
        num = random_int(1, 3)
        if num == 1:
            n = random_int(200, 300)
            f.write(str(n) + '\n')
        elif num == 2:
            n = random_int(200, 300)
            L1 = random_int(0, 1000)
            f.write(str(n) + ' ' + str(L1) + '\n')
        else:
            n = random_int(200, 300)
            L1 = random_int(0, 1000)
            L2 = random_int(L1, 1000)
            f.write(str(n) + ' ' + str(L1) + ' ' + str(L2) + '\n')
    
    

