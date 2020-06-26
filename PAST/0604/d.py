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

N = INT()
S = [input() for i in range(5)]
# print(len(S[0]))

example = [
".###..#..###.###.#.#.###.###.###.###.###.",
".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.",
".#.#..#..###.###.###.###.###...#.###.###.",
".#.#..#..#.....#...#...#.#.#...#.#.#...#.",
".###.###.###.###...#.###.###...#.###.###."]

Num = []
for i in range(1, 4*(10-1)+1+1, 4):
    # iは1スタート
    # print(i, 4 + i)
    real_left = i
    real_right = i + 4
    l = i
    r = i + 4 - 1
    num = []
    for line in example:
        # print(line)
        num.append(line[l:r])
    Num.append(num)
# print(*Num, sep = "\n")
    
ans = ""
for i in range(1, 4*(N-1)+1+1, 4):
    # iは1スタート
    # print(i, 4 + i)
    real_left = i
    real_right = i + 4
    l = i
    r = i + 4 - 1
    this_num = []
    for line in S:
        # print(line)
        this_num.append(line[l:r])
    for i, Nu in enumerate(Num):
        # print(i, Nu)
        # print("this", this_num)
        if this_num == Nu:
            ans += str(i)
print(ans)

