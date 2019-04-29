#!/usr/bin/python
# -*- coding:utf8 -*-
print("hello world");

x=3;
x*=3;
print x;

import math;
a=math.pi;
b=math.sqrt(9.5);
if(a>b):
    print (a);
else:
    print(b);
#选择两个较大的数
first=1;
second=2;
third=3;
if first<third:
    t=second;
    second=third;
    third=t;
if first<second:
    t=first;
    first=second;
    second=t;
if second<third:
    t=second;
    second=third;
    third=t;
print first,'>',second,'>',third ;

#按照位置参数传递,保证顺序
def fun(a,b):
    print ('a=',a)
    print ('b=', b)
fun(2,3)

def fun(a=0,b=9):
    print ('a=',a)
    print ('b=', b)
fun(39)
fun(20,40)

#按关键字参数传递
fun(b=100,a=9)
fun(b=9)

def fun1(string,*numbers):
    print fun1,numbers
    print max(numbers)
fun1("str",1,2,4,5,5,435,6)

def fun2(a,*b,**c):
    print a,b,c
fun2(10,1,1,2,3,54,5,b=6,c=7,d=0)
