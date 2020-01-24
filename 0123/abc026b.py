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

def main():
    N = INT()
    L = [INT() for i in range(N)]
    C = [L[i] * L[i] * pi for i in range(N)]
    C.sort(reverse=True)
    ans = 0
    for i in range(N):
        # if i == 0:
        #     ans += C[i]
        # else:
        if i % 2 == 0:
            ans += C[i]
        else:
            ans -= C[i]
    print(ans)





if __name__ == "__main__":
    main()


