import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

# def dfs(i, sum):
#     if sum > h:
#     if dfs(i + 1, sum) return True
#     if dfs(i + 1, sum + a[i]) return True
#     # if dfs(i + 1, sum + a[i]) return True
#     return False
## 最小公倍数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


## 最大公約数 
def lcm(a, b):
    y = a*b / gcd(a, b)
    return int(y)

def main():
    h, n = MAP()
    L = [LIST() for i in range(n)]
    A = []
    B = []
    dp1 = [0] * 1002
    dp2 = [0] * 1002
    for i in range(n):
        A.append(L[i][0])
        B.append(L[i][1])
        
    # a = L[0][0]
    # damage_per = [b / a for a, b in L]
    # print(damage_per)
    # 初期化
    for i in range(n):
        dp1[i] = A[i]
        dp2[i] = B[i]
        
    
        # dp2[] = B[i]

    # print(dp1)
    print(dp2)
    


if __name__ == "__main__":
    main()