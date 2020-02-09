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
    
ans = 0
max_index = 0
# left = 0
# right = k
max_ruiseki = sum(p[0:k])
now_ruiseki = 0
ruiseki = [max_ruiseki]
for left in range(n-k+1):
    if left != 0:
        right = k + left 
        # print(left-1, p[left-1])
        
        # print(right-1 ,p[right-1])
        new_ruiseki = ruiseki[left-1] + p[right-1] - p[left-1]
        ruiseki.append(new_ruiseki)

# print(ruiseki)
m = 0
max_index = 0
for i in range(len(ruiseki)):
    if m != max(m, ruiseki[i]):
        m = ruiseki[i]
        index = i

# print(index)

A = p[index:index+k]
    # now_ruiseki = max_ruiseki
for a in A:
    ans += kitai(a)
print(ans)

    



# next_ruiseki = 0
# for i in range(n-k+1):
#     next_ruiseki = ruiseki    
#     ruiseki = max(ruiseki)


    # A
    # A = p[i:i+k]
    # if c != max(c, sum(A)):
    #     c = sum(A)
    #     C = deepcopy(A)
# for a in C:
#     ans += kitai(a)
# print(ans)




