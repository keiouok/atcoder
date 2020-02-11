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
mod = 10 ** 9 + 7

n, k  = MAP()
p = LIST()

def kitai(a):
    tmp = 0
    # for a in A:
    tmp = 1/a * (1/2 * a * (a+1))
    return tmp
acc = [0] * n

# それぞれの期待値を先に求めて，それから和を求める
for i in range(n):
    acc[i] = (p[i] + 1) / 2
ruiseki = [0] * n
ruiseki[0] = acc[0]
for i in range(n-1):
    ruiseki[i+1] = ruiseki[i] + acc[i+1]
ruiseki.insert(0, 0)
# print(ruiseki)

ans = 0
for i in range(n-k+1):
    m = ruiseki[k+i] - ruiseki[i]
    # print(m)
    ans = max(ans, m)
print(ans)

    
    # if i == 0:
    #     ruiseki[k]
    # else:
    #     ruiseki[k+i] - ruiseki[i]
    # ans = max(ans, acc[i+k]-acc[i])



        {5}  &  {667} & {656} & {529} & {522}\\ \hline 
        {10} &  {657} & {641} & {520} & {510}\\ \hline 
        {15} &  {644} & {624} & {516} & {497}\\ \hline 
        {20} &  {641} & {613} & {511} & {489}\\ \hline 
        {25} &  {631} & {602} & {501} & {479}\\ \hline 
        {30} &  {597} & {588} & {485} & {471}\\ \hline 