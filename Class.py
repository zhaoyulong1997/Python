#!/usr/bin/python
# -*- coding:utf8 -*-

class Class:
    def setName(self,n):
        #__name实现私有属性的效果
        self.name=n
    def getName(self):
        return self.name

if __name__ == '__main__':
    p1=Class()
    p1.setName('ZHSJ')
    print (p1.getName())