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
 
N = INT()
H = [INT() for i in range(N)]

node = []
if H[0] > H[1]:
    node.append((0, "top"))
else:
    node.append((0, "bottom"))

for i in range(1, N-1):
    if H[i-1] < H[i] and H[i] > H[i+1]:
        node.append((i, "top"))
    elif H[i-1] > H[i] and H[i] < H[i+1]:
        node.append((i, "bottom"))
if H[-1] > H[-2]:
    node.append((N-1, "top"))
else:
    node.append((N-1, "bottom"))
print(node)
ans = 0
if H[0] > H[1]:
    ans += node[1][0] + 1
print(ans)
if H[-1] > H[-2]:
    ans = max(ans, N - node[-2][0])
print(ans)

for i in range(len(node)-2):
    if node[i][1] == "bottom" and i+2 <= len(node) - 1:
        ans = max(ans, node[i+2][0]-node[i][0]+1)
print(ans)

