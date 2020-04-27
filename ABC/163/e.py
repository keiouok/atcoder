S = list(input())
N = len(S)

l = [0] * 2019
index = 0
temp = 0
for i in range(N-1, -1, -1):
    temp += int(S[i]) * 10 * index
    l[temp%2019] += 1
    index += 1
 
ans = l[0]
 
for i in range(1, 2019):
    v = l[i]
    ans += v * (v-1) // 2
 
print(ans)