# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:45:18 2015

@author: liuweizhi
"""

## version 1
n=input();a=map(int,raw_input().split());b=sorted(a)
l,r=100001,0
for i in range(n):
    if a[i]!=b[i]:
        l=min(l,i)
    if a[n-1-i]!=b[n-1-i]:
        r=max(r,n-1-i)
    if (l!=100001) and (r!=0):
        break
f=lambda l,r,a:a[:l]+a[l:r+1][::-1]+a[r+1:]
print ['no','yes\n%d %d'%(l+1,r+1)][f(l,r,a)==b] if a!=b else 'yes\n1 1'