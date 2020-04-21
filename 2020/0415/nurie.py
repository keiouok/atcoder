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
L = [LIST() for i in range(N-1)]

graph = defaultdict(list)
for a, b in L:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# q = [(N, par)]
def dfs(n, par):
    # q.append()
    f, g = 1, 1
    for node in graph[n]:
        if node == par:
            continue
        fn, gn = dfs(node, n)
        f *= gn
        f %= mod
        g *= fn
        g % mod
    return (f + g) % mod, g

print(dfs(0, None)[0])


exit()
nurie = [-1] * N + [0]
print(nurie)
nurie1 = deepcopy(nurie)
nurie2 = deepcopy(nurie)
nurie1[0] = 1
nurie2[0] = 0

q = deque([nurie1, nurie2])
print(q)
visited = [False] * N
visited[0] = True
ans = 0
while q:
    a = q.popleft()
    print("a", a)
    if -1 not in a:
        ans += 1
    for node in graph[a[-1]]:
        print(node)
        print(visited[node])
        nurie = deepcopy(a)
        if visited[node] == False:
            visited[node] = True
            print(a[-1])
            print("n", nurie[-1])
            if nurie[nurie[-1]] == 0:
                nurie[node] = 1
                print(nurie)
                nurie[-1] = node
                q.append(nurie)
            elif nurie[a[-1]] == 1:
                for i in [0, 1]:
                    nurie[node] = i
                    nurie[-1] = node
                    q.append(nurie)
print(ans)



            
        
