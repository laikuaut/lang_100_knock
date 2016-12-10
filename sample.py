#!/usr/bin/env python
# coding: utf-8

from util import util
from nlp100.chapter4.Q030 import *

def main():
#    mecab_data = read_mecab_info('data/neko.txt.mecab')
#    for sent in mecab_data:
#        for word in sent:
#            print(word.surface, end=" ")
#        print()

#    data = read_mecab_data('data/neko.txt.mecab')
    data = Q_030()
    print(data[0:3])

if __name__ == '__main__':
    main()
