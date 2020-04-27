S = list(input())
N = len(S)
S = [int(s) for s in S]
S = S[::-1]
l = [0] * 2019
index = 0
tmp = 0
z = 1
for i, s in enumerate(S):
    tmp += s * pow(10, i, 2019)
    l[tmp%2019] += 1

ans = l[0]

for v in l:
    ans += v * (v-1) // 2
print(ans)