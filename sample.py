#!/usr/bin/env python
# config: utf-8

from nlp100 import Q008

def main():

    in_str     = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(Q008.cipher(in_str))


if __name__ == '__main__':
    main()
