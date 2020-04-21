import sys
from copy import deepcopy
def input(): return sys.stdin.readline().strip()
def MAP(): return map(int, input().split())

sys.setrecursionlimit(10 ** 9)

H, W = MAP()
S = [list(input()) for _ in range(H)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def padding(s, color):
    dot = []
    for h in range(H):
        for w in range(W):
            if s[h][w] == color:
                dot.append((h, w))
                
    ans = deepcopy(s)
    for h, w in dot:
        for k in range(8):
            if 0 <=  w + dx[k] < W and 0 <= h + dy[k] < H:
                ans[h+dy[k]][w+dx[k]] = color
                
    return ans

  
def main():
    dot_s = padding(S, ".")
    sharp_s = padding(dot_s,"#")
    if S == sharp_s:
        print("possible")
        print(*["".join(l) for l in dot_s], sep="\n")
    else:
        print("impossible")

        
if __name__ == '__main__':
    main()
