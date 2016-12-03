# coding: utf-8

from util import util

def Q_013_1():
    """ 13. col1.txtとcol2.txtをマージ
    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
    """

    with open('data/col1.txt', 'r') as col1_f, \
         open('data/col2.txt', 'r') as col2_f, \
         open('data/col_merge.txt', 'w') as merge_f:
        for line1, line2 in zip(col1_f, col2_f):
            merge_f.write('{}\t{}\n'.format(line1.strip(), line2.strip()))

def Q_013_2():
    """ 13. col1.txtとcol2.txtをマージ
    確認にはpasteコマンドを用いよ．
    """

    for _ in util.exe_cmd('paste data/col1.txt data/col2.txt> data/col_merge.txt'): pass
