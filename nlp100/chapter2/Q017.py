# coding: utf-8

from util import util

def Q_017_1():
    """ 17. １列目の文字列の異なり
    1列目の文字列の種類（異なる文字列の集合）を求めよ．
    """

    file_name = 'data/hightemp.txt'
    with open(file_name, 'r') as f:
        return {line.split('\t')[0] for line in f}

def Q_017_2():
    """ 17. １列目の文字列の異なり
    確認にはsort, uniqコマンドを用いよ．
    """
    ite = util.exe_cmd('cut -f1 data/hightemp.txt | sort | uniq')
    return set(ite)
