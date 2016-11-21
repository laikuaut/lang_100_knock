# coding: utf-8

from util import util

def Q_015(n):
    """ 15. 末尾のN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
    """

    ite = util.exe_cmd('tail -n {n} data/hightemp.txt'.format(n=n))
    return list(ite)
