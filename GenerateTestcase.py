from GenerativeFunction import *
import os
import subprocess
from shutil import copy2 

NUM_TESTS = 5
PROBLEM_NAME = "Tester"
PROBLEM_FOLDER = "F:\\ProblemSettingBigO"
PROBLEM_PATH = os.path.join(PROBLEM_FOLDER, PROBLEM_NAME)
TESTCASE_FOLDER = os.path.join(PROBLEM_PATH, "testcase")

FILE_IN = os.path.join(PROBLEM_PATH, PROBLEM_NAME + ".inp")
FILE_OUT = os.path.join(PROBLEM_PATH, PROBLEM_NAME + ".out")
EXE_FILE = os.path.join(PROBLEM_PATH, PROBLEM_NAME + ".exe")

def write_array(arr):
    return ' '.join(map(str, arr))

def generative_main(f):
    n = random_int(4, 10)
    f.write(str(n) + '\n')
    arr = random_array(0, 10, n)
    f.write(write_array(arr))

def create_file(FILE_NAME):
    f = open(FILE_NAME, "w")
    generative_main(f)
    f.close()

if __name__ == '__main__':
    if not os.path.isdir(TESTCASE_FOLDER):
        print('Creating testcase folder ...', end = ' ')
        os.mkdir(TESTCASE_FOLDER)
        print('Done')
 
    for iTest in range(NUM_TESTS):
        print('Generating test {} ...'.format(iTest), end = ' ')
        create_file(FILE_IN)
        os.chdir(PROBLEM_PATH)
        subprocess.Popen(PROBLEM_NAME + ".exe")

        copy2(FILE_IN, os.path.join(TESTCASE_FOLDER, "{}.in".format(iTest)))
        copy2(FILE_OUT, os.path.join(TESTCASE_FOLDER, "{}.ans".format(iTest)))
        print('Done')
