# coding=utf8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DateTimeField, FileField, IntegerField, TextAreaField
from wtforms.validators import Required, Email, Length


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your email?', validators=[Required(), Email(), Length(1, 64)])
    submit = SubmitField('Submit')


class CreateActivityForm(Form):
    finish = SubmitField(u'完成')
    # 基本信息
    name = StringField(u'游戏名称', validators=[Required()], description=u'不能超过64个字')
    ts_start = DateTimeField(u'开始时间', validators=[Required], description=u'必填')
    ts_end = DateTimeField(u'结束时间', validators=[Required], description=u'必填，必须大于开始时间')
    rule = TextAreaField(u'活动规则', validators=[Required], description=u'不能超过300个字')
    subs_link = StringField(u'关注链接', validators=[Required],
                            description=u'请前往微信公众平台新建图文，将新建好的图文链接填入输入框即可实现一键关注')
    # 奖项设置
    prize1_name = StringField()
    prize1_item = StringField()
    prize1_count = IntegerField()

    prize2_name = StringField()
    prize2_item = StringField()
    prize2_count = IntegerField()

    prize3_name = StringField()
    prize3_item = StringField()
    prize3_count = IntegerField()

    prize4_name = StringField()
    prize4_item = StringField()
    prize4_count = IntegerField()

    prize5_name = StringField()
    prize5_item = StringField()
    prize5_count = IntegerField()

    prize6_name = StringField()
    prize6_item = StringField()
    prize6_count = IntegerField()

    # 素材定制
    img_demo = FileField(u'游戏素材图片demo')
    # 分享设置
    share_demo = StringField(u'分享类型')


class TestForm(Form):
    test_dtpicker = StringField(u"选择时间日期")