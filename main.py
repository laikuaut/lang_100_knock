#!/usr/bin/env python
# config: utf-8

import re

class NLP_100():

    @classmethod
    def Q_000(cls):
        """ 00. 文字列の逆順
        文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
        """
        # 入力文字
        input_str = 'stressed'
        # 逆順
        return input_str[::-1]

    @classmethod
    def Q_001(cls):
        """ 01. 「パタトクカシーー」
        「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
        """

        # 入力文字
        input_str = 'パタトクカシーー'
        # 文字列の1,3,5,7文字目を取得
        return input_str[0::2]

    @classmethod
    def Q_002(cls):
        """ 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
        「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
        """

        # 文字列
        str1 = 'パトカー'
        str2 = 'タクシー'

        # 交互に連結
        result = ''
        for char1, char2 in zip(str1, str2):
            result += char1 + char2

        return result

    @classmethod
    def Q_003(cls):
        """ 03. 円周率
        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
        """

        # 単語の文字数が円周率=3.14159265358979になっている
        input_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        word_list = re.split(r'\W+', input_str)
        return [len(word) for word in word_list if len(word) > 0]

    @classmethod
    def Q_004(cls):
        """ 04. 元素記号
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
        取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
        """

        # 結果がkey=元素記号, value=元素番号の辞書型になる
        input_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        word_list = [word for word in re.split(r'\W+', input_str) if len(word) > 0]
        one_pos_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

        # 元素記号格納辞書
        element = {}
        for num, word in enumerate(word_list):
            if num+1 in one_pos_list:
                element[word[0:1]] = num+1
            else:
                element[word[0:2]] = num+1

        return element

    @classmethod
    def Q_005_1(cls, n):
        """ 05. n-gram
        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
        文字bi-gramを処理
        """

        input_str = "I am an NLPer"
        return cls.Q_005_ngram(input_str, n)

    @classmethod
    def Q_005_2(cls, n):
        """ 05. n-gram
        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
        単語bi-gramを処理
        """

        input_str = "I am an NLPer"
        word_list = [word for word in re.split(r'\W+', input_str) if len(word) > 0]
        return cls.Q_005_ngram(word_list, n)

    @classmethod
    def Q_005_ngram(cls, input, n):
        last = len(input) - n + 1
        return [input[i:i+n] for i in range(0, last)]

    @classmethod
    def Q_006(cls):
        pass

    @classmethod
    def Q_007(cls):
        pass

    @classmethod
    def Q_008(cls):
        pass

    @classmethod
    def Q_009(cls):
        pass

    @classmethod
    def Q_010(cls):
        pass

    @classmethod
    def Q_011(cls):
        pass

    @classmethod
    def Q_012(cls):
        pass

    @classmethod
    def Q_013(cls):
        pass

    @classmethod
    def Q_014(cls):
        pass

    @classmethod
    def Q_015(cls):
        pass

    @classmethod
    def Q_016(cls):
        pass

    @classmethod
    def Q_017(cls):
        pass

    @classmethod
    def Q_018(cls):
        pass

    @classmethod
    def Q_019(cls):
        pass

    @classmethod
    def Q_020(cls):
        pass

    @classmethod
    def Q_021(cls):
        pass

    @classmethod
    def Q_022(cls):
        pass

    @classmethod
    def Q_023(cls):
        pass

    @classmethod
    def Q_024(cls):
        pass

    @classmethod
    def Q_025(cls):
        pass

    @classmethod
    def Q_026(cls):
        pass

    @classmethod
    def Q_027(cls):
        pass

    @classmethod
    def Q_028(cls):
        pass

    @classmethod
    def Q_029(cls):
        pass

    @classmethod
    def Q_030(cls):
        pass

    @classmethod
    def Q_031(cls):
        pass

    @classmethod
    def Q_032(cls):
        pass

    @classmethod
    def Q_033(cls):
        pass

    @classmethod
    def Q_034(cls):
        pass

    @classmethod
    def Q_035(cls):
        pass

    @classmethod
    def Q_036(cls):
        pass

    @classmethod
    def Q_037(cls):
        pass

    @classmethod
    def Q_038(cls):
        pass

    @classmethod
    def Q_039(cls):
        pass

    @classmethod
    def Q_040(cls):
        pass

    @classmethod
    def Q_041(cls):
        pass

    @classmethod
    def Q_042(cls):
        pass

    @classmethod
    def Q_043(cls):
        pass

    @classmethod
    def Q_044(cls):
        pass

    @classmethod
    def Q_045(cls):
        pass

    @classmethod
    def Q_046(cls):
        pass

    @classmethod
    def Q_047(cls):
        pass

    @classmethod
    def Q_048(cls):
        pass

    @classmethod
    def Q_049(cls):
        pass

    @classmethod
    def Q_050(cls):
        pass

    @classmethod
    def Q_051(cls):
        pass

    @classmethod
    def Q_052(cls):
        pass

    @classmethod
    def Q_053(cls):
        pass

    @classmethod
    def Q_054(cls):
        pass

    @classmethod
    def Q_055(cls):
        pass

    @classmethod
    def Q_056(cls):
        pass

    @classmethod
    def Q_057(cls):
        pass

    @classmethod
    def Q_058(cls):
        pass

    @classmethod
    def Q_059(cls):
        pass

    @classmethod
    def Q_060(cls):
        pass

    @classmethod
    def Q_061(cls):
        pass

    @classmethod
    def Q_062(cls):
        pass

    @classmethod
    def Q_063(cls):
        pass

    @classmethod
    def Q_064(cls):
        pass

    @classmethod
    def Q_065(cls):
        pass

    @classmethod
    def Q_066(cls):
        pass

    @classmethod
    def Q_067(cls):
        pass

    @classmethod
    def Q_068(cls):
        pass

    @classmethod
    def Q_069(cls):
        pass

    @classmethod
    def Q_070(cls):
        pass

    @classmethod
    def Q_071(cls):
        pass

    @classmethod
    def Q_072(cls):
        pass

    @classmethod
    def Q_073(cls):
        pass

    @classmethod
    def Q_074(cls):
        pass

    @classmethod
    def Q_075(cls):
        pass

    @classmethod
    def Q_076(cls):
        pass

    @classmethod
    def Q_077(cls):
        pass

    @classmethod
    def Q_078(cls):
        pass

    @classmethod
    def Q_079(cls):
        pass

    @classmethod
    def Q_080(cls):
        pass

    @classmethod
    def Q_081(cls):
        pass

    @classmethod
    def Q_082(cls):
        pass

    @classmethod
    def Q_083(cls):
        pass

    @classmethod
    def Q_084(cls):
        pass

    @classmethod
    def Q_085(cls):
        pass

    @classmethod
    def Q_086(cls):
        pass

    @classmethod
    def Q_087(cls):
        pass

    @classmethod
    def Q_088(cls):
        pass

    @classmethod
    def Q_089(cls):
        pass

    @classmethod
    def Q_090(cls):
        pass

    @classmethod
    def Q_091(cls):
        pass

    @classmethod
    def Q_092(cls):
        pass

    @classmethod
    def Q_093(cls):
        pass

    @classmethod
    def Q_094(cls):
        pass

    @classmethod
    def Q_095(cls):
        pass

    @classmethod
    def Q_096(cls):
        pass

    @classmethod
    def Q_097(cls):
        pass

    @classmethod
    def Q_098(cls):
        pass

    @classmethod
    def Q_099(cls):
        pass

