#!/usr/bin/python
# -*- coding:utf8 -*-

#List2[-1]代表从List2从后往前数的第一个元素


List1=['python','2','3','r']
List2=['a','b','c']
print List1[0],List2[1],List2[-1]

print List1[0:2],List2[1:2]
print List1[:],List2[0:1]

List1.append(22)
print List1

List2.insert(1,2)
print List2

List2.remove('b')
print List2

List2.pop(1)
print List2

# #当数据发生改变后，变量的内存地址发生了改变，
# 那么整型就是不可变数据类型
# 当数据发生改变后，变量的内存地址发生了改变，
# 那么字符串就是不可变数据类型
a=10
print(id(a))

a=20
print(id(a))

print(type(a))


