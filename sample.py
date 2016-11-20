#!/usr/bin/env python
# config: utf-8

from nlp100 import Q008

def main():
    in_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    data = Q008.encode(in_str)
    out_str = Q008.decode(data)

    print(in_str)
    print(data)
    print(out_str)


if __name__ == '__main__':
    main()
