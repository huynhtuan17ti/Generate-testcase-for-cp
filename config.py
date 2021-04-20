import os

class Config(object):
    PROBLEM_NAME = "NKINV"
    PROBLEM_FOLDER = "F:\\ProblemSettingBigO"
    PROBLEM_PATH = os.path.join(PROBLEM_FOLDER, PROBLEM_NAME)
    TESTCASE_FOLDER = os.path.join(PROBLEM_PATH, "testcase") 

    L = 0 # generate testcase with {}.in, {}.ans and {} in [L, R]
    R = 5

    # for checking
    CHECKING_PROBLEM = '3. PHANSO'
    SOLUTION_NAME = 'sol_tuan'
    CHECKING_FOLDER = "C:\\Users\\Asus\\Dropbox\\TA Big-O Competitive Programming\\!CP01\\Level 02\\10. Greatest Common Divisor\\" + PROBLEM_NAME
    CHECKING_TESTCASE = 'test' # name of folder includes testcase