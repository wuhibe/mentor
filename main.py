from datetime import datetime
import os
import models
from models.check import Check
from models.project import Project
from models.score import Score
from models.student import Student
from models.task import Task
import checker

t = Task.get('101')
p = Project.get(t.pid)
s = Student.get('102')

username = s.github
parent = p.parent
project = p.name
filename = t.name
out = t.output

i = os.system('mkdir -p Checker/EXAMINE && git clone ' +
              'https://github.com/{}/{}.git Checker/{} 2>/dev/null'
              .format(username, parent, parent))
if i != 0:
    print('Check repo')
basic_checks = checker.simple_check(parent, project, filename, out)
print(basic_checks)

os.system('rm -rf Checker temp')
