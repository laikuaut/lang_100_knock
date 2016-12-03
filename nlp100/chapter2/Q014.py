# coding: utf-8

from util import util

def Q_014_1(n):
    """ 14. 先頭からN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
    """

    data = []
    with open('data/hightemp.txt', 'r') as f:
        data = [line.strip() for line, _ in zip(f, range(10))]

    return data

def Q_014_2(n):
    """ 14. 先頭からN行を出力
    確認にはheadコマンドを用いよ．
    """

    ite = util.exe_cmd('head -n {n} data/hightemp.txt'.format(n=n))
    return list(ite)
