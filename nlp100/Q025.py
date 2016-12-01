# coding: utf-8

import re

def Q_025():
    """ 25. テンプレートの抽出
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
    """

    # 基礎情報開始行判定用正規表現(regex for checking basis info start line.)
    regex_start_basis_info = re.compile(r'{{基礎情報 ')
    # フィード判定用正規表現(regex for deciding feed line.)
    regex_start_feed = re.compile(r'^\|')
    # 値連続行判定用正規表現
    regex_next_feed_value = re.compile(r'^\*')
    # 基礎情報終了行判定用正規表現
    regex_end_basis_info = re.compile(r'^}}$')

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
                basis_info_list[key] = value
            if regex_next_feed_value.match(line):
                basis_info_list[key] += line.rstrip().lstrip('*')

    return basis_info_list
