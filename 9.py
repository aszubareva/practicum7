N, K, R = map(int, input().split())
c = 1
while N < R:
    c += 1
    N = N + (K/100)*N
print(c)