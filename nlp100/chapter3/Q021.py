# coding: utf-8

import re

def Q_021():
    """ 21. カテゴリ名を含む行を抽出
    記事中でカテゴリ名を宣言している行を抽出せよ．
    """

    regex = re.compile(r'^\[\[Category:.+\]\]$')
    category_list = []
    with open('data/Britain.txt', 'r') as f:
        for line in f:
            if regex.match(line):
                category_list.append(line.strip())
    return category_list
