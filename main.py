from GenerativeFunction import *
import random
import math

def write_array(arr):
    return ''.join(map(str, arr))

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

def writeToFile(f):
    n = random_int(1990, 2000)
    f.write(str(n) + '\n')
    for i in range(n):
        t, c = random_int(0, 10), random_int(1, 10**9)
        f.write(str(t) + ' ' + str(c) + '\n')

#safe
def writeToFile_(f):
    n = random_int(30, 35)
    m = random_int(8, 10)
    f.write(str(n) + ' ' + str(m) + '\n')
    res = random_int(1, 1)
    a = []
    for i in range(res):
        a.append(generate_string(n))

    for i in range(m):
        s = generate_string(n)
        while check(a, s, n) == -1:
            s = generate_string(n)

        c = check(a, s, n)
        f.write(write_array(s) + ' ' + str(c) + '\n')

