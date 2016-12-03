# coding: utf-8

from util import util
import linecache

def Q_015_1(n):
    """ 15. 末尾のN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
    """

    file_name = 'data/hightemp.txt'
    line_count = len(linecache.getlines(file_name))
    tail_n = line_count - n
    data = [ linecache.getline(file_name, tail_n + i + 1).strip() for i in range(n)]
    linecache.clearcache()
    return data

def Q_015_2(n):
    """ 15. 末尾のN行を出力
    確認にはtailコマンドを用いよ．
    """

    ite = util.exe_cmd('tail -n {n} data/hightemp.txt'.format(n=n))
    return list(ite)
