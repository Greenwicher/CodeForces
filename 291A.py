# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:50:32 2015

@author: liuweizhi
"""

## version 1
n=input();c=[0]*(n+1)
a=sorted([0]+map(int,raw_input().split()));b=list(set(a));
for i in range(len(b)):c[i]=a.count(b[i])
print [sum(1 for i in c[1:] if i==2),-1][max(c[1:]+[0])>2]

## version 2
n,list=input(),map(int,raw_input().split())
a=[list.count(i) for i in set(list) if i>0]
print [a.count(2),-1][max(a+[0])>2]
    

