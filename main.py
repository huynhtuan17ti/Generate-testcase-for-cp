from GenerativeFunction import *
import random
import math

def write_array(arr):
    return ' '.join(map(str, arr))

def swap(u, v):
    return v, u

def generate_string(n):
    s = []
    for j in range(n):
        t = percentage_chose(50)
        if t:
            s.append(1)
        else:
            s.append(0)
    return s

def calc(a, b, n):
    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1
    return cnt

def check(a, s, n):
    S = set()
    for arr in a:
        val = calc(arr, s, n)
        if val > 5:
            return -1
        S.add(val)
    if len(S) == 1:
        return S.pop()
    else:
        return -1

def change(s, pos, new):
    l = list(s)
    l[pos] = chr(new + ord('a'))
    s = ''.join(l)
    return s

def writeToFile(f):
    n = random_int(50000, 60000)
    a = random_array(1, 60000, n)
    f.write(str(n) + '\n')
    for i in range(n):
        f.write(str(a[i]) + '\n')

    
    

