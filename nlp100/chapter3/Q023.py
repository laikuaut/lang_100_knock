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
        self.__re_secrion_line = re.compile(r'^(={2,})(.+?)(={2,})$')
        # (セクション名, セクションレベル)のタプル格納リスト
        self.section_list = []

    def addSection(self, line):
        """ セクション行追加
        入力行がセクション構造の行であるかを判定し、
        セクション行である場合は、セクション情報リストへ追加する。
        """
        matchObj = self.__re_secrion_line.match(line)
        if matchObj:
            groups = matchObj.groups()
            level_symbol = groups[0]
            level = len(level_symbol) - 1
            name = line.replace(level_symbol, '')
            self.section_list.append((name, level))

def Q_023():
    """ 23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
    """

    section = Section()
    with open('data/Britain.txt', 'r') as f:
        for line in f:
            section.addSection(line.strip())

    return section.section_list

