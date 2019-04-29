#!/usr/bin/python
# -*- coding:utf8 -*-

print range(2,9)

#相邻元素的间隔为3
print range(2,9,3)

print '-'*70

L=[1,2,3]
for a in L:
    a+=1  #a不是引用，不会改变L元素值
print L

#range()与len()函数遍历序列并修改元素
for i in range(len(L)):
    L[i]+=1 #通过索引访问
print L

#简单搜索质数
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print n,'equals',x,'*',n/x
            break
        else:
            print n,'是一个质数'

