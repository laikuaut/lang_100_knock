# coding: utf-8

import re

class BasisInfo(object):

    def __init__(self):
        # 基礎情報辞書
        self.info_data = {}

        # 基礎情報開始行判定用正規表現(regex for checking basis info start line.)
        self.__regex_start_basis_info = re.compile(r'{{基礎情報 ')

        # フィード判定用正規表現(regex for deciding feed line.)
        self.__regex_start_feed = re.compile(r'^\|')

        # 基礎情報終了行判定用正規表現(regex for checking basis info end line.)
        self.__regex_end_basis_info = re.compile(r'^}}$')

        # 斜体と強調
        self.__regex_italic_and_bold = re.compile(r"(?:'{5}|'{2,3})(.+?)(?:'{5}|'{2,3})")

        # 内部リンク判定用正規表現
        self.__regex_inner_link = re.compile(r'\[\[[^:]+\]\]')

        # 内部リンク開始位置判定用正規表現
        self.__regex_inner_link_start = re.compile(r'\[\[')

        # 内部リンク終了位置判定用正規表現
        self.__regex_inner_link_end = re.compile(r'\]\]')

    def readFile(self, file_path):
        with open(file_path, 'r') as f:
            info_flag = False
            for line in f:
                if self.__regex_start_basis_info.match(line):
                    info_flag = True
                    break
            for line in f:
                if self.__regex_end_basis_info.match(line):
                    break
                if self.__regex_start_feed.match(line):
                    key, value = line.rstrip().lstrip('|').split(' = ')
                    self.info_data[key] = self.__formatter(value) + "\n"
                else:
                    self.info_data[key] += self.__formatter(line.rstrip()) + "\n"

    def __formatter(self, line):
        line = self.__emphasis_remove(line)
        line = self.__inner_link_remove(line)
        return line

    def __emphasis_remove(self, line):
        while self.__regex_italic_and_bold.search(line):
            line = self.__regex_italic_and_bold.sub('\g<1>', line)
        return line

    def __inner_link_remove(self, line):
        # 内部リンクを含んている間処理を継続
        while self.__regex_inner_link.search(line):
            # 内部リンク開始記号の文字範囲を取得('[[')
            startRange = self.__regex_inner_link_start.search(line).span()
            # 内部リンク終了記号の文字範囲を取得(']]')
            endRange = self.__regex_inner_link_end.search(line).span()

            # 内部リンクの文字列部分を取得
            inner_string = line[startRange[1]:endRange[0]]
            # 表示文字部分を取得(エスケープ等の考慮なし)
            inner_data = inner_string.split('|')
            inner_string = inner_data[1] if len(inner_data) > 1 else inner_data[0]

            # 整形済みの内部リンクを元の行へ反映( '[['前の文字列 + 内部リンク文字列 + ']]'後の文字列)
            line = line[0:startRange[0]] + inner_string + line[endRange[1]:]
        return line

def Q_027():
    """ 27. 内部リンクの除去
    26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ.
    （参考: [マークアップ早見表](http://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8)）
    """

    basis_info = BasisInfo()
    basis_info.readFile('data/Britain.txt')

    return basis_info.info_data



