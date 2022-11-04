# Mentor - WebStack Portfolio Project

## Overview

Mentor is a platform inspired by online learning platforms such as HackerRank and ALX's very own intranet.

A student can register and add his email and password for registration, as well as his github link on which he will be completing his projects. Upon requesting a check for his code on Mentor, the content and output of his code will be checked against a set of criteria and be graded accordingly.

## Setting up the Project

- Install dependencies

```
$ pip install -r requirements.txt
```

- Create `mentor` table in database

```
$ cat init.sql | mysql -u [USER] -p
Enter password: [PASSWORD]
```

- Run the project

```
$ HOST_USR=[USER] HOST_PWD=[PASSWORD] python3 -m app.routes
```

The SQLAlchemy ORM creates all the neccesary tables during this step.

- Run the setup query to have sample data in the database

```
$ cat setup.sql | mysql -u [USER] -p mentor
Enter password: [PASSWORD]
```

## Usage

- After setting up the project, register yourself as a new user and add a github link

- Browse to Projects tab and view the projects

- If tasks exist, press `Check` to start the checker

- View your grades for the given task.

| Your Grades will be calculated based on: |
|---|
| 0 - File Exists|
| 1 - Pycodestyle|
| 2 - File permissions|
| 3 - Shebang and final empty line|
| 4 - Correct output|

> **Warning**
> The project is created as a demonstration and will clone and run code on your local machine if the filenames match. Use with caution.

## Author

- Wuhibeselassie Tamire - [Github](https://github.com/wuhibe) / [LinkedIn](https://linkedin.com/in/wuhibeselassie-nigatu)

## Screenshots

<div>
    <img src="screenshots/register.png" alt="register">
    <img src="screenshots/login.png" alt="login">
    <img src="screenshots/landing_page.png" alt="landing Page" >
    <img src="screenshots/projects.png" alt="projects">
    <img src="screenshots/tasks.png" alt="Tasks">
    <img src="screenshots/checker.png" alt="Checker">
    <img src="screenshots/resources.png" alt="Resources">
</div>
