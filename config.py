import os

class Config(object):
    PROBLEM_NAME = "NKINV"
    PROBLEM_FOLDER = "F:\\ProblemSettingBigO"
    PROBLEM_PATH = os.path.join(PROBLEM_FOLDER, PROBLEM_NAME)
    TESTCASE_FOLDER = os.path.join(PROBLEM_PATH, "testcase") 

    L = 0 # generate testcase with {}.in, {}.ans and {} in [L, R]
    R = 5