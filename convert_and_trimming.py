import os
from config import Config

cfg = Config()

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

PROBLEM_NAME = cfg.PROBLEM_NAME
PROBLEM_FOLDER = cfg.PROBLEM_FOLDER
PROBLEM_PATH = cfg.PROBLEM_PATH
TESTCASE_FOLDER = cfg.TESTCASE_FOLDER

def convert(file_path):
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
        
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    content = content.strip(bytes(' \t\r', encoding='utf8'))

    with open(file_path, 'wb') as open_file:
        open_file.write(content)

if __name__ == '__main__':
    file_dir = os.listdir(TESTCASE_FOLDER)
    for file in file_dir:
        print("Converting {} ...".format(file), end = ' ')
        file_path = os.path.join(TESTCASE_FOLDER, file)
        convert(file_path)
        print("Done")