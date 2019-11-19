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
import itertools

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

m = 55555
r = 5
N = INT()
# 素数列挙 O(NloglogN)
def primes_for(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, n + 1):
      for j in range(i * 2, n + 1, i):
          is_prime[j] = False
  return [i for i in range(n + 1) if is_prime[i]]

prime_list = primes_for(m)
# prime_list = prime_list[:55]
# print(prime_list)
last_is_one = []
for prime in prime_list:
    if prime % 10 == 1:
        last_is_one.append(prime)
# print(len(last_is_one))
last_is_one.sort()
# print(last_is_one[:N])
p_s = []
for p in last_is_one[:N]:
    p_s.append(str(p))

ans = " ".join(p_s)
print(ans)

# ans = " ".join(last_is_one[:N])
# print(ans)



# print(last_is)
        # print(prime)


# len(list(itertools.combinations(prime_list, r))

