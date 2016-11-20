# coding: utf-8

from . import Q003

def Q_004():
    """ 04. 元素記号
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
    取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    """

    # 結果がkey=元素記号, value=元素番号の辞書型になる
    input_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    word_list = Q003.word_split(input_str)
    one_pos_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    # 元素記号格納辞書
    element = {}
    for num, word in enumerate(word_list):
        if num+1 in one_pos_list:
            element[word[0:1]] = num+1
        else:
            element[word[0:2]] = num+1

    return element
