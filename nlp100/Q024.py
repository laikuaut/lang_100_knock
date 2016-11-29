# coding: utf-8

import re

def Q_024():
    """ 24. ファイル参照の抽出
    記事から参照されているメディアファイルをすべて抜き出せ．
    """

    regex = re.compile(r'(?<=^\[\[File:)(.+\.[a-zA-Z]+)(?=\|.+\]\])')
    file_list = []
    with open('data/Britain.txt', 'r') as f:
        for line in f:
            matchObj = regex.search(line)
            if matchObj:
                file_list.append(matchObj.group())
    return file_list
