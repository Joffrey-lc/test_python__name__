# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/7 17:07
@Auth ： LC
@File ：supNet.py
@IDE ：PyCharm
"""
print("主程序执行了")


def main():
    print(__name__)
    print("main执行了")


def test():
    print("test执行了")


if __name__ == '__main__':
    print(__name__)
    test()

if __name__ == 'supNet':
    print('被import了')
