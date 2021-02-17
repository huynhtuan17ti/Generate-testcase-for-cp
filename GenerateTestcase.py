from GenerativeFunction import *
import os
import subprocess
from shutil import copy2 
import sys 
from threading import Event
sys.setrecursionlimit(10**6)

NUM_TESTS = 15
PROBLEM_NAME = "RepairingRoad"
PROBLEM_FOLDER = "F:\\ProblemSettingBigO"
PROBLEM_PATH = os.path.join(PROBLEM_FOLDER, PROBLEM_NAME)
TESTCASE_FOLDER = os.path.join(PROBLEM_PATH, "testcase")

FILE_IN = os.path.join(PROBLEM_PATH, PROBLEM_NAME + ".inp")
FILE_OUT = os.path.join(PROBLEM_PATH, PROBLEM_NAME + ".out")
EXE_FILE = os.path.join(PROBLEM_PATH, PROBLEM_NAME + ".exe")

def write_array(arr):
    return ' '.join(map(str, arr))

def generative_main(f):
    n = random_int(9999, 100000)
    m = int(min(n*(n-1)/2, random_int(n, 100000)))
    f.write(str(n) + ' ' + str(m) + '\n') 
    edges = generate_connected_graph(n, m, base = 1)
    edges = add_weight_egdes(edges, 1, 5)
    for (u, v, c) in edges:
        f.write(str(u) + ' ' + str(v) + ' ' + str(c) + '\n')

def create_file(FILE_NAME):
    f = open(FILE_NAME, "w")
    num_test = random_int(1, 2)
    f.write(str(num_test) + '\n')
    while num_test:
        num_test -= 1
        generative_main(f)
    f.close()

if __name__ == '__main__':
    if not os.path.isdir(TESTCASE_FOLDER):
        print('Creating testcase folder ...', end = ' ')
        os.mkdir(TESTCASE_FOLDER)
        print('Done')
 
    for iTest in range(14, NUM_TESTS):
        print('Generating test {} ...'.format(iTest), end = ' ')
        create_file(FILE_IN)
        os.chdir(PROBLEM_PATH)
        subprocess.Popen(PROBLEM_NAME + ".exe")
        
        Event().wait(3) #wait 3 seconds for file exe runs

        copy2(FILE_IN, os.path.join(TESTCASE_FOLDER, "{}.in".format(iTest)))
        copy2(FILE_OUT, os.path.join(TESTCASE_FOLDER, "{}.ans".format(iTest)))
        print('Done')
