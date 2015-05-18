# coding=utf8
import unittest
from app import create_app, db
from app.models import Activity,Award,GameCase,GameProto,User,Player


class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_new_activity(self):
        proto_ff = GameProto(name='firefly', name_display=u'一起来抓萤火虫', desc={'rule': u'这是游戏规则', 'award': u'这是奖励信息'},
                             share_fmt={'title': u'这是微信分享title', 'desc': u'这是微信分享desc'})
        proto_cs = GameProto(name='catchstar', name_display=u'超模鉴定器', desc={'rule': u'这是游戏规则', 'award': u'这是奖励信息'},
                             share_fmt={'title': u'这是微信分享title', 'desc': u'这是微信分享desc'})
        proto_ff.save()
        proto_cs.save()
        self.assertEqual(len(GameProto.query.all()), 2)
        self.assertEqual(GameProto.query.all()[0].name, 'firefly')
        self.assertEqual(GameProto.query.all()[1].name, 'catchstar')

        user_a = User('corp-apple', 'apple@email.com', 'apple')
        user_b = User('corp-boy', 'boy@email.com', 'boy')
        user_a.save()
        user_b.save()
        self.assertEqual(len(User.query.all()), 2)
        self.assertEqual(User.query.all()[0].name, 'corp-apple')
        self.assertEqual(User.query.all()[1].name, 'corp-boy')

        case = GameCase(proto_ff)
        case.save()
        self.assertEqual(len(GameCase.query.all()), 1)

        items = [
            {'name': u'捕虫新手', 'value': 50},
            {'name': u'捕虫能手', 'value': 80},
            {'name': u'捕虫高手', 'value': 100}
        ]
        award = Award(award_type=2, items=items)
        award.save()
        self.assertEqual(len(Award.query.all()), 1)

        act = Activity(u'apple抓萤火虫活动', user_a, case, award)
        act.save()
        self.assertEqual(len(Activity.query.all()), 1)