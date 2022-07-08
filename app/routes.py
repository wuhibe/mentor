import random
from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
import models
from models.project import Project
from models.score import Score
from models.student import Student
from models.task import Task
from app import app
import checker


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='404 Error'), 404


@app.errorhandler(500)
def internal_error(error):
    models.db.reload()
    return render_template('500.html', title='500 Error'), 500


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """ method to handle requests made to /register route """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if request.method == 'POST':
        try:
            s = Student.query.filter_by(github=form.github.data).first()
            if s:
                flash('GitHub is already registered')
                return redirect(url_for('register'))
            email = Student.query.filter_by(email=form.email.data).first()
            if email:
                flash('Email already in use')
                return redirect(url_for('register'))
        except Exception:
            pass
        if form.validate_on_submit():
            dct = {
                'email': form.email.data,
                'github': form.github.data,
                'first_name': form.fname.data,
                'last_name': form.lname.data
            }
            user = Student(**dct)
            user.set_password(form.password.data)
            user.save()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        else:
            flash('Check details')
            return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)


@app.route('/', strict_slashes=False)
def dashboard():
    return render_template('dash.html', title='Home')


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ method to handle requests made to /login route """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)


@app.route('/index', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def profile():
    form = RegistrationForm()
    s = Student.get_by_email(current_user.email)
    if request.method == 'POST':
        try:
            st = Student.query.filter_by(github=form.github.data).first()
            if st and st.id != s.id:
                flash('Please use your own github.')
                return redirect(url_for('profile'))
            st = Student.query.filter_by(email=form.email.data).first()
            if st and st.id != s.id:
                flash('Email already in use')
                return redirect(url_for('profile'))
        except Exception:
            pass
        s.github = form.github.data,
        s.first_name = form.fname.data,
        s.last_name = form.lname.data
        s.set_password(form.password.data)
        s.save()
        flash('Changes have been saved!')
        return redirect(url_for('profile'))
    return render_template('profile.html', title='User Profile',
                           form=form, user=s)


@app.route('/resources', strict_slashes=False)
@login_required
def resources():
    return render_template('resources.html', title='Resources')


@app.route('/projects', strict_slashes=False)
@login_required
def projects():
    projects = Project.all()
    return render_template('projects.html', title='Projects',
                           projects=projects)


@app.route('/projects/<id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def project(id):
    project = Project.get(id)
    if project == []:
        abort(404)
    s = Student.get_by_email(current_user.email)
    if request.method == 'POST':
        tid = str(request.form['task'])
        checker.check_task(tid, s.id)
    tasks = []
    score = Score.all_tasks(s.id)
    if project is not None:
        tasks = Task.get_all_tasks(project.id)
    return render_template('tasks.html', title='Project - {}'.format(id),
                           project=project, tasks=tasks, score=score)


@app.route('/logout', strict_slashes=False)
@login_required
def logout():
    """ method to handle requests made to /logout route """
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000,)
