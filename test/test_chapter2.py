#!/usr/bin/env python
# coding: utf-8

import unittest
import glob
from util import util
from nlp100.chapter2.Q010 import *
from nlp100.chapter2.Q011 import *
from nlp100.chapter2.Q012 import *
from nlp100.chapter2.Q013 import *
from nlp100.chapter2.Q014 import *
from nlp100.chapter2.Q015 import *
from nlp100.chapter2.Q016 import *
from nlp100.chapter2.Q017 import *
from nlp100.chapter2.Q018 import *
from nlp100.chapter2.Q019 import *

class Test_Chapter2(unittest.TestCase):

    def test_Q_010(self):
        self.assertEqual(Q_010_1(), 24)
        self.assertEqual(Q_010_2(), ["24"])

    def test_Q_011(self):
        current = ['高知県 江川崎 41 2013-08-12',
            '埼玉県 熊谷 40.9 2007-08-16',
            '岐阜県 多治見 40.9 2007-08-16',
            '山形県 山形 40.8 1933-07-25',
            '山梨県 甲府 40.7 2013-08-10',
            '和歌山県 かつらぎ 40.6 1994-08-08',
            '静岡県 天竜 40.6 1994-08-04',
            '山梨県 勝沼 40.5 2013-08-10',
            '埼玉県 越谷 40.4 2007-08-16',
            '群馬県 館林 40.3 2007-08-16',
            '群馬県 上里見 40.3 1998-07-04',
            '愛知県 愛西 40.3 1994-08-05',
            '千葉県 牛久 40.2 2004-07-20',
            '静岡県 佐久間 40.2 2001-07-24',
            '愛媛県 宇和島 40.2 1927-07-22',
            '山形県 酒田 40.1 1978-08-03',
            '岐阜県 美濃 40 2007-08-16',
            '群馬県 前橋 40 2001-07-24',
            '千葉県 茂原 39.9 2013-08-11',
            '埼玉県 鳩山 39.9 1997-07-05',
            '大阪府 豊中 39.9 1994-08-08',
            '山梨県 大月 39.9 1990-07-19',
            '山形県 鶴岡 39.9 1978-08-03',
            '愛知県 名古屋 39.9 1942-08-02']
        self.assertEqual(Q_011_0(), current)
        self.assertEqual(Q_011_1(), current)
        self.assertEqual(Q_011_2(), current)
        self.assertEqual(Q_011_3(), current)

    def test_Q_012(self):
        correct1 = ['高知県','埼玉県','岐阜県','山形県','山梨県','和歌山県','静岡県','山梨県','埼玉県','群馬県','群馬県','愛知県','千葉県','静岡県','愛媛県','山形県','岐阜県','群馬県','千葉県','埼玉県','大阪府','山梨県','山形県','愛知県']
        correct2 = ['江川崎', '熊谷', '多治見', '山形', '甲府', 'かつらぎ', '天竜', '勝沼', '越谷', '館林', '上里見', '愛西', '牛久', '佐久間', '宇和島', '酒田', '美濃', '前橋', '茂原', '鳩山', '豊中', '大月', '鶴岡', '名古屋']

        for _ in util.exe_cmd('rm data/col1.txt -f'): pass
        for _ in util.exe_cmd('rm data/col2.txt -f'): pass
        Q_012_1()
        result1 = []
        result2 = []
        with open('data/col1.txt', 'tr', encoding='utf-8') as col1:
            result1 = [line.strip() for line in col1]
        with open('data/col2.txt', 'tr', encoding='utf-8') as col2:
            result2 = [line.strip() for line in col2]
        self.assertEqual(result1, correct1)
        self.assertEqual(result2, correct2)

        for _ in util.exe_cmd('rm data/col1.txt -f'): pass
        for _ in util.exe_cmd('rm data/col2.txt -f'): pass
        Q_012_2()
        result1 = []
        result2 = []
        with open('data/col1.txt', 'tr', encoding='utf-8') as col1:
            result1 = [line.strip() for line in col1]
        with open('data/col2.txt', 'tr', encoding='utf-8') as col2:
            result2 = [line.strip() for line in col2]
        self.assertEqual(result1, correct1)
        self.assertEqual(result2, correct2)

    def test_Q_013(self):
        correct1 = ['高知県','埼玉県','岐阜県','山形県','山梨県','和歌山県','静岡県','山梨県','埼玉県','群馬県','群馬県','愛知県','千葉県','静岡県','愛媛県','山形県','岐阜県','群馬県','千葉県','埼玉県','大阪府','山梨県','山形県','愛知県']
        correct2 = ['江川崎', '熊谷', '多治見', '山形', '甲府', 'かつらぎ', '天竜', '勝沼', '越谷', '館林', '上里見', '愛西', '牛久', '佐久間', '宇和島', '酒田', '美濃', '前橋', '茂原', '鳩山', '豊中', '大月', '鶴岡', '名古屋']
        correct = ['{0}\t{1}'.format(c1, c2) for c1, c2 in zip(correct1, correct2)]

        for _ in util.exe_cmd('rm data/col_merge.txt -f'): pass
        Q_013_1()
        with open('data/col_merge.txt', 'tr', encoding='utf-8') as col:
            result = [line.strip() for line in col]
        self.assertEqual(result, correct)

        for _ in util.exe_cmd('rm data/col_merge.txt -f'): pass
        Q_013_2()
        with open('data/col_merge.txt', 'tr', encoding='utf-8') as col:
            result = [line.strip() for line in col]
        self.assertEqual(result, correct)

    def test_Q_014(self):
        current = ['高知県	江川崎	41	2013-08-12',
            '埼玉県	熊谷	40.9	2007-08-16',
            '岐阜県	多治見	40.9	2007-08-16',
            '山形県	山形	40.8	1933-07-25',
            '山梨県	甲府	40.7	2013-08-10',
            '和歌山県	かつらぎ	40.6	1994-08-08',
            '静岡県	天竜	40.6	1994-08-04',
            '山梨県	勝沼	40.5	2013-08-10',
            '埼玉県	越谷	40.4	2007-08-16',
            '群馬県	館林	40.3	2007-08-16']
        self.assertEqual(Q_014_1(10), current)
        self.assertEqual(Q_014_2(10), current)

    def test_Q_015(self):
        current = ['愛媛県	宇和島	40.2	1927-07-22',
            '山形県	酒田	40.1	1978-08-03',
            '岐阜県	美濃	40	2007-08-16',
            '群馬県	前橋	40	2001-07-24',
            '千葉県	茂原	39.9	2013-08-11',
            '埼玉県	鳩山	39.9	1997-07-05',
            '大阪府	豊中	39.9	1994-08-08',
            '山梨県	大月	39.9	1990-07-19',
            '山形県	鶴岡	39.9	1978-08-03',
            '愛知県	名古屋	39.9	1942-08-02']
        self.assertEqual(Q_015_2(10), current)
        self.assertEqual(Q_015_1(10), current)

    def test_Q_016(self):
        current = [
            ['高知県	江川崎	41	2013-08-12',
            '埼玉県	熊谷	40.9	2007-08-16',
            '岐阜県	多治見	40.9	2007-08-16',
            '山形県	山形	40.8	1933-07-25',
            '山梨県	甲府	40.7	2013-08-10'],
            ['和歌山県	かつらぎ	40.6	1994-08-08',
            '静岡県	天竜	40.6	1994-08-04',
            '山梨県	勝沼	40.5	2013-08-10',
            '埼玉県	越谷	40.4	2007-08-16',
            '群馬県	館林	40.3	2007-08-16'],
            ['群馬県	上里見	40.3	1998-07-04',
            '愛知県	愛西	40.3	1994-08-05',
            '千葉県	牛久	40.2	2004-07-20',
            '静岡県	佐久間	40.2	2001-07-24',
            '愛媛県	宇和島	40.2	1927-07-22'],
            ['山形県	酒田	40.1	1978-08-03',
            '岐阜県	美濃	40	2007-08-16',
            '群馬県	前橋	40	2001-07-24',
            '千葉県	茂原	39.9	2013-08-11',
            '埼玉県	鳩山	39.9	1997-07-05'],
            ['大阪府	豊中	39.9	1994-08-08',
            '山梨県	大月	39.9	1990-07-19',
            '山形県	鶴岡	39.9	1978-08-03',
            '愛知県	名古屋	39.9	1942-08-02']]
        self.assertEqual(Q_016_1(5), current)

        util.exe_cmd('rm -rf data/splitted')

        Q_016_2(5)
        result = []
        for path in glob.glob('data/splitted/hightemp.txt.*'):
            result.append(list(util.exe_cmd('cat {}'.format(path))))
        self.assertEqual(result, current)

    def test_Q_017(self):
        current = {
            '愛知県',
            '愛媛県',
            '岐阜県',
            '群馬県',
            '高知県',
            '埼玉県',
            '山形県',
            '山梨県',
            '静岡県',
            '千葉県',
            '大阪府',
            '和歌山県'
            }
        self.assertEqual(Q_017_1(), current)
        self.assertEqual(Q_017_2(), current)

    def test_Q_018(self):
        current = ['高知県	江川崎	41	2013-08-12',
            '埼玉県	熊谷	40.9	2007-08-16',
            '岐阜県	多治見	40.9	2007-08-16',
            '山形県	山形	40.8	1933-07-25',
            '山梨県	甲府	40.7	2013-08-10',
            '和歌山県	かつらぎ	40.6	1994-08-08',
            '静岡県	天竜	40.6	1994-08-04',
            '山梨県	勝沼	40.5	2013-08-10',
            '埼玉県	越谷	40.4	2007-08-16',
            '群馬県	館林	40.3	2007-08-16',
            '群馬県	上里見	40.3	1998-07-04',
            '愛知県	愛西	40.3	1994-08-05',
            '千葉県	牛久	40.2	2004-07-20',
            '静岡県	佐久間	40.2	2001-07-24',
            '愛媛県	宇和島	40.2	1927-07-22',
            '山形県	酒田	40.1	1978-08-03',
            '岐阜県	美濃	40	2007-08-16',
            '群馬県	前橋	40	2001-07-24',
            '千葉県	茂原	39.9	2013-08-11',
            '埼玉県	鳩山	39.9	1997-07-05',
            '大阪府	豊中	39.9	1994-08-08',
            '山梨県	大月	39.9	1990-07-19',
            '山形県	鶴岡	39.9	1978-08-03',
            '愛知県	名古屋	39.9	1942-08-02']
        self.assertEqual(Q_018_1(), current)
        self.assertEqual(Q_018_2(), current)

    def test_Q_019(self):
        current = [
            ('埼玉県', '3'),
            ('山形県', '3'),
            ('山梨県', '3'),
            ('群馬県', '3'),
            ('静岡県', '2'),
            ('千葉県', '2'),
            ('愛知県', '2'),
            ('岐阜県', '2'),
            ('愛媛県', '1'),
            ('高知県', '1'),
            ('大阪府', '1'),
            ('和歌山県', '1')]

        result1 = Q_019_1()
        result2 = Q_019_2()
        # 出力順が出現頻度順になっているかを確認(要素の出現順は比較しない)
        for c, r in zip(current, result1):
            self.assertEqual(r[1], c[1])
        for c, r in zip(current, result2):
            self.assertEqual(r[1], c[1])

        # 出現頻度の最大値と最小値を算出
        max_num = max([int(col[1]) for col in current])
        min_num = min([int(col[1]) for col in current])

        # 出現頻度ごとの要素内容が同じであることを確認
        for i in range(min_num, max_num+1):
            self.assertEqual(
                    {col[0] for col in result1 if col[1] == i},
                    {col[0] for col in current if col[1] == i}
                )
            self.assertEqual(
                    {col[0] for col in result2 if col[1] == i},
                    {col[0] for col in current if col[1] == i}
                )

if __name__ == '__main__':
    unittest.main()
