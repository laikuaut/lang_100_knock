# coding: utf-8

from util import util
from collections import defaultdict

def Q_019_1():
    """ 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
    各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
    """

    # 1列目のみのリストデータ作成
    data = defaultdict(int)
    with open('data/hightemp.txt', 'r', encoding='utf-8') as f:
        for line in f:
            col1 = line.split('\t')[0]
            data[col1] += 1

    # 出現頻度を算出
    count_list = sorted(data.items(), key=lambda x:x[1], reverse=True)

    # 全ての要素をタプルへ変換(コマンド確認側と合わせるために書く要素を文字列化)
    return list(map(lambda x:tuple(map(lambda y:str(y),x)), count_list))

def Q_019_2():
    """ 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
    確認にはcut, uniq, sortコマンドを用いよ．
    """
    ite = util.exe_cmd('cut -f1 data/hightemp.txt | sort | uniq -c | sort -nr')
    return [tuple(reversed(line.split())) for line in list(ite)]
