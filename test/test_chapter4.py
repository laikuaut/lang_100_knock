#!/usr/bin/env python
# coding: utf-8

import unittest
import glob
from util import util
from nlp100.chapter4.Q030 import *
from nlp100.chapter4.Q031 import *
from nlp100.chapter4.Q032 import *
from nlp100.chapter4.Q033 import *
from nlp100.chapter4.Q034 import *
from nlp100.chapter4.Q035 import *
from nlp100.chapter4.Q036 import *
from nlp100.chapter4.Q037 import *
#from nlp100.chapter4.Q038 import *
#from nlp100.chapter4.Q039 import *

class Test_Chapter4(unittest.TestCase):

    def test_Q_030(self):
        result = Q_030()

        sent_num = 0
        with open('test/data/Q030.txt', 'r') as f:
            word_num = 0
            for line in f:
                line = line.rstrip('\r\n')
                if line == "EOS":
                    if word_num == 0:
                        self.assertEqual(len(result[sent_num]), 0)
                    word_num = 0
                    sent_num += 1
                else:
                    result_word = result[sent_num][word_num]
                    elems = line.split('\t')
                    self.assertEqual(result_word['surface'], elems[0])
                    self.assertEqual(result_word['pos'], elems[1])
                    self.assertEqual(result_word['pos1'], elems[2])
                    self.assertEqual(result_word['base'], elems[3])
                    word_num+=1

    def test_Q_031(self):
        current = set()
        with open('test/data/Q031.txt', 'r') as f:
            for line in f:
                current.add(line.strip())
        self.assertEqual(Q_031(), current)

    def test_Q_032(self):
        current = set()
        with open('test/data/Q032.txt', 'r') as f:
            for line in f:
                current.add(line.strip())
        self.assertEqual(Q_032(), current)

    def test_Q_033(self):
        current = set()
        with open('test/data/Q033.txt', 'r') as f:
            for line in f:
                current.add(line.strip())
        self.assertEqual(Q_033(), current)

    def test_Q_034(self):
        # [TODO]
        Q_034()
        pass

    def test_Q_035(self):
        # [TODO]
        Q_035()
        pass

    def test_Q_036(self):
        # [TODO]
        Q_036()
        pass

    def test_Q_037(self):
        # [TODO]
        Q_037()
        pass

    def test_Q_038(self):
        pass

    def test_Q_039(self):
        pass

if __name__ == '__main__':
    unittest.main()
