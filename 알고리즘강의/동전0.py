N, K = list(map(int, input().split()))
list = [int(input()) for _ in range(N)]
count = 0

for i in range(N):
    if list[N-1-i] >= K:
        continue
    else:
        while True:
            K = K - list[N-1-i]
            count += 1
            if K < list[N-1-i]:
                break
print(count)