# coding=utf8
from flask import render_template
from . import main
from .forms import CreateActivityForm1, CreateActivityForm2


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/create', methods=['GET', 'POST'])
def create():
    form1 = CreateActivityForm1()
    form2 = CreateActivityForm2()
    return render_template('create.html', form1=form1, form2=form2)


@main.route('/test1')
def test1():
    return render_template('test1.html')