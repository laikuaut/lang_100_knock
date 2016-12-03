#!/usr/bin/env python
# coding: utf-8

import unittest
import glob
from util import util
from nlp100.chapter1.Q000 import *
from nlp100.chapter1.Q001 import *
from nlp100.chapter1.Q002 import *
from nlp100.chapter1.Q003 import *
from nlp100.chapter1.Q004 import *
from nlp100.chapter1.Q005 import *
from nlp100.chapter1.Q006 import *
from nlp100.chapter1.Q007 import *
from nlp100.chapter1.Q008 import *
from nlp100.chapter1.Q009 import *

class Test_Chapter1(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
