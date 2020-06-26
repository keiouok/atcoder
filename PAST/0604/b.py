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

N, M, Q = MAP()
S = [LIST() for i in range(Q)]
people_point = [0] * (N + 1)
problem_point = [N] * (M + 1)
# mondai_toita_hito
hito_toita_mondai = defaultdict(list)
problem_people = [[] for i in range(M + 1)]
# print(S)
# people_solve = [[] * ]
for s in S:
    # print(s)
    if s[0] == 1:
        n = s[1]
        # print(people_point[n])
        ans = 0
        for problem in hito_toita_mondai[n]:
            ans += problem_point[problem]
        print(ans)
    elif s[0] == 2:
        n, m = s[1], s[2]
        problem_point[m] -= 1
        hito_toita_mondai[n].append(m)
        # for h in problem_people[m]:
            # people_point[h] -= 1
        # problem_people[m].append(n)
        # people_point[n] += problem_point[m]




