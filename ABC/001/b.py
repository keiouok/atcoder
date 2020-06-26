import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def is_second(hms):
    seq = hms
    time = seq.split(":")
    # print(time)
    m = 3600
    sec = 0
    for i, t in enumerate(time):        
        t = int(t)
        sec += m * t
        m //= 60
    # print(hms, sec)
    return sec
ans = []


while 1:
    N = INT()
    if N == 0:
        break
    else:
        counter = [0] * (3600 * 24 + 1)
        stock = []
        dic = defaultdict()
        for i in range(N):
            from_to = S_MAP()
            s, e = from_to
            s_s, e_s = is_second(s), is_second(e)
            stock.append([s_s, e_s])
            dic[s_s] = e_s
        # print(dic)
        # print(stock)
        # for s, e in dic.items():
        stock_s = sorted(stock, reverse=False)
        stock_e = sorted(stock_s, key=lambda x: x[1])
        # print(stock_s)
        # print(stock_e)
        # for s, e in stock_e:
        for s, e in stock_e:
            for i in range(s, e, 1):
                counter[i] += 1
        ans.append(max(counter))
for a in ans:
    print(a)







        
