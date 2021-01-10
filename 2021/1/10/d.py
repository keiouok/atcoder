import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, C = MAP()
L = [LIST() for i in range(N)]

ans = 0

ma_day = 0
c_all = 0
dic = defaultdict(int)
imos_dic = defaultdict(int)

for i in range(N):
    a, b, c = L[i]
    ma_day = max(ma_day, b)
    dic[a] += 1
    dic[b+1] += 1
    # imos_dic[a] += -1
    # imos_dic[b+1] += 1
    imos_dic[a] += c
    imos_dic[b+1] += -c
    day = b - a + 1
    c_all += day * c

print(dic)
# imos_dic = sorted(imos_dic)
imos_dic = sorted(imos_dic.items(), key=lambda pair: pair[0], reverse=False)

r = 0
# for day, c in imos_dic:
#     day
wa = 0
Wa = []
for i in range(len(imos_dic) - 1):
    day_s, c_s = imos_dic[i]
    day_e, c_e = imos_dic[i+1]
    imos_dic[i+1][1] += imos_dic[i][1]
    ans += imos_dic[i][1] * (day_e - day_s + 1)
    # gap = day_e - day_s + 1    
    # wa = wa + c_e + c_s
    # Wa.append(wa)
print(ans)
exit()
print(Wa)

print(imos_dic)

C_all = ma_day * C
print("C_all:", C_all)
print("c_all:", c_all)

# exit()

imos = [0] * (2 * 10 ** 5 + 1)

# exit()
imos = [0] * (ma_day + 2)


for i in range(N):
    a, b, c = L[i]
    # imos[a:b+1]
    imos[a] += c
    imos[b+1] -= c

print(imos)
for i in range(N):
    imos[i+1] += imos[i]
    # 1, 2日のみ使う
print(imos)