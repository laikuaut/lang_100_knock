#!/usr/bin/env python
# coding: utf-8

import unittest
import glob
from util import util
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
from nlp100.Q011 import *
from nlp100.Q012 import *
from nlp100.Q013 import *
from nlp100.Q014 import *
from nlp100.Q015 import *
from nlp100.Q016 import *
from nlp100.Q017 import *
from nlp100.Q018 import *
from nlp100.Q019 import *
from nlp100.Q020 import *
from nlp100.Q021 import *
from nlp100.Q022 import *
from nlp100.Q023 import *
from nlp100.Q024 import *
from nlp100.Q025 import *
from nlp100.Q026 import *
from nlp100.Q027 import *

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
        self.assertEqual(Q_010_1(), 24)
        self.assertEqual(Q_010_2(), \
            ['24 data/hightemp.txt'])

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

    def test_Q_020(self):
        util.exe_cmd('rm data/Britain.txt')
        Q_020()

        with open('data/Britain.txt', 'r') as result_f, \
             open('test/data/Britain.json', 'r') as current_f:
            current_data = json.loads(current_f.readline())
            result = result_f.read().rstrip()
            self.assertEqual(result, current_data['text'])

    def test_Q_021(self):
        current = ['[[Category:イギリス|*]]',
                '[[Category:英連邦王国|*]]',
                '[[Category:G8加盟国]]',
                '[[Category:欧州連合加盟国]]',
                '[[Category:海洋国家]]',
                '[[Category:君主国]]',
                '[[Category:島国|くれいとふりてん]]',
                '[[Category:1801年に設立された州・地域]]']
        result = Q_021()
        self.assertEqual(result, current)

    def test_Q_022(self):
        current = [
            'イギリス|*',
            '英連邦王国|*',
            'G8加盟国',
            '欧州連合加盟国',
            '海洋国家',
            '君主国',
            '島国|くれいとふりてん',
            '1801年に設立された州・地域']
        self.assertEqual(Q_022(), current)

    def test_Q_023(self):
        current = [('国名',1),
                ('歴史',1),
                ('地理',1),
                ('気候',2),
                ('政治',1),
                ('外交と軍事',1),
                ('地方行政区分',1),
                ('主要都市',2),
                ('科学技術',1),
                ('経済',1),
                ('鉱業',2),
                ('農業',2),
                ('貿易',2),
                ('通貨',2),
                ('企業',2),
                ('交通',1),
                ('道路',2),
                ('鉄道',2),
                ('海運',2),
                ('航空',2),
                ('通信',1),
                ('国民',1),
                ('言語',2),
                ('宗教',2),
                (' 婚姻 ',2),
                ('教育',2),
                ('文化',1),
                ('食文化',2),
                ('文学',2),
                (' 哲学 ',2),
                ('音楽',2),
                ('イギリスのポピュラー音楽',3),
                ('映画',2),
                ('コメディ',2),
                ('国花',2),
                ('世界遺産',2),
                ('祝祭日',2),
                ('スポーツ',1),
                ('サッカー',2),
                ('競馬',2),
                ('モータースポーツ',2),
                ('脚注',1),
                ('関連項目',1),
                ('外部リンク',1)]
        self.assertEqual(Q_023(), current)

    def test_Q_024(self):
        current = [
                "Royal Coat of Arms of the United Kingdom.svg",
                "Battle of Waterloo 1815.PNG",
                "The British Empire.png",
                "Uk topo en.jpg",
                "BenNevis2005.jpg",
                "Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg",
                "Palace of Westminster, London - Feb 2007.jpg",
                "David Cameron and Barack Obama at the G20 Summit in Toronto.jpg",
                "Soldiers Trooping the Colour, 16th June 2007.jpg",
                "Scotland Parliament Holyrood.jpg",
                "London.bankofengland.arp.jpg",
                "City of London skyline from London City Hall - Oct 2008.jpg",
                "Oil platform in the North SeaPros.jpg",
                "Eurostar at St Pancras Jan 2008.jpg",
                "Heathrow T5.jpg",
                "Anglospeak.svg",
                "CHANDOS3.jpg",
                "The Fabs.JPG",
                "Wembley Stadium, illuminated.jpg"
                ]
        self.assertEqual(Q_024(), current)

    def test_Q_025(self):
        current = {
            '略名' : 'イギリス',
            '日本語国名' : 'グレートブリテン及び北アイルランド連合王国',
            '公式国名' : '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>' \
                '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>' \
                '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>' \
                '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>' \
                '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>' \
                '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>' \
                '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>',
            '国旗画像' : 'Flag of the United Kingdom.svg',
            '国章画像' : '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
            '国章リンク' : '（[[イギリスの国章|国章]]）',
            '標語' : '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）',
            '国歌' : '[[女王陛下万歳|神よ女王陛下を守り給え]]',
            '位置画像' : 'Location_UK_EU_Europe_001.svg',
            '公用語' : '[[英語]]（事実上）',
            '首都' : '[[ロンドン]]',
            '最大都市' : 'ロンドン',
            '元首等肩書' : '[[イギリスの君主|女王]]',
            '元首等氏名' : '[[エリザベス2世]]',
            '首相等肩書' : '[[イギリスの首相|首相]]',
            '首相等氏名' : '[[デーヴィッド・キャメロン]]',
            '面積順位' : '76',
            '面積大きさ' : '1 E11',
            '面積値' : '244,820',
            '水面積率' : '1.3%',
            '人口統計年' : '2011',
            '人口順位' : '22',
            '人口大きさ' : '1 E7',
            '人口値' : '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>',
            '人口密度値' : '246',
            'GDP統計年元' : '2012',
            'GDP値元' : '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>',
            'GDP統計年MER' : '2012',
            'GDP順位MER' : '5',
            'GDP値MER' : '2兆4337億<ref name="imf-statistics-gdp" />',
            'GDP統計年' : '2012',
            'GDP順位' : '6',
            'GDP値' : '2兆3162億<ref name="imf-statistics-gdp" />',
            'GDP/人' : '36,727<ref name="imf-statistics-gdp" />',
            '建国形態' : '建国',
            '確立形態1' : '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）',
            '確立年月日1' : '[[927年]]／[[843年]]',
            '確立形態2' : '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）',
            '確立年月日2' : '[[1707年]]',
            '確立形態3' : '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）',
            '確立年月日3' : '[[1801年]]',
            '確立形態4' : "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更",
            '確立年月日4' : '[[1927年]]',
            '通貨' : '[[スターリング・ポンド|UKポンド]] (&pound;)',
            '通貨コード' : 'GBP',
            '時間帯' : '±0',
            '夏時間' : '+1',
            'ISO 3166-1' : 'GB / GBR',
            'ccTLD' : '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>',
            '国際電話番号' : '44',
            '注記' : '<references />'
            }
        result = Q_025()
        for key in result.keys():
            self.assertEqual(result[key], current[key])

    def test_Q_026(self):
        current = {
            '略名' : 'イギリス',
            '日本語国名' : 'グレートブリテン及び北アイルランド連合王国',
            '公式国名' : '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>' \
                '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>' \
                '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>' \
                '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>' \
                '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>' \
                '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>' \
                '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>',
            '国旗画像' : 'Flag of the United Kingdom.svg',
            '国章画像' : '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
            '国章リンク' : '（[[イギリスの国章|国章]]）',
            '標語' : '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）',
            '国歌' : '[[女王陛下万歳|神よ女王陛下を守り給え]]',
            '位置画像' : 'Location_UK_EU_Europe_001.svg',
            '公用語' : '[[英語]]（事実上）',
            '首都' : '[[ロンドン]]',
            '最大都市' : 'ロンドン',
            '元首等肩書' : '[[イギリスの君主|女王]]',
            '元首等氏名' : '[[エリザベス2世]]',
            '首相等肩書' : '[[イギリスの首相|首相]]',
            '首相等氏名' : '[[デーヴィッド・キャメロン]]',
            '面積順位' : '76',
            '面積大きさ' : '1 E11',
            '面積値' : '244,820',
            '水面積率' : '1.3%',
            '人口統計年' : '2011',
            '人口順位' : '22',
            '人口大きさ' : '1 E7',
            '人口値' : '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>',
            '人口密度値' : '246',
            'GDP統計年元' : '2012',
            'GDP値元' : '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>',
            'GDP統計年MER' : '2012',
            'GDP順位MER' : '5',
            'GDP値MER' : '2兆4337億<ref name="imf-statistics-gdp" />',
            'GDP統計年' : '2012',
            'GDP順位' : '6',
            'GDP値' : '2兆3162億<ref name="imf-statistics-gdp" />',
            'GDP/人' : '36,727<ref name="imf-statistics-gdp" />',
            '建国形態' : '建国',
            '確立形態1' : '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）',
            '確立年月日1' : '[[927年]]／[[843年]]',
            '確立形態2' : '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）',
            '確立年月日2' : '[[1707年]]',
            '確立形態3' : '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）',
            '確立年月日3' : '[[1801年]]',
            '確立形態4' : "現在の国号「グレートブリテン及び北アイルランド連合王国」に変更",
            '確立年月日4' : '[[1927年]]',
            '通貨' : '[[スターリング・ポンド|UKポンド]] (&pound;)',
            '通貨コード' : 'GBP',
            '時間帯' : '±0',
            '夏時間' : '+1',
            'ISO 3166-1' : 'GB / GBR',
            'ccTLD' : '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>',
            '国際電話番号' : '44',
            '注記' : '<references />'
            }
        result = Q_026()
        for key in result.keys():
            self.assertEqual(result[key], current[key])

    def test_Q_027(self):
        current = {
            '略名' : 'イギリス',
            '日本語国名' : 'グレートブリテン及び北アイルランド連合王国',
            '公式国名' : '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>' \
                '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（スコットランド・ゲール語）<br/>' \
                '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（ウェールズ語）<br/>' \
                '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（アイルランド語）<br/>' \
                '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（コーンウォール語）<br/>' \
                '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（スコットランド語）<br/>' \
                '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>',
            '国旗画像' : 'Flag of the United Kingdom.svg',
            '国章画像' : '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
            '国章リンク' : '（国章）',
            '標語' : '{{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）',
            '国歌' : '神よ女王陛下を守り給え',
            '位置画像' : 'Location_UK_EU_Europe_001.svg',
            '公用語' : '英語（事実上）',
            '首都' : 'ロンドン',
            '最大都市' : 'ロンドン',
            '元首等肩書' : '女王',
            '元首等氏名' : 'エリザベス2世',
            '首相等肩書' : '首相',
            '首相等氏名' : 'デーヴィッド・キャメロン',
            '面積順位' : '76',
            '面積大きさ' : '1 E11',
            '面積値' : '244,820',
            '水面積率' : '1.3%',
            '人口統計年' : '2011',
            '人口順位' : '22',
            '人口大きさ' : '1 E7',
            '人口値' : '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>',
            '人口密度値' : '246',
            'GDP統計年元' : '2012',
            'GDP値元' : '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>',
            'GDP統計年MER' : '2012',
            'GDP順位MER' : '5',
            'GDP値MER' : '2兆4337億<ref name="imf-statistics-gdp" />',
            'GDP統計年' : '2012',
            'GDP順位' : '6',
            'GDP値' : '2兆3162億<ref name="imf-statistics-gdp" />',
            'GDP/人' : '36,727<ref name="imf-statistics-gdp" />',
            '建国形態' : '建国',
            '確立形態1' : 'イングランド王国／スコットランド王国<br />（両国とも1707年連合法まで）',
            '確立年月日1' : '927年／843年',
            '確立形態2' : 'グレートブリテン王国建国<br />（1707年連合法）',
            '確立年月日2' : '1707年',
            '確立形態3' : 'グレートブリテン及びアイルランド連合王国建国<br />（1800年連合法）',
            '確立年月日3' : '1801年',
            '確立形態4' : "現在の国号「グレートブリテン及び北アイルランド連合王国」に変更",
            '確立年月日4' : '1927年',
            '通貨' : 'UKポンド (&pound;)',
            '通貨コード' : 'GBP',
            '時間帯' : '±0',
            '夏時間' : '+1',
            'ISO 3166-1' : 'GB / GBR',
            'ccTLD' : '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>',
            '国際電話番号' : '44',
            '注記' : '<references />'
            }
        result = Q_027()
        for key in result.keys():
            self.assertEqual(result[key], current[key])

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
