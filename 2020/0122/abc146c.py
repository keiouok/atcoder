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

def ret(a, b, N):
    return a * N + b * len(str(N))
# bigger number, more expensive
def main():
    a, b, x = MAP()
    # below x en 
    left = 0
    right = x + 1

    # if len(str(x)) >= 10:
    #     print(10 ** 9)
    #     exit()
    while(right - left > 1):
        mid = (right + left) // 2
        r = ret(a, b, mid)
        if r > x:
            right = mid
        else:
            left = mid
    print(min(left, 10 ** 9))
    
if __name__ == "__main__":
    main()





