# 要復習
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
    L = LIST()
    L.sort()
    ans = 0
    # count = 0
    for i in range(0, N - 2):
        a = L[i]
        for j in range(i + 1, N - 1):
            b = L[j]
            x = a + b - 1
            # a + b > c なので c <= a + b - 1
            # x の入るべき場所にいれた際，そのxの最初のインデックスを返す
            # print(x)
            index = bisect(L, x)
            # print(index)
            # indexの方が大きければ調べる
            if j < index:
                # index が指してるのは，xを入れるべきindex
                # つまり，a + b - 1 の次に大きい数字の一番最初があるindex
                # を指しているので，それを除くための-1が必要
                ans += (index - j - 1)
    print(ans)
if __name__ == "__main__":
    main()


