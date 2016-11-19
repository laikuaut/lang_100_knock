# config: utf-8

from . import Q005

# 和集合
def Q_006_1():
    """ 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
    それぞれ, XとYとして求め，XとYの和集合を求めよ．
    """

    set1 = set(Q005.ngram("paraparaparadise", 2))
    set2 = set(Q005.ngram("paragraph", 2))

    return set1 | set2

def Q_006_2():
    """ 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
    それぞれ, XとYとして求め，XとYの積集合を求めよ．
    """

    set1 = set(Q005.ngram("paraparaparadise", 2))
    set2 = set(Q005.ngram("paragraph", 2))

    return set1 & set2

def Q_006_3():
    """ 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
    それぞれ, XとYとして求め，XとYの差集合を求めよ．
    """

    set1 = set(Q005.ngram("paraparaparadise", 2))
    set2 = set(Q005.ngram("paragraph", 2))

    return set1 - set2

def Q_006_4():
    """ 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合
    'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """

    set1 = set(Q005.ngram("paraparaparadise", 2))
    set2 = set(Q005.ngram("paragraph", 2))

    return 'se' in set1

def Q_006_5():
    """ 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合
    'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """

    set1 = set(Q005.ngram("paraparaparadise", 2))
    set2 = set(Q005.ngram("paragraph", 2))

    return 'se' in set2

def Q_006_6():
    """ 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合
    それぞれ, XとYとして求め，XとYの排他的論理和を求めよ．
    """

    set1 = set(Q005.ngram("paraparaparadise", 2))
    set2 = set(Q005.ngram("paragraph", 2))

    return set1 ^ set2
