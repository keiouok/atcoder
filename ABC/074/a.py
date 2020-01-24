import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7A,B,C,D,E,F=map(int,input().split())
X=[]
Y=[]
for i in range(31):
    for j in range(31):
        x=100*A*i+100*B*j
        if x<=F:
            X.append(x)
for i in range(1501):
    for j in range(1501):
        y=C*i+D*j
        if y<=F:
            Y.append(y)
 
X=set(X)
Y=set(Y)
X=list(X)
Y=list(Y)
X.sort()
Y.sort()
#print(X)
#print(Y)
 
e=(100*E)/(100+E)
ans=0
x_ans=0
y_ans=0
#print("e",e)
flag=False
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i]+Y[j]<=F and X[i]+Y[j]!=0:
            dense=(100*Y[j])/(X[i]+Y[j])
            #print(dense)
            if dense<=e:
                flag=True#suger exist
            #if Y[j]<=(E*X[i]/100):
                if ans<dense:
                    ans=dense
                    #print(X[i])
                    #print(Y[j])
                    x_ans=X[i]+Y[j]
                    y_ans=Y[j]
if flag:
    print(x_ans,y_ans)
else:
    water=A
    print(A,0)
A,B,C,D,E,F=map(int,input().split())
X=[]
Y=[]
for i in range(31):
    for j in range(31):
        x=100*A*i+100*B*j
        if x<=F:
            X.append(x)
for i in range(1501):
    for j in range(1501):
        y=C*i+D*j
        if y<=F:
            Y.append(y)

X=set(X)
Y=set(Y)
X=list(X)
Y=list(Y)
X.sort()
Y.sort()
#print(X)
#print(Y)

e=(100*E)/(100+E)
ans=0
x_ans=0
y_ans=0
#print("e",e)
flag=False
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i]+Y[j]<=F and X[i]+Y[j]!=0:
            dense=(100*Y[j])/(X[i]+Y[j])
            #print(dense)
            if dense<=e:
                flag=True#suger exist
            #if Y[j]<=(E*X[i]/100):
                if ans<dense:
                    ans=dense
                    #print(X[i])
                    #print(Y[j])
                    x_ans=X[i]+Y[j]
                    y_ans=Y[j]
if flag:
    print(x_ans,y_ans)
else:
    water=A
    print(A,0)
