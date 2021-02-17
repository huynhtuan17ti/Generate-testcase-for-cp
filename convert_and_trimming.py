import os

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

PROBLEM_NAME = "Tester"
PROBLEM_FOLDER = "F:\\ProblemSettingBigO"
PROBLEM_PATH = os.path.join(PROBLEM_FOLDER, PROBLEM_NAME)
TESTCASE_FOLDER = os.path.join(PROBLEM_PATH, "testcase")

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