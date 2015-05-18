# encoding = utf-8
from flask import Markup,redirect,request,jsonify,Blueprint
from weixin.client import WeixinMpAPI
from weixin.oauth2 import OAuth2AuthExchangeError

wx = Blueprint('wx', __name__)

APP_ID = 'wx110f2e8007007ceb'
APP_SECRET = '3fea78a7acabc2dc1e9ea546f4438b31'
REDIRECT_URI = 'http://wx4399.com/authorization'


@wx.route("/authorization")
def authorization():
    code = request.args.get('code')
    api = WeixinMpAPI(appid=APP_ID,
                    app_secret=APP_SECRET,
                    redirect_uri=REDIRECT_URI)
    auth_info = api.exchange_code_for_access_token(code=code)
    api = WeixinMpAPI(access_token=auth_info['access_token'])
    resp = api.user(openid=auth_info['openid'])
    return jsonify(resp)


@wx.route("/login")
def login():
    api = WeixinMpAPI(appid=APP_ID,
                    app_secret=APP_SECRET,
                    redirect_uri=REDIRECT_URI)
    redirect_uri = api.get_authorize_login_url(scope=("snsapi_userinfo",))
    return redirect(redirect_uri)


@wx.route("/")
def hello():
    return Markup('<a href="%s">weixin login!</a>') % '/login'

