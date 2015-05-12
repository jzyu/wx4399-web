# coding=utf8
from flask import render_template
from . import main
from .forms import CreateActivityForm


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateActivityForm()
    return render_template('create.html', form=form)

# -- test --
from .forms import TestForm

@main.route('/test1')
def test1():
    return render_template('test_prize_setting.html')


@main.route('/test2')
def test2():
    form = TestForm()
    return render_template('test_dtpicker.html', form=form)


@main.route('/test3')
def test3():
    form = TestForm()
    return render_template('test_dtpicker2.html', form=form)