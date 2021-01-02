N = int(input())
P = list(map(int, input().split()))
x = 1
now = 0
ans = []
for i in range(N):
    if P[i] == i + 1:
        print(-1)
        exit()
    if P[i] == x:
        # swap
        P[now:i+1] = [P[i]] + P[now:i]

        # for j in range(now, i+1):
        for j in range(now, i):
            if P[j] != j + 1:
                print(-1)
                exit() 
            else:
                for k in range(i, now, -1):
                    ans.append(k)
                now = i
                x = i + 1
                if P[i] == x and i != N - 1:
                    print(-1)
                    exit()
print(*ans, sep="\n")



