import sys, re, os
from collections import deque, defaultdict, Counter
from math import gcd, ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
# from fractions import gcd
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

K = INT()

ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += gcd(gcd(i, j), k)
print(ans)


exit()
q = [[str(i)] for i in range(1, K+1)]
# print(q)
s = []
ans = 0
while q:
    a = q.pop()
    # print(q)@
    if len(a) == 3:
        # s.append(a)
        ans += int(a[-1])
        # print(a)
    else:
        for i in range(1, K+1):
            b = deepcopy(a)
            if int(b[-1]) <= i:
                b.append(b[-1])
            # b += str(gcd(i, int(b[-1])))
            else:
                b.append(str(i))
            q.append(b)
print(ans)
# print(s)
# print(s)
# ans = 0
# for d in s:
#     print(sorted(list(d))[0])

# print(ans)
