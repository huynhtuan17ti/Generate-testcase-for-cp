from GenerativeFunction import *
import random

def write_array(arr):
    return ''.join(map(str, arr))

def swap(u, v):
    return v, u

def writeToFile(f):
    n = random_int(80, 80)
    W = random_int(10**9-5, 10**9)
    f.write(str(n) + ' ' + str(W) + '\n')
    for i in range(n):
        w = random_int(10**6, W)
        v = random_int(900, 10**3)
        f.write(str(w) + ' ' + str(v) + '\n')

