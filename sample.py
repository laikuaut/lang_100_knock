#!/usr/bin/env python
# coding: utf-8

from util import util
from nlp100.chapter4.Q036 import *

def main():
    data = Q_036()
    for word in data:
        print('{} = {}'.format(word[0], word[1]))

if __name__ == '__main__':
    main()
