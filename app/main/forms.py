# coding=utf8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import Required, Email, Length


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your email?', validators=[Required(), Email(), Length(1, 64)])
    submit = SubmitField('Submit')


class CreateActivityForm1(Form):
    name = StringField(u'游戏名称', validators=[Required()], description=u'不能超过64个字')
    ts_start = DateTimeField(u'开始时间', validators=[Required], description=u'必填')
    ts_end = DateTimeField(u'结束时间', validators=[Required], description=u'必填，必须大于开始时间')
    rule = StringField(u'活动规则', validators=[Required], description=u'不能超过300个字')
    subs_link = StringField(u'关注链接', validators=[Required], description=u'请前往微信公众平台新建图文，将新建好的图文链接填入输入框即可实现一键关注')
    next_step = SubmitField(u'下一步')

class CreateActivityForm2(Form):
    name = StringField(u'奖品名称', validators=[Required()], description=u'圣诞树全部点亮后玩家可获赠奖品的名称，一棵点亮的圣诞树对应一个奖品，派发完即止')
    count1 = IntegerField(u'奖品数量', validators=[Required], description=u'商家提供给玩家的奖品数量，一棵点亮的圣诞树对应一个奖品，派发完即止，数值范围：1~10000')
    count2 = IntegerField(u'点亮圣诞树所需人数', validators=[Required], description=u'商家提供给玩家的奖品数量，一棵点亮的圣诞树对应一个奖品，派发完即止，数值范围：1~10000')
    count3 = IntegerField(u'点灯成功率', validators=[Required], description=u'好友点灯的成功概率')
    finish = SubmitField(u'完成')