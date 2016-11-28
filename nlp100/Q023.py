# coding: utf-8

import re

class Section(object):
    def __init__(self):
        self.__re_secrion_line = re.compile(r'^==+.+==+$')
        self.__re_section_level = re.compile(r'==+')
        self.section_list = []

    def addSection(self, line):
        if self.__re_secrion_line.match(line):
            self.section_list.append(self.getSection(line))

    def getSection(self, line):
        level_symbol = self.__re_section_level.match(line).group()
        level = len(level_symbol) - 1
        name = line.replace(level_symbol, '')
        return (name, level)

def Q_023():
    """ 23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
    """

    section = Section()
    with open('data/Britain.txt', 'r') as f:
        for line in f:
            section.addSection(line.strip())

    return section.section_list

