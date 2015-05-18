# coding=utf8
import json
from flask import request
from flask.ext.cors import cross_origin
from flask import Blueprint

gapi = Blueprint('gapi', __name__)


@gapi.route('/getScoreInfo')
@cross_origin()
# 游戏部署在80端口，wx4399-web部署在8080端口，需要cors才能访问
def get_scoreboard_info():
    infos = [
        {'rank': 1, 'uid': '1234aaa', 'nickname': '冠军名字', 'score': 999, 'headicon': 'http://download.easyicon.net/png/1072002/128/'},
        {'rank': 2, 'uid': '1234bbb', 'nickname': '亚军名字', 'score': 888, 'headicon': 'http://download.easyicon.net/png/1071996/128/'},
        {'rank': 3, 'uid': '1234ccc', 'nickname': '季军名字', 'score': 777, 'headicon': 'http://download.easyicon.net/png/1072032/128/'},
        {'rank': 4, 'uid': '1234ddd', 'nickname': '张三aaa4', 'score': 666, 'headicon': 'http://download.easyicon.net/png/1100252/128/'},
        {'rank': 5, 'uid': '1234eee', 'nickname': '老王bbb5', 'score': 555, 'headicon': 'http://download.easyicon.net/png/1160288/128/'},
        {'rank': 6, 'uid': '1234fff', 'nickname': '昵称超长测试昵称超长测试6', 'score': 444, 'headicon': 'http://download.easyicon.net/png/1160289/128/'},
        {'rank': 7, 'uid': '1234ggg', 'nickname': '坏boycc7', 'score': 333, 'headicon': 'http://download.easyicon.net/png/1064545/128/'},
        {'rank': 8, 'uid': '1234hhh', 'nickname': '坏boycc8', 'score': 222, 'headicon': 'http://download.easyicon.net/png/1064535/128/'},
        {'rank': 9, 'uid': '1234iii', 'nickname': '坏boycc9', 'score': 200, 'headicon': 'http://download.easyicon.net/png/1064533/128/'},
        {'rank': 10,'uid': '1234jjj', 'nickname': '坏boycc10', 'score': 199, 'headicon': 'http://download.easyicon.net/png/1064539/128/'},
        {'rank': 11, 'uid': '1234kkk', 'nickname': 'Name 11', 'score': 188, 'headicon': 'http://download.easyicon.net/png/1064533/128/'},
        {'rank': 12, 'uid': '1234lll', 'nickname': 'name 12', 'score': 177, 'headicon': 'http://download.easyicon.net/png/1064539/128/'}
    ]
    resp_text = json.dumps(infos)
    return resp_text


@gapi.route('/saveHighScore')
@cross_origin()
def save_high_score():
    uid = str(request.args.get('uid'))
    score = int(request.args.get('score'))
    return 'save_high_score ok, uid = %s, score = %d' % (uid, score)


@gapi.route('/saveAwardInfo')
@cross_origin()
def save_award_info():
    uid = str(request.args.get('uid'))
    name = request.args.get('name')
    mobile = str(request.args.get('mobile'))
    return 'save_award_info ok, uid = %s, name = %s, mobile = %s' % (uid, name, mobile)