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
A, B, N = MAP()

x = N

ans1 = (A * (B-1)//B) - A * ((B-1) // B)
ans2 = ((A * N)//B) - A * (N // B)
# print(ans2)
# ans = max(A-1, ans2)

if N < B:
    print(ans2)
else:
    
    print(ans1)

# exit()

exit()
# exit()
memo = [0] * (B+1)
ma = 0
for x in range(1, B+1):
    memo[x] = int((A * (x)/B)) - A * ((x)  // B)
    ma = max(memo[x], ma)
# print(memo[N-1])
print(memo)
# print(N)

# exit()
if N >= B:
    ans = ma
else:
    ans = memo[N]
print(ans)
