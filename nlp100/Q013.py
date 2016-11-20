# coding: utf-8

from util import util

def Q_013():
    """ 13. col1.txtとcol2.txtをマージ
    12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
    """

    for _ in util.exe_cmd('paste data/col1.txt data/col2.txt> data/col_merge.txt'): pass
