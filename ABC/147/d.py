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

N = INT()
A = LIST()

max_length = len("{:b}".format(max(A)))

cnt = [defaultdict(int) for _ in range(max_length)]

for i in range(N):
    num = "{:b}".format(A[i]).zfill(max_length)
    for j in range(len(num)):
        # [i桁目][numのj番目の数，(0 or 1)]
        # 0, 1 の数を数える
        cnt[max_length-1-j][num[j]] += 1

ans = 0

for i in range(max_length):
    # 1を左にiシフト(2 ** i 倍)
    # 桁内で0の個数 * 桁内で1の個数 が，XOR = 1になる数 (0 xor 1 = 1)
    ans = ans + (1 << i) * cnt[i]["0"] * cnt[i]["1"]
ans = ans % mod
print(ans)



