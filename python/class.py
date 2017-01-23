#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性， 私有属性在外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" %(self.name, self.age))

p = people('tom', 10, 30)
p.speak()
