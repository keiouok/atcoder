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

# にぶたん
# A * N + B * d(N)
# d(N)は桁数
# 10 7 100
# 10 * N + 7 * d(N)

# bigger number, more expensive
def main():
    a, b, x = MAP()
    # below x en 
    k = 1
    # k桁で買えるもの
    # 10 ** k <= N < 10 ** (k + 1)
    # k = 1なら，a * 10 + b * 2 <= x，これがx以下なら，k = 2に変わる．xより大きければ，k=1のまま，なのでOK
    while a * (10 ** k) + b * (k + 1) <= x: # k桁における最小の価格
        k += 1
    # 二分探索すべき一番大きい桁が分かった
    # 整数10 ** 9以上を買うには10 ** 9 + 0円が必要
    if k >= 10:
        print(10 ** 9)
        exit()
    n = (x - (b * k)) // a
    if len(str(n)) != k:
        n -= 1
    print(0 if n <= 0 else n)

    # if n <= 0:
    #     print(0)
    # else:
    #     print(n)
if __name__ == "__main__":
    main()





