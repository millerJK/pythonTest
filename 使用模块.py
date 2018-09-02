#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'模块测试'
__author__ = "mick"

import sys


def test():
    args = sys.argv;
    if len(args) == 1:
        print("hello,world")
    elif len(args) == 2:
        print(args);
    else:
        print("too many args")


if __name__ == '__main__':
    test()
