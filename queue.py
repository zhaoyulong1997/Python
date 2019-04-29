#!/usr/bin/python
# -*- coding:utf8 -*-
#queue
#队尾进，队首出
print "deque用作队列"
from collections import * #from collections import deque
queue=deque([7,8,9])
queue.append(10)
queue.append(11)
print queue.popleft()
print queue.popleft()
print queue