# coding: utf-8

from .mecab_read import read_mecab_data
from collections import defaultdict
from pylab import *
from pandas import *

def Q_037():
    """ 37. 頻度上位10語
    出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    noun_phrase_set = defaultdict(lambda: 0)
    for sent in data:
        for word in sent:
            noun_phrase_set[word['surface']] += 1

    rank_10 = [(k, v) for k, v in sorted(noun_phrase_set.items(), key=lambda x:x[1], reverse=True)][0:10]

    # 日本語を使うため必要
    fontprop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/vlgothic/VL-Gothic-Regular.ttf")

    count_list = [v[1] for v in rank_10]
    index = ['{}位\n{}'.format(i, v[0]) for i, v in enumerate(rank_10, start=1)]
    plt.bar(range(1,11), count_list, align='center', width=0.3)
    plt.xticks(range(1,11), index, fontproperties=fontprop)
    plt.xlabel('単語表層系', fontproperties=fontprop)
    plt.ylabel('出現頻度', fontproperties=fontprop)
    plt.title('単語の出現頻度の棒グラフ(上位10単語)', fontproperties=fontprop)
    plt.grid(True)
    plt.savefig("result/Q037.png")

    return None

