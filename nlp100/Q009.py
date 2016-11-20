# config: utf-8

import random

def Q_009():
    """ 09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
    それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．
    適当な英語の文
    （例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
    を与え，その実行結果を確認せよ．
    """

    in_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    return typoglycemia(in_str)

def typoglycemia(data):
    word_list = data.split(' ')
    out_list = []
    for word in word_list:
        if len(word) > 4:
            middle_list = [char for char in word[1:-1]]

            # 本来ループの必要はないが、同じ並びの結果だと試験が面倒なので強制的に別の並びしかでないようにする
            while word[1:-1] == ''.join(middle_list):
                random.shuffle(middle_list)
            out_list.append(word[0] + ''.join(middle_list) + word[-1])
        else:
            out_list.append(word)
    return ' '.join(out_list)
