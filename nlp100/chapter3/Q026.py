# coding: utf-8

import re

def Q_026():
    """ 26. 強調マークアップの除去
    25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ.
    （参考: [マークアップ早見表](http://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8)）
    """

    # 基礎情報開始行判定用正規表現(regex for checking basis info start line.)
    regex_start_basis_info = re.compile(r'{{基礎情報 ')
    # フィード判定用正規表現(regex for deciding feed line.)
    regex_start_feed = re.compile(r'^\|')
    # 基礎情報終了行判定用正規表現(regex for checking basis info end line.)
    regex_end_basis_info = re.compile(r'^}}$')
    # 斜体
    regex_italic = re.compile(r"''(.+)''")
    # 強調
    regex_bold = re.compile(r"'''(.+)'''")
    # 斜体と強調
    regex_italic_and_bold = re.compile(r"'''''(.+)'''''")
    # 強調マークアップ正規表現リスト
    regex_emphasis_list = [
            regex_italic_and_bold,
            regex_bold,
            regex_italic,
    ]

    basis_info_list = {}
    with open('data/Britain.txt', 'r') as f:
        info_flag = False
        for line in f:
            if regex_start_basis_info.match(line):
                info_flag = True
                break
        for line in f:
            if regex_end_basis_info.match(line):
                break
            if regex_start_feed.match(line):
                key, value = line.rstrip().lstrip('|').split(' = ')
                # 複数行にまたがる要素もあるため、改行コードを戻す
                basis_info_list[key] = emphasis_remove(value, regex_emphasis_list) + "\n"
            else:
                basis_info_list[key] += emphasis_remove(line.rstrip(), regex_emphasis_list) + "\n"

    return basis_info_list

def emphasis_remove(line, regex_list):
    for regex in regex_list:
        line = regex.sub('\g<1>', line)
    return line
