# atcoder

早く土から出たい．

## 参考文献

二次元配列

http://sonickun.hatenablog.com/entry/2014/06/13/132821

https://qiita.com/knakajima3027/items/b871631b8997a6d67223

[python] いろいろな文字種のリストを作成

https://qiita.com/okkn/items/3aef4458ed2269a59d63

## cheet_sheet

```
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

## 最小公倍数
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


## 最大公約数 
def lcm(a, b):
    y = a*b / gcd(a, b)
    return int(y)
```

## list内をstring出力

2重リストの展開表示(要素がintの場合はaの部分にmapをかけてint型をstr型にキャストしておく)

```

a = [[".", "#", "."], ["#", "#", "#"]]
print(*["".join(x) for x in a], sep="\n")
```
```
.#.
```

## 3 数以上の最小公倍数、最大公約数
```
def many_lcm(l):
    tmp = l[0]
    for i in range(1, len(l)):
        tmp = tmp * l[i]//gcd(tmp, l[i])
    return tmp
```

## 約数の列挙
```
def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
```
## 素因数分解
```
#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table
```

## 素数判定
```
#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1
```

## エラトステネスの篩
 O(nloglogn), 素数列挙
```
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table
```
## べき乗
```
#xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x%m, n//2, m)
    if n%2 == 1:
        res = res*x%m
    return res
```

## bit生成
```
import itertools
L = [0, 1] #生成する数字
num = 3 #生成するビット数
bit_list = list(itertools.product([0, 1], repeat=num))

'''実行結果
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
'''
```

## 階乗
```
import itertools

seq = ('a', 'b', 'c', 'd', 'e')

#階乗
ptr = list(itertools.permutations(seq)) #組み合わせ列挙 5!

'''実行結果
[('a', 'b', 'c', 'd', 'e'),
 ('a', 'b', 'c', 'e', 'd'),
 ('a', 'b', 'd', 'c', 'e'),
 ('a', 'b', 'd', 'e', 'c'),
           中略
 ('e', 'd', 'c', 'a', 'b'),
 ('e', 'd', 'c', 'b', 'a')]
 '''

ptr_num = len(list(itertools.permutations(seq))) #組み合わせ数 

'''実行結果
    120
'''
```

## 順列
```
#nPa(順列)
import itertools

seq = ('a', 'b', 'c', 'd', 'e')
ptr = list(itertools.permutations(seq, 3)) #順列列挙 5P3

'''実行結果
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'b'),
       中略
 ('e', 'd', 'a'),
 ('e', 'd', 'b'),
 ('e', 'd', 'c')]
'''

ptr_num = len(list(itertools.permutations(seq, 3))) #順列数

'''実行結果
    60
'''
```
## 組み合わせ
```
#nCa (組み合わせ)
import itertools

seq = ('a', 'b', 'c', 'd', 'e')
ptr = list(itertools.combinations(seq,3)) # 組み合わせ列挙 5C3

'''実行結果
[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'd'),
 ('a', 'c', 'e'),
 ('a', 'd', 'e'),
 ('b', 'c', 'd'),
 ('b', 'c', 'e'),
 ('b', 'd', 'e'),
 ('c', 'd', 'e')]
 '''
```

## 数え上げ
```
from collections import Counter
arr = [1,1,4,6,1,1,35,1,5,1,3]
d = Counter() #インスタンスを生成
d.update(arr)
print(d[1]) #d[数えたい値]

'''実行結果
6
'''
```

## 多次元配列のソート
```
A = [[1, 2], [3, 1], [2, 5]]
B = sorted(A, key=lambda x: x[0]) # 0番目の要素でソート
C = sorted(A, key=lambda x: x[1]) # 1番目の要素でソート

'''実行結果
B = [[1, 2], [2, 5], [3, 1]]
C = [[3, 1], [1, 2], [2, 5]]
'''
```

## にぶたん
```
import bisect
#ソートされたリストAにソートを崩さずに値xを挿入するとき、xの入るべきインデックスを返す。
bisect.bisect(A,x)

#リストAに値xを入れ、xが複数になるとき、一番左の値xのインデックスを返す
bisect.bisect_left(A,x)

#リストAに値xを入れ、xが複数になるとき、一番右の値xのインデックスを返す
bisect.bisect_right(A,x)
```


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

# にぶたん
# A * N + B * d(N)
# d(N)は桁数
# 10 7 100
# 10 * N + 7 * d(N)

def ret(a, b, N):
    return a * N + b * len(str(N))
# bigger number, more expensive
ABC146C，整数屋の問題から自作．rightは[left, right)が半開区間となり，leftは含むがrightを含まないようにするために，right = x + 1にする必要がある．
```
# x = 持っているお金の金額
# 返すのは，お店で変える最大の整数N
# retは整数Nを買うのに必要な金額を返す関数

def binary_search(x):
    left = 0
    right = x + 1

    while(right - left > 1):
        mid = (right + left) // 2
        r = ret(a, b, mid)
        if r > x:
            right = mid
        else:
            left = mid
    return min(left, 10 ** 9)
```

## UnionFind
```
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)
```

## クラスカル法

```
#union-find木
#クラスカル法にはUnion-find木が必要
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


#クラスカル法
# V: 頂点集合(リスト) E: 辺集合[始点, 終点, 重み](リスト)
class kruskal():
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.E.sort(key=lambda x: x[2]) #辺の重みでソート

    def weight(self): #最小全域木の重み和を求める
        UF = UnionFind(len(V)) #頂点数でUnion Find Treeを初期化
        res = 0
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res += e[2]

        return res

    def edge(self):
        UF = UnionFind(len(self.V)) #頂点数でUnion Find Treeを初期化
        res_E = []
        for i in range(len(self.E)):
            e = self.E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_E.append(e)

        return res_E

    def node(self):
        UF = UnionFind(len(V)) #頂点数でUnion Find Treeを初期化
        res_V = []
        for i in range(len(E)):
            e = E[i]

            if (UF.same(e[0], e[1])) == False:
                UF.unite(e[0], e[1])
                res_V.append(e[0])
                res_V.append(e[1])

        return list(set(res_V))
        
        
```

## ワ―シャルフロイド法
```
#d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V): 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d #d[i][j]に頂点i, j間の最短距離を格納
```

## 文字列生成
```
>>> import string
>>> help(string)
(中略)
DATA
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv...\xaf\xb0...
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    whitespace = '\t\n\x0b\x0c\r '
>>> string.digits
'0123456789'
```

## アルファベット，英語，小文字
```
[chr(i) for i in range(97, 97+26)]
# [chr(i) for i in range(ord('a'), ord('z')+1)]
```

## 二次元配列，書き変わらないようにリスト内包で作成せよ

悪い例，他の要素の置き換わる
```
arr = [[0] * 10] * 10
```

いい例

```
arr = [[0 for i in range(10)] for j in range(10)]
```


## 素数列挙 O(NloglogN) (by tonnnura)
```
def primes_for(n):
  is_prime = [True] * (n + 1)
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, n + 1):
      for j in range(i * 2, n + 1, i):
          is_prime[j] = False
  return [i for i in range(n + 1) if is_prime[i]]
```
## ABC035D ダイクストラ法
```
def dijkstra(E, start):
    N_d = len(E)
    dist = [INF] * N_d
    dist[start] = 0
    q = [(0, start)]
    while q:
        dist_v, v = heappop(q)
        if dist[v] != dist_v:
            continue
        for u, dist_vu in E[v]:
            dist_u = dist_v + dist_vu
            if dist_u < dist[u]:
                dist[u] = dist_u
                heappush(q, (dist_u, u))
    return dist
```
E は 連結リスト(多分) startは始点

E[a].append(b, c)

意味するのは，「a番目のノードがbと繋がっており，コストはc」 これが連結リスト．すべてのノードからダイクストラを求める必要はない．0スタートを逆順にすればよいだけ．大事．

