# coding=utf8
from flask import render_template, request
from . import main
from .forms import CreateActivityForm
from ..models import Activity
from flask.ext.login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateActivityForm()
    return render_template('create.html', form=form)


@main.route('/activitys')
@login_required
def activitys():
    items = Activity.query.all()
    return render_template('activitys.html', items=items)


@main.route('/activitys/stop')
@login_required
def stop_activity():
    return "stop_activity"


# -- test run game --
from flask import Flask

Flask()

@main.route('/run')
def run_game():
    base_href = request.host_url + 'static/games/firefly/'
    return render_template('game-portal.html', base_href=base_href, game_title=u'一起来抓萤火虫')

# -- test form --
from .forms import TestForm

@main.route('/test1')
def test1():
    return render_template('test/test_prize_setting.html')


@main.route('/test2')
def test2():
    form = TestForm()
    return render_template('test/test_dtpicker.html', form=form)


@main.route('/test3')
def test3():
    form = TestForm()
    return render_template('test/test_dtpicker2.html', form=form)