#!/usr/bin/python3
'''checker module'''
import os
from models.check import Check
from models.project import Project
from models.score import Score
from models.student import Student
from models.task import Task


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


def check_task(tid:str, sid:str):
    t = Task.get(tid)
    p = Project.get(t.pid)
    st = Student.get(sid)
    username = st.github
    parent = p.parent
    project = p.name
    filename = t.name
    out = t.output
    i = os.system('mkdir -p Checker/EXAMINE && git clone ' +
                'https://github.com/{}/{}.git Checker/{} 2>/dev/null'
                .format(username, parent, parent))
    if i != 0:
        print('Check repo')
    basic_checks = simple_check(parent, project, filename, out)
    os.system('rm -rf Checker temp')
    score = 0
    for check in basic_checks:
        if check:
            score += 20
    s = Score.task_by_sid(sid, tid)
    if s == []:
        s = Score({'sid':sid})
    else:
        s = s[0]
    s.tscore = score
    s.save()
    return score
