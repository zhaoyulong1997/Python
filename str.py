#!/usr/bin/python
# -*- coding:utf8 -*-

str = 'learn Python'
print str,str[0],str[-1]

#切片
print str[:6]
print str[:8]
#当字符串中有双引号，最好用单引号创建
print '"hjksfdhksfkj"'
#如果用单引号创建有单引号的字符串，字符串中的单引号前加\
print 'doesn\'t'

#特殊字符的转义
print 'E:\note\Python.doc'
#字符串前加r,特殊字符会失效
print r'E:\note\Python.doc'

#  +运算符及格式化字符串
str1='jksfhhj'
str2='dfgkldskfl'
str1=str1+str2
print str1

format_str='there are %d apples %s the desk'
a_tuple=(2,'on')
print format_str%a_tuple
#或者
format_str1='there are {0} apples {1} the desk'.format(3,'on')
print format_str1


str3='zootopia'
print str3.find('to')
str4='s s s g f g w'
print str4.split( )
print ''.join(str4.split())

str='4321'
print '>'.join(str)

str='"Yes",I answered.'
print str.split(',')
print str.lower()
print str.count('e')



