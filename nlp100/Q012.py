# coding: utf-8

from util import util

def Q_012_1():
    """ 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    各行の1列目だけを抜き出したものをcol1.txtに，
    2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    """
    with open('data/hightemp.txt', 'r') as rf, \
         open('data/col1.txt', 'w') as wf1, \
         open('data/col2.txt', 'w') as wf2:
        for line in rf:
            cols = line.split('\t')
            wf1.write('{}\n'.format(cols[0]))
            wf2.write('{}\n'.format(cols[1]))

def Q_012_2():
    """ 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    確認にはcutコマンドを用いよ．
    """

    for _ in util.exe_cmd('cut -f1 data/hightemp.txt > data/col1.txt'): pass
    for _ in util.exe_cmd('cut -f2 data/hightemp.txt > data/col2.txt'): pass
