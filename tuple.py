#!/usr/bin/python
# -*- coding:utf8 -*-
#元组
tuple={'A','我'}
print len(tuple)
tuple={'d','mdb','我们'.decode('CP936')}
print tuple  #set(['mdb', u'\u93b4\u621c\u6ed1', 'd'])

tuple=3*(1+4,)
print tuple  #(5,5,5)
print tuple.count(5)  #3
