# coding: utf-8

import re

def Q_022():
    """ 22. カテゴリ名の抽出
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
    """

    regex = re.compile(r'(?<=^\[\[Category:)(.+)(?=\]\]$)')
    category_list = []
    with open('data/Britain.txt', 'r') as f:
        for line in f:
            matchObj = regex.search(line)
            if matchObj:
                category_list.append(matchObj.group())
    return category_list
