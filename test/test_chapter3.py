#!/usr/bin/env python
# coding: utf-8

import unittest
import glob
from util import util
from nlp100.chapter3.Q020 import *
from nlp100.chapter3.Q021 import *
from nlp100.chapter3.Q022 import *
from nlp100.chapter3.Q023 import *
from nlp100.chapter3.Q024 import *
from nlp100.chapter3.Q025 import *
from nlp100.chapter3.Q026 import *
from nlp100.chapter3.Q027 import *

class Test_Chapter3(unittest.TestCase):

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
            '略名' : 'イギリス\n',
            '日本語国名' : 'グレートブリテン及び北アイルランド連合王国\n',
            '公式国名' : '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>\n' \
                '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>\n' \
                '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>\n' \
                '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>\n' \
                '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>\n' \
                '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>\n' \
                '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>\n',
            '国旗画像' : 'Flag of the United Kingdom.svg\n',
            '国章画像' : '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]\n',
            '国章リンク' : '（[[イギリスの国章|国章]]）\n',
            '標語' : '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）\n',
            '国歌' : '[[女王陛下万歳|神よ女王陛下を守り給え]]\n',
            '位置画像' : 'Location_UK_EU_Europe_001.svg\n',
            '公用語' : '[[英語]]（事実上）\n',
            '首都' : '[[ロンドン]]\n',
            '最大都市' : 'ロンドン\n',
            '元首等肩書' : '[[イギリスの君主|女王]]\n',
            '元首等氏名' : '[[エリザベス2世]]\n',
            '首相等肩書' : '[[イギリスの首相|首相]]\n',
            '首相等氏名' : '[[デーヴィッド・キャメロン]]\n',
            '面積順位' : '76\n',
            '面積大きさ' : '1 E11\n',
            '面積値' : '244,820\n',
            '水面積率' : '1.3%\n',
            '人口統計年' : '2011\n',
            '人口順位' : '22\n',
            '人口大きさ' : '1 E7\n',
            '人口値' : '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>\n',
            '人口密度値' : '246\n',
            'GDP統計年元' : '2012\n',
            'GDP値元' : '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>\n',
            'GDP統計年MER' : '2012\n',
            'GDP順位MER' : '5\n',
            'GDP値MER' : '2兆4337億<ref name="imf-statistics-gdp" />\n',
            'GDP統計年' : '2012\n',
            'GDP順位' : '6\n',
            'GDP値' : '2兆3162億<ref name="imf-statistics-gdp" />\n',
            'GDP/人' : '36,727<ref name="imf-statistics-gdp" />\n',
            '建国形態' : '建国\n',
            '確立形態1' : '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）\n',
            '確立年月日1' : '[[927年]]／[[843年]]\n',
            '確立形態2' : '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）\n',
            '確立年月日2' : '[[1707年]]\n',
            '確立形態3' : '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）\n',
            '確立年月日3' : '[[1801年]]\n',
            '確立形態4' : "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更\n",
            '確立年月日4' : '[[1927年]]\n',
            '通貨' : '[[スターリング・ポンド|UKポンド]] (&pound;)\n',
            '通貨コード' : 'GBP\n',
            '時間帯' : '±0\n',
            '夏時間' : '+1\n',
            'ISO 3166-1' : 'GB / GBR\n',
            'ccTLD' : '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>\n',
            '国際電話番号' : '44\n',
            '注記' : '<references />\n'
            }
        result = Q_025()
        for key in result.keys():
            self.assertEqual(result[key], current[key])

    def test_Q_026(self):
        current = {
            '略名' : 'イギリス\n',
            '日本語国名' : 'グレートブリテン及び北アイルランド連合王国\n',
            '公式国名' : '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>\n' \
                '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>\n' \
                '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>\n' \
                '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>\n' \
                '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>\n' \
                '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>\n' \
                '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>\n',
            '国旗画像' : 'Flag of the United Kingdom.svg\n',
            '国章画像' : '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]\n',
            '国章リンク' : '（[[イギリスの国章|国章]]）\n',
            '標語' : '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）\n',
            '国歌' : '[[女王陛下万歳|神よ女王陛下を守り給え]]\n',
            '位置画像' : 'Location_UK_EU_Europe_001.svg\n',
            '公用語' : '[[英語]]（事実上）\n',
            '首都' : '[[ロンドン]]\n',
            '最大都市' : 'ロンドン\n',
            '元首等肩書' : '[[イギリスの君主|女王]]\n',
            '元首等氏名' : '[[エリザベス2世]]\n',
            '首相等肩書' : '[[イギリスの首相|首相]]\n',
            '首相等氏名' : '[[デーヴィッド・キャメロン]]\n',
            '面積順位' : '76\n',
            '面積大きさ' : '1 E11\n',
            '面積値' : '244,820\n',
            '水面積率' : '1.3%\n',
            '人口統計年' : '2011\n',
            '人口順位' : '22\n',
            '人口大きさ' : '1 E7\n',
            '人口値' : '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>\n',
            '人口密度値' : '246\n',
            'GDP統計年元' : '2012\n',
            'GDP値元' : '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>\n',
            'GDP統計年MER' : '2012\n',
            'GDP順位MER' : '5\n',
            'GDP値MER' : '2兆4337億<ref name="imf-statistics-gdp" />\n',
            'GDP統計年' : '2012\n',
            'GDP順位' : '6\n',
            'GDP値' : '2兆3162億<ref name="imf-statistics-gdp" />\n',
            'GDP/人' : '36,727<ref name="imf-statistics-gdp" />\n',
            '建国形態' : '建国\n',
            '確立形態1' : '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）\n',
            '確立年月日1' : '[[927年]]／[[843年]]\n',
            '確立形態2' : '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）\n',
            '確立年月日2' : '[[1707年]]\n',
            '確立形態3' : '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）\n',
            '確立年月日3' : '[[1801年]]\n',
            '確立形態4' : '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更\n',
            '確立年月日4' : '[[1927年]]\n',
            '通貨' : '[[スターリング・ポンド|UKポンド]] (&pound;)\n',
            '通貨コード' : 'GBP\n',
            '時間帯' : '±0\n',
            '夏時間' : '+1\n',
            'ISO 3166-1' : 'GB / GBR\n',
            'ccTLD' : '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>\n',
            '国際電話番号' : '44\n',
            '注記' : '<references />\n'
            }
        result = Q_026()
        for key in result.keys():
            self.assertEqual(result[key], current[key])

    def test_Q_027(self):
        current = {
            '略名' : 'イギリス\n',
            '日本語国名' : 'グレートブリテン及び北アイルランド連合王国\n',
            '公式国名' : '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>\n' \
                '*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（スコットランド・ゲール語）<br/>\n' \
                '*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（ウェールズ語）<br/>\n' \
                '*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（アイルランド語）<br/>\n' \
                '*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（コーンウォール語）<br/>\n' \
                '*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（スコットランド語）<br/>\n' \
                '**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>\n',
            '国旗画像' : 'Flag of the United Kingdom.svg\n',
            '国章画像' : '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]\n',
            '国章リンク' : '（国章）\n',
            '標語' : '{{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）\n',
            '国歌' : '神よ女王陛下を守り給え\n',
            '位置画像' : 'Location_UK_EU_Europe_001.svg\n',
            '公用語' : '英語（事実上）\n',
            '首都' : 'ロンドン\n',
            '最大都市' : 'ロンドン\n',
            '元首等肩書' : '女王\n',
            '元首等氏名' : 'エリザベス2世\n',
            '首相等肩書' : '首相\n',
            '首相等氏名' : 'デーヴィッド・キャメロン\n',
            '面積順位' : '76\n',
            '面積大きさ' : '1 E11\n',
            '面積値' : '244,820\n',
            '水面積率' : '1.3%\n',
            '人口統計年' : '2011\n',
            '人口順位' : '22\n',
            '人口大きさ' : '1 E7\n',
            '人口値' : '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>\n',
            '人口密度値' : '246\n',
            'GDP統計年元' : '2012\n',
            'GDP値元' : '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>\n',
            'GDP統計年MER' : '2012\n',
            'GDP順位MER' : '5\n',
            'GDP値MER' : '2兆4337億<ref name="imf-statistics-gdp" />\n',
            'GDP統計年' : '2012\n',
            'GDP順位' : '6\n',
            'GDP値' : '2兆3162億<ref name="imf-statistics-gdp" />\n',
            'GDP/人' : '36,727<ref name="imf-statistics-gdp" />\n',
            '建国形態' : '建国\n',
            '確立形態1' : 'イングランド王国／スコットランド王国<br />（両国とも1707年連合法まで）\n',
            '確立年月日1' : '927年／843年\n',
            '確立形態2' : 'グレートブリテン王国建国<br />（1707年連合法）\n',
            '確立年月日2' : '1707年\n',
            '確立形態3' : 'グレートブリテン及びアイルランド連合王国建国<br />（1800年連合法）\n',
            '確立年月日3' : '1801年\n',
            '確立形態4' : '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更\n',
            '確立年月日4' : '1927年\n',
            '通貨' : 'UKポンド (&pound;)\n',
            '通貨コード' : 'GBP\n',
            '時間帯' : '±0\n',
            '夏時間' : '+1\n',
            'ISO 3166-1' : 'GB / GBR\n',
            'ccTLD' : '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>\n',
            '国際電話番号' : '44\n',
            '注記' : '<references />\n'
            }
        result = Q_027()
        for key in result.keys():
            self.assertEqual(result[key], current[key])

    def test_Q_028(self):
        pass

    def test_Q_029(self):
        pass

if __name__ == '__main__':
    unittest.main()
