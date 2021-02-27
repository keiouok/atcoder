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

N = INT()

tmp = 1
ma = 0
while 1:
    tmp *= 2
    ma += 1
    if tmp >= N:
        break

dic = [0] * (10 ** 5 + 1)
print(ma)
# exit()    
cnt = 0
dic = defaultdict(int)
for i in range(2, N//2+1):
    for m in range(2, ma+1):
        if i ** m <= N:
            if i ** m not in dic: 
                cnt += 1
                dic[i ** m] = 1
        else:
            break
print(N-len(dic))

