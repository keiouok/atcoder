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

island = [list(input()) for i in range(10)]
# False : 通っていない，True：通った
visited = [[False] * 10 for i in range(10)]
circle = sum([line.count("o") for line in island])

def dfs(i, j):
    global visited_copy, island_copy, count
    
    if i != 0 and visited_copy[i-1][j] == False and island_copy[i-1][j] == "o":
        count += 1
        visited_copy[i-1][j] = True
        dfs(i-1, j)

    if j != 0 and visited_copy[i][j-1] == False and island_copy[i][j-1] == "o":
        count += 1
        visited_copy[i][j-1] = True
        dfs(i, j-1)

    if i != 9 and visited_copy[i+1][j] == False and island_copy[i+1][j] == "o":
        count += 1
        visited_copy[i+1][j] = True
        dfs(i+1, j)

    if j != 9 and visited_copy[i][j+1] == False and island_copy[i][j+1] == "o":
        count += 1
        visited_copy[i][j+1] = True
        dfs(i, j+1)

for h in range(10):
    for w in range(10):
        visited_copy = deepcopy(visited)
        island_copy = deepcopy(island)
        # visited already
        visited_copy[h][w] = True
        if island_copy[h][w] == "x":
            island_copy[h][w] = "o"
            count = 0
        else:
            count = 1
        dfs(h, w)
        if count == circle:
            print("YES")
        #    print(*visited_copy, sep="\n")
            exit()
print("NO")
#print(*visited_copy, sep="\n")
