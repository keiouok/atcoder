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

# 二次元配列，他の要素まで書き変わらないように静的確保，意識
# c = [[0] * 10] * 10
c = [[0 for i in range(10)] for j in range(10)]


for i in range(1, n+1):
    s_i = str(i)
    # print(s_i)
    first = int(s_i[0])
    last = int(s_i[-1])
    # print(first)
    # print(last)
    c[first][last] += 1
    # print(c)

# print(c)
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += c[i][j] * c[j][i]
print(ans)


# exit()

# dic = defaultdict(int)
# for i in range(1, n+1):
#     dic["{},{}".format(str(i)[0], str(i)[-1])] += 1

# # print(dic)

# ans = 0
# for n in dic.copy():
#     s, e = n.split(",")
#     # print(s, e)
#     # if s == e:
#     #     ans += dic[n] * dic[n]
#     # else:
#     ans += dic[n] * dic["{},{}".format(e, s)]
# print(ans)        

