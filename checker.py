#!/usr/bin/python3
'''checker module'''
import os


def file_exists(parent, project, filename):
    ''' file exists check '''
    i = os.system('cp Checker/{}/{}/{}.py Checker/EXAMINE/ 2> /dev/null'
                  .format(parent, project, filename))
    return i == 0


def pycode_perm_decor(filename):
    ''' check file for coding conventions '''
    os.system('pycodestyle Checker/EXAMINE/{}.py > temp'.format(filename))
    with open('temp', 'r') as file:
        r = file.read()
        pycode = (r == '')
    os.system('stat -c "%a" Checker/EXAMINE/{}.py > temp'.format(filename))
    with open('temp', 'r') as file:
        r = file.read()
        perm = (eval(r)//100 == 7)
    with open('Checker/EXAMINE/{}.py'.format(filename), 'r') as file:
        r = file.readlines()
        # first line is shebang and last character is newline
        decor = r[0] == '#!/usr/bin/python3\n' and r[-1][-1] == '\n'
    return (pycode, perm, decor)


def simple_check(parent, project, filename, out):
    ''' function that runs checks
        Return -> List with:
            0 - File Exists
            1 - Pycodestyle
            2 - File permissions
            3 - Shebang and final empty line
            4 - Correct output
    '''
    if file_exists(parent, project, filename):
        pycode, perm, decor = pycode_perm_decor(filename)
        os.system('python3 Checker/EXAMINE/{}.py > temp'.format(filename))
        with open('temp', 'r') as file:
            r = file.read()
            case = (r == out)
        return [True, pycode, perm, decor, case]
    return [False for i in range(0, 5)]
