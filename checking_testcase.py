import sys
import os
import subprocess
from threading import Event
from shutil import copy2 
import filecmp
from convert_and_trimming import convert
from config import Config

cfg = Config()

PROBLEM_NAME = cfg.CHECKING_PROBLEM
SOLUTION_NAME = cfg.SOLUTION_NAME
FOLDER_PATH = cfg.CHECKING_FOLDER
TESTCASE_PATH = os.path.join(FOLDER_PATH, CHECKING_TESTCASE)

if __name__ == '__main__':
    testcase_list = os.listdir(TESTCASE_PATH)
    print('Found {} files (include .in .ans file)'.format(len(testcase_list)))
    for file in testcase_list:
        if 'in' in file:
            name = file[:-3]
            print('Checking test {} ... '.format(name), end = '')
            FILE_IN = os.path.join(TESTCASE_PATH, file)
            FILE_OUT = os.path.join(TESTCASE_PATH, name + '.ans')
            copy2(FILE_IN, os.path.join(FOLDER_PATH, SOLUTION_NAME + '.inp'))

            # Run file exe
            os.chdir(FOLDER_PATH)
            subprocess.Popen(SOLUTION_NAME + ".exe")
            Event().wait(3) #wait 3 seconds for file exe runs

            # Convert file out to CLR
            convert(os.path.join(FOLDER_PATH, SOLUTION_NAME + '.out'))

            # Compare two file out
            if not filecmp.cmp(FILE_OUT, os.path.join(FOLDER_PATH, SOLUTION_NAME + '.out')):
                print("Output wrong!")
                break
            else:
                print("Output goes brrr!")




