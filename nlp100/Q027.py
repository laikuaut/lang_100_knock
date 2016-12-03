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
        # 斜体
        self.__regex_italic = re.compile(r"''(.+)''")
        # 強調
        self.__regex_bold = re.compile(r"'''(.+)'''")
        # 斜体と強調
        self.__regex_italic_and_bold = re.compile(r"'''''(.+)'''''")
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
                    self.info_data[key] = self.__formatter(value)
                else:
                    self.info_data[key] += self.__formatter(line.rstrip())

    def __formatter(self, line):
        line = self.__emphasis_remove(line)
        line = self.__inner_link_remove(line)
        return line

    def __emphasis_remove(self, line):
        # 強調マークアップ正規表現リスト
        regex_emphasis_list = [
                self.__regex_italic_and_bold,
                self.__regex_bold,
                self.__regex_italic,
        ]

        for regex in regex_emphasis_list:
            line = regex.sub('\g<1>', line)
        return line

    def __inner_link_remove(self, line):
        while self.__regex_inner_link.search(line):
            startRange = self.__regex_inner_link_start.search(line).span()
            endRange = self.__regex_inner_link_end.search(line).span()
            inner_string = line[startRange[1]:endRange[0]]
            pre_string = line[0:startRange[0]]
            post_string = line[endRange[1]:]
            inner_data = inner_string.split('|')
            inner_string = inner_data[1] if len(inner_data) > 1 else inner_data[0]
            line = pre_string + inner_string + post_string
        return line

def Q_027():
    """ 27. 内部リンクの除去
    26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ.
    （参考: [マークアップ早見表](http://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8)）
    """

    basis_info = BasisInfo()
    basis_info.readFile('data/Britain.txt')

    return basis_info.info_data



