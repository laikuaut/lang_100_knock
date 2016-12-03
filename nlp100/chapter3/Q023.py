# coding: utf-8

import re

class Section(object):
    """ セクション構造クラス
    セクション構造の行を読み込み保存する。
    """
    def __init__(self):
        """ 初期化
        メンバ変数を初期化
        """

        # セクション構造行抽出用正規表現
        self.__re_secrion_line = re.compile(r'^==+.+==+$')
        # セクション構造のレベル部分文字列抽出正規表現
        self.__re_section_level = re.compile(r'==+')
        # (セクション名, セクションレベル)のタプル格納リスト
        self.section_list = []

    def addSection(self, line):
        """ セクション行追加
        入力行がセクション構造の行であるかを判定し、
        セクション行である場合は、セクション情報リストへ追加する。
        """
        if self.__re_secrion_line.match(line):
            self.section_list.append(self.__getSection(line))

    def __getSection(self, line):
        """ セクション情報タプル取得
        セクション行を解析して(セクション名, セクションレベル)のタプルを返却する。
        ※ 入力行はaddSectionにてセクション行であるかを判定済みの前提
        """

        level_symbol = self.__re_section_level.match(line).group()
        level = len(level_symbol) - 1
        name = line.replace(level_symbol, '')
        return (name, level)

def Q_023():
    """ 23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
    """

    section = Section()
    with open('data/Britain.txt', 'r') as f:
        for line in f:
            section.addSection(line.strip())

    return section.section_list

