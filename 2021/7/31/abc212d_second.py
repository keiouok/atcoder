def INT(): return int(input())
def LIST(): return list(map(int, input().split()))
import heapq

Q = INT()
L = [LIST() for i in range(Q)]

total = 0

pq = []
# heapq.heapify(pq) # 無くてもたぶん行ける

for q in L:
    if q[0] == 1:
        x = q[1]
        heapq.heappush(pq, x - total)
    elif q[0] == 2:
        x = q[1]
        total += x   
    elif q[0] == 3:
        x = heapq.heappop(pq)
        print(x + total)

