# coding: utf-8

from util import util

def Q_010_1():
    """ 10. 行数のカウント
    行数をカウントせよ．
    """

    num_lines = 0
    with open('data/hightemp.txt', 'r') as f:
        num_lines = sum(1 for line in f)

    return num_lines

def Q_010_2():
    """ 10. 行数のカウント
    確認にはwcコマンドを用いよ．
    """

    ite = util.exe_cmd('wc -l data/hightemp.txt')
    return list(ite)
