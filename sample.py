#!/usr/bin/env python
# config: utf-8

from nlp100 import Q005

def main():
    list1 = Q005.ngram("paraparaparadise", 2)
    list2 = Q005.ngram("paragraph", 2)

    for i in list1:
        if i not in list2:
            print(i)
    for i in list2:
        if i not in list1:
            print(i)


if __name__ == '__main__':
    main()
