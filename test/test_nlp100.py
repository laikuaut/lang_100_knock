#!/usr/bin/env python
# config: utf-8

import unittest
from nlp100.Q000 import *
from nlp100.Q001 import *
from nlp100.Q002 import *
from nlp100.Q003 import *
from nlp100.Q004 import *
from nlp100.Q005 import *
from nlp100.Q006 import *
from nlp100.Q007 import *
from nlp100.Q008 import *
from nlp100.Q009 import *
from nlp100.Q010 import *

class Test_NLP_100(unittest.TestCase):

    def test_Q_000(self):
        self.assertEqual(Q_000(), 'desserts')

    def test_Q_001(self):
        self.assertEqual(Q_001(), 'パトカー')

    def test_Q_002(self):
        self.assertEqual(Q_002(), 'パタトクカシーー')

    def test_Q_003(self):
        self.assertEqual(Q_003(), \
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9])

    def test_Q_004(self):
        self.assertEqual(Q_004(), \
            {'H':1,'He':2,'Li':3,'Be':4,'B':5,'C':6,'N':7,
             'O':8,'F':9,'Ne':10,'Na':11,'Mi':12,'Al':13,
             'Si':14,'P':15,'S':16,'Cl':17,'Ar':18,'K':19,
             'Ca':20})

    def test_Q_005(self):
        self.assertEqual(Q_005_1(2), \
            ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er'])
        self.assertEqual(Q_005_2(2), \
            [['I', 'am'], ['am', 'an'], ['an', 'NLPer']])

    def test_Q_006(self):
        self.assertEqual(Q_006_1(), \
            {'ad', 'ag', 'ap', 'ar', 'di', 'gr', 'is', 'pa', 'ph', 'ra', 'se'})
        self.assertEqual(Q_006_2(), \
            {'ap', 'ar', 'pa', 'ra'})
        self.assertEqual(Q_006_3(), \
            {'ad', 'di', 'is', 'se'})
        self.assertTrue(Q_006_4())
        self.assertFalse(Q_006_5())
        self.assertEqual(Q_006_6(), \
            {'ad', 'ag', 'di', 'gr', 'is', 'ph', 'se'})

    def test_Q_007(self):
        self.assertEqual(Q_007(), '12時の気温は22.4')

    def test_Q_008(self):
        in_str     = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        encode_str = "Nld I mvvw z wirmp, zoxlslorx lu xlfihv, zugvi gsv svzeb ovxgfivh rmeloermt jfzmgfn nvxszmrxh."

        result = Q_008(in_str)
        # 暗号化確認
        self.assertEqual(result, encode_str)
        # 複合化確認
        self.assertEqual(Q_008(result), in_str)

    def test_Q_009(self):
        in_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        result = Q_009()
        in_word_list = in_str.split(' ')
        out_word_list = result.split(' ')
        for in_word, out_word in zip(in_word_list, out_word_list):
            # 文字数チェック
            self.assertEqual(len(in_word), len(out_word))
            # 利用している文字がすべて同じか
            self.assertEqual([c for c in sorted(in_word)], [c for c in sorted(out_word)])
            # 4文字以下と5文字以上の並べ替え確認
            if len(in_word) > 4:
                self.assertNotEqual(in_word, out_word)
            else:
                self.assertEqual(in_word, out_word)

    def test_Q_010(self):
        self.assertEqual(Q_010(), \
            ['24 data/hightemp.txt'])
        pass

    def test_Q_011(self):
        pass

    def test_Q_012(self):
        pass

    def test_Q_013(self):
        pass

    def test_Q_014(self):
        pass

    def test_Q_015(self):
        pass

    def test_Q_016(self):
        pass

    def test_Q_017(self):
        pass

    def test_Q_018(self):
        pass

    def test_Q_019(self):
        pass

    def test_Q_020(self):
        pass

    def test_Q_021(self):
        pass

    def test_Q_022(self):
        pass

    def test_Q_023(self):
        pass

    def test_Q_024(self):
        pass

    def test_Q_025(self):
        pass

    def test_Q_026(self):
        pass

    def test_Q_027(self):
        pass

    def test_Q_028(self):
        pass

    def test_Q_029(self):
        pass

    def test_Q_030(self):
        pass

    def test_Q_031(self):
        pass

    def test_Q_032(self):
        pass

    def test_Q_033(self):
        pass

    def test_Q_034(self):
        pass

    def test_Q_035(self):
        pass

    def test_Q_036(self):
        pass

    def test_Q_037(self):
        pass

    def test_Q_038(self):
        pass

    def test_Q_039(self):
        pass

    def test_Q_040(self):
        pass

    def test_Q_041(self):
        pass

    def test_Q_042(self):
        pass

    def test_Q_043(self):
        pass

    def test_Q_044(self):
        pass

    def test_Q_045(self):
        pass

    def test_Q_046(self):
        pass

    def test_Q_047(self):
        pass

    def test_Q_048(self):
        pass

    def test_Q_049(self):
        pass

    def test_Q_050(self):
        pass

    def test_Q_051(self):
        pass

    def test_Q_052(self):
        pass

    def test_Q_053(self):
        pass

    def test_Q_054(self):
        pass

    def test_Q_055(self):
        pass

    def test_Q_056(self):
        pass

    def test_Q_057(self):
        pass

    def test_Q_058(self):
        pass

    def test_Q_059(self):
        pass

    def test_Q_060(self):
        pass

    def test_Q_061(self):
        pass

    def test_Q_062(self):
        pass

    def test_Q_063(self):
        pass

    def test_Q_064(self):
        pass

    def test_Q_065(self):
        pass

    def test_Q_066(self):
        pass

    def test_Q_067(self):
        pass

    def test_Q_068(self):
        pass

    def test_Q_069(self):
        pass

    def test_Q_070(self):
        pass

    def test_Q_071(self):
        pass

    def test_Q_072(self):
        pass

    def test_Q_073(self):
        pass

    def test_Q_074(self):
        pass

    def test_Q_075(self):
        pass

    def test_Q_076(self):
        pass

    def test_Q_077(self):
        pass

    def test_Q_078(self):
        pass

    def test_Q_079(self):
        pass

    def test_Q_080(self):
        pass

    def test_Q_081(self):
        pass

    def test_Q_082(self):
        pass

    def test_Q_083(self):
        pass

    def test_Q_084(self):
        pass

    def test_Q_085(self):
        pass

    def test_Q_086(self):
        pass

    def test_Q_087(self):
        pass

    def test_Q_088(self):
        pass

    def test_Q_089(self):
        pass

    def test_Q_090(self):
        pass

    def test_Q_091(self):
        pass

    def test_Q_092(self):
        pass

    def test_Q_093(self):
        pass

    def test_Q_094(self):
        pass

    def test_Q_095(self):
        pass

    def test_Q_096(self):
        pass

    def test_Q_097(self):
        pass

    def test_Q_098(self):
        pass

    def test_Q_099(self):
        pass

if __name__ == '__main__':
    unittest.main()
