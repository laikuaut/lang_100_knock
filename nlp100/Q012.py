# coding: utf-8

from util import util

def Q_012():
    """ 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
    """

    for _ in util.exe_cmd('cut -f1 data/hightemp.txt > data/col1.txt'): pass
    for _ in util.exe_cmd('cut -f2 data/hightemp.txt > data/col2.txt'): pass
