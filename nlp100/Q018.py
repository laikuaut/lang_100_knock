# coding: utf-8

from util import util

def Q_018_1():
    """ 18. 各行を3コラム目の数値の降順にソート
    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    """
    with open('data/hightemp.txt', 'r') as f:
        data_list = [line.strip().split('\t') for line in f]
        return ['\t'.join(line) for line in sorted(data_list, key=lambda x:x[2], reverse=True)]

def Q_018_2():
    """ 18. 各行を3コラム目の数値の降順にソート
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    """

    ite = util.exe_cmd("sort -k3 -r data/hightemp.txt")
    return list(ite)
