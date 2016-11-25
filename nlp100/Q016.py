# coding: utf-8

from util import util
import linecache

def Q_016_1(n):
    """ 16. ファイルをN分割する
    自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
    """

    file_name = 'data/hightemp.txt'
    line_count = len(linecache.getlines(file_name))
    linecache.clearcache()
    data = []
    with open(file_name, 'r') as f:
        for i in range(int(line_count / n + 1)):
            n_data = []
            for j in range(n):
                line = f.readline()
                if line:
                    n_data.append(line.strip())
            data.append(n_data)
    return data

def Q_016_2(n):
    """ 16. ファイルをN分割する
    同様の処理をsplitコマンドで実現せよ．
    """

    for _ in util.exe_cmd('mkdir -p data/splitted'.format(n=n)): pass
    for _ in util.exe_cmd('split -l {n} -a 3 data/hightemp.txt data/splitted/hightemp.txt.'.format(n=n)): pass
    return 0
