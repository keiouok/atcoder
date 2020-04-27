import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
alpha_s = "".join()
S = input()
dic = defaultdict(int)
# list(S)
for s in S:
    dic[s] += 1

if S == alpha_s:
    print(-1)
elif len(S) < len(ascii_lowercase):
    for char in ascii_lowercase:
        if char not in S:
            print(S+char)
            break
else:
    S = S[::-1]
    # abcd...z -> z...a
    for i in range(len(S)-1):
        if S[i+1] < S[i]:
            for char in sorted(S[:i+1]):
                if char > S[i+1]:
                    print(S[::-1][:-i-2]+char)
                    exit()

