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

n = INT()
s = []
for i in range(n):
    m = list(input())
    m.sort()
    s.append(m)
s.sort()
# print(s)
# print(s)
count = 0
ren = 1
r = []
rsum = [0] * n
for i in range(n-1):
    if s[i] == s[i+1]:
        count += 1
        ren += 1
        # print(ren)
        rsum[i+1] +=rsum[i]+1
    else:
        r.append(ren)
        ren = 1
        # print(ren)
r.append(ren)
        
for i in range(n):
    rsum[i] = rsum[i] + 1
    

def P(n, r):
    return factorial(n)//factorial(n-r)

def C(n, r):
    return P(n, r)//factorial(r)
# print(r)

# print(count)
# print("rsum:", rsum)
b = []
rsum.append(1)

for i in range(n):
    if rsum[i]>rsum[i+1]:
        b.append(rsum[i])
    #     continue
    # else:
    #     print(rsum[i+1])
    #     b.append(rsum[i+1])
# print("b", b)
count2 = 0
for i in b:
    # print(i)
    # print(C(i,2))
    count2 += C(i, 2)
print(count2)
    # if b[i]>=3:


# for i in range(n):
#     for j in range(n):
#         # if i != j:
#         if i < j:
#         #     print(s[i])
#         # print(s[j])
#             if s[i] == s[j]:
#                 count += 1
# # for i in range(n):
    
# print(count)