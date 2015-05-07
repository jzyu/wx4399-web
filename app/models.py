#-*- coding:utf-8 -*-
from . import db, login_manager
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin


"""
Activity GameCase Award 是1对1关系，即：GameCase和Award本质上同属于Activity表，创建一个Acvitity时同时要新建GameCase和Award
User 和 Activity 是1对多关系
Activity 和 Player 是1对多关系
GameProto 和 GameCase 是1对多关系
"""

# -- util function --


# cmbstr: '60|80|100|'
def cmbstr_make_from_keys(dicts, key, separator):
    """
    把字典列表中的key合并为字符串
    :param dicts: 字典列表，比如：[{'value':60},{'value':80},{'value':100}]
    """
    cmbstr = ''
    for d in dicts:
        cmbstr += (unicode(d[key]) + separator)
    return cmbstr


def cmbstr_get_item(cmbstr, i, separator):
    return cmbstr.split(separator)[i]


def cmbstr_get_item_nr(cmbstr, separator):
    return len(cmbstr.split(separator)) - 1


class Activity(db.Model):
    """ 营销活动
        主键：id
        外键：user_id(1:M), case_id(1:1), award_id(1:1)，
        其他：
            name 活动名称
            status 活动状态 (0停止，1进行中，2已过期)
            ts_start, ts_end 时段：开始时间，结束时间
            nr_player, nr_viewer 统计信息：参与数量(有游戏成绩的player)、传播数量(打开过链接的player)
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(128))
    status = db.Column(db.SmallInteger, default=0)
    ts_start = db.Column(db.TIMESTAMP)
    ts_end = db.Column(db.TIMESTAMP)
    nr_player = db.Column(db.Integer, default=0)
    nr_viewer = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('activity_list', lazy='dynamic'))

    case_id = db.Column(db.Integer, db.ForeignKey('game_case.id'), unique=True, nullable=False)
    game_case = db.relationship('GameCase', backref=db.backref('activity', uselist=False, lazy='noload'))

    award_id = db.Column(db.Integer, db.ForeignKey('award.id'), unique=True, nullable=False)
    award = db.relationship('Award', backref=db.backref('activity', uselist=False, lazy='noload'))

    def __init__(self, user, game_case, award, name, ts_start=None, ts_end=None):
        self.name = name
        self.user = user
        self.game_case = game_case
        self.award = award
        if ts_start is None:
            ts_start = datetime.now()  # NOTE: mysql TIMESTAMP类型对应python datetime.datetime类型
        if ts_end is None:
            ts_end = ts_start + timedelta(days=30)
        self.ts_start = ts_start
        self.ts_end = ts_end

    def __repr__(self):
        return "<Activity %r>" % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(UserMixin, db.Model):
    """ 商户
    主键：id,
    其他：name, email
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    #@password.setter
    #def password(self, password):
    #    self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return "<User %r>" % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#GameCase - 对应的表名为：game_case
class GameCase(db.Model):
    """ 游戏实例 - 游戏的定制信息
    主键：id,
    外键：proto_id(1:M), activity_id(1:1)
    其他：desc_rule, desc_award, 文本描述：游戏规则、奖励信息
         day_play_nr 一天最多可以玩多少次(-1表示不限制)
         help_favor_type   助力受益类型：0=无，1=增加每日可玩次数
         help_favor_value  助力受益值
         share_favor_type  分享受益类型：0=无，1=增加奖品数量，2=增加游戏分数
         share_favor_value 分享受益值
         share_title_fmt share_desc_fmt 微信分享标题和描述的格式
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    desc_rule = db.Column(db.String(2048))
    desc_award = db.Column(db.String(2048))
    day_play_nr = db.Column(db.SMALLINT, default=-1)
    help_favor_type = db.Column(db.SMALLINT, default=0)
    help_favor_value = db.Column(db.Integer, default=0)
    share_favor_type = db.Column(db.SMALLINT, default=0)
    share_favor_value = db.Column(db.Integer, default=0)
    share_title_fmt = db.Column(db.String(256))
    share_desc_fmt = db.Column(db.String(256))

    proto_id = db.Column(db.Integer, db.ForeignKey('game_proto.id'))  #, nullable=False)
    game_proto = db.relationship('GameProto', backref=db.backref('case_list', lazy='dynamic'))

    #activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    #activity = db.relationship('Activity', backref=db.backref('game_case', uselist=False, lazy='dynamic'))

    def __init__(self, game_proto, desc=None, help_favor=None, share_favor=None, day_play_nr=-1, share_fmt=None):
        if desc is None:
            desc = {'rule': game_proto.desc_rule, 'award': game_proto.desc_award}
        if help_favor is None:
            help_favor = {'type': 0, 'value': 0}
        if share_favor is None:
            share_favor = {'type': 0, 'value': 0}
        if share_fmt is None:
            share_fmt = {'title': game_proto.share_title_fmt, 'desc': game_proto.share_desc_fmt}
        self.game_proto = game_proto
        self.desc_award = desc['award']
        self.desc_rule = desc['rule']
        self.help_favor_type = help_favor['type']
        self.help_favor_value = help_favor['value']
        self.share_favor_type = share_favor['type']
        self.share_favor_value = share_favor['value']
        self.day_play_nr = day_play_nr
        self.share_title_fmt = share_fmt['title']
        self.share_desc_fmt = share_fmt['desc']

    def __repr__(self):
        return "<GameCase %r-%r>" % (self.game_proto, self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()


class GameProto(db.Model):
    """ 游戏原型 - 包含：1.游戏可定制的素材和规则 2.游戏实例的默认值
    主键：id,
    其他：name,
        desc_rule, desc_award, 文本描述：游戏规则、奖励信息
        share_title_fmt share_desc_fmt 微信分享标题和描述的格式
        #todo: add 游戏可定制的素材
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(128))
    desc_rule = db.Column(db.String(2048))
    desc_award = db.Column(db.String(2048))
    share_title_fmt = db.Column(db.String(256))
    share_desc_fmt = db.Column(db.String(256))

    def __init__(self, name, desc=None, share_fmt=None):
        if desc is None:
            desc = {'rule': '', 'award': ''}
        if share_fmt is None:
            share_fmt = {'title': '', 'desc': ''}
        self.name = name
        self.desc_award = desc['award']
        self.desc_rule = desc['rule']
        self.share_title_fmt = share_fmt['title']
        self.share_desc_fmt = share_fmt['desc']

    def __repr__(self):
        return "<GameProto %r>" % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Player(db.Model):
    """ 游戏玩家
    主键：id,
    外键：activity_id(1:M)
    其他：oid, nick, sex, city, province, country, imgurl, sub_status, 微信登陆获取的信息
        input_name input_mobile 用户主动输入的名字和手机号码
        highscore 最高得分
        award_value award_status 获奖的数值和领奖状态
        day_remain_nr 今日剩余游戏次数(-1表示次数无限制)
        friends_id 好友列表字符串(游戏转发形成，存储方式：openid | openid ...)
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    oid = db.Column(db.String(64))  # openid
    nick = db.Column(db.String(128))
    city = db.Column(db.String(32))
    province = db.Column(db.String(32))
    country = db.Column(db.String(32))
    imgurl = db.Column(db.String(256))
    sex = db.Column(db.SMALLINT)
    sub_status = db.Column(db.SMALLINT)
    #sub_ts = db.Column(db.TIMESTAMP)
    input_name = db.Column(db.String(32))
    input_mobile = db.Column(db.String(16))
    highscore = db.Column(db.Integer)
    award_value = db.Column(db.Integer)
    award_status = db.Column(db.SMALLINT)
    day_remain_nr = db.Column(db.SMALLINT, default=-1)
    friends_id = db.Column(db.String(3000))

    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    activity = db.relationship('Activity', backref=db.backref('player_list', lazy='dynamic'))

    def __init__(self):
        pass

    def __repr__(self):
        return "<Player %r>" % self.nickname

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_wx_info(self, info):
        self.oid = info['oid']
        self.nick = info['nick']
        self.sex = int(info['sex'])
        self.city = info['city']
        self.province = info['province']
        self.country = info['country']
        self.imgurl = info['imgurl']
        self.sub_status= info['sub_status']


class Award(db.Model):
    """ 奖励
    主键：id,
    外键：activity_id(1:1)
    其他：
        setting_type 奖励设置：
            0 - 无奖，
            1 - 按排名发奖，     award_value 保存2个值：达标分数线 | 奖项个数
            2 - 按分数级别发奖， award_value 保存n个值，n=奖项数
        award_values 奖励的数值，保存形如: 60|80|100
        award_names  各级奖励的奖品，保存形式：iphon6P | Apple Watch | 小米手环
        title_values 各级称号的分值，保存形式：0|20|40|60|80|100
        title_names  各级称号的名称，保存形式：获得“捕虫新手”称号|获得“捕虫新星”称号|获得“捕虫达人”称号
    """

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    award_type = db.Column(db.SMALLINT)
    award_values = db.Column(db.String(2048))
    award_names = db.Column(db.String(2048))
    title_values = db.Column(db.String(2048))
    title_names = db.Column(db.String(2048))

    def __init__(self, awards=None, titles=None):
        if awards is None:
            awards = [{'value': 0, 'name': ''}]
        if titles is None:
            titles = [{'value': 0, 'name': ''}]
        self.award_values = cmbstr_make_from_keys(awards, 'value', '|')
        self.award_names = cmbstr_make_from_keys(awards, 'name', '|')
        self.title_values = cmbstr_make_from_keys(titles, 'value', '|')
        self.title_names = cmbstr_make_from_keys(titles, 'name', '|')

    def __repr__(self):
        return "<Award %r>" % self.id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_award_nr(self):
        return cmbstr_get_item_nr(self.award_values, '|')

    def get_title_nr(self):
        return cmbstr_get_item_nr(self.title_values, '|')

    def get_award_name(self, i):
        return cmbstr_get_item(self.award_names, i, '|')

    def get_title_name(self, i):
        return cmbstr_get_item(self.title_names, i, '|')

