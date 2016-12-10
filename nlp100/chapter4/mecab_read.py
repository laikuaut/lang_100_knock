# coding: utf-8

class WordInfo():
    """ 単語情報クラス
    辞書ではなくて、1要素ごとに使った場合の例
    個人的には、要素が決まっているからこっちの方が使いやすく感じる。
    """
    def __init__(self, word_line):
        # 分割
        elem = word_line.split('\t')
        info_list = elem[1].split(',')
        # 表層形
        self.surface = elem[0]
        # 品詞
        self.pos = info_list[0]
        # 品詞細分類1
        if len(info_list) > 1:
            self.pos1 = info_list[1]
        # 品詞細分類2
        if len(info_list) > 2:
            self.pos2 = info_list[2]
        # 品詞細分類3
        if len(info_list) > 3:
            self.pos3 = info_list[3]
        # 活用形
        if len(info_list) > 4:
            self.conjugation_form = info_list[4]
        # 活用型
        if len(info_list) > 5:
            self.conjugation_type = info_list[5]
        # 原形
        if len(info_list) > 6:
            self.base = info_list[6]
        # 読み
        if len(info_list) > 7:
            self.read_form = info_list[7]
        # 発音
        if len(info_list) > 8:
            self.pronunciation = info_list[8]

def read_mecab_info(file_path):
    mecab_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        mecab_sent = []
        for line in f:
            line = line.rstrip('\n\r')
            if line == "EOS":
                if mecab_sent:
                    mecab_data.append(mecab_sent)
                    mecab_sent = []
            else:
                mecab_sent.append(WordInfo(line))

    return mecab_data

def read_mecab_data(file_path):
    """ 形態素結果読み込み
    Q030の回答
    """
    sent_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        sent = []
        for line in f:
            line = line.rstrip('\n\r')
            word = {}
            if line == "EOS":
                if sent:
                    sent_list.append(sent)
                    sent = []
            else:
                sent.append(get_word_dist(line))
    return sent_list

def get_word_dist(line):
    # 分割
    elem = line.split('\t')
    info_list = elem[1].split(',')
    # 単語辞書情報作成
    word = {
        'surface' : elem[0],
        'base' : info_list[6],
        'pos' : info_list[0],
        'pos1' : info_list[1]
    }
    return word
