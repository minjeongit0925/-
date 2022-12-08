# N K => 이항계수를 구하는 프로그램 

N, K = list(map(int, input().split()))
mul_N = 1
mul_K = 1
mul_N_K = 1

# 이항계수 공식: N! // K!(N-K)!
for i in range(1, N+1):
    mul_N = mul_N * i
for i in range(1, K+1):
    mul_K = mul_K * i
for i in range(1, N-K+1):
    mul_N_K = mul_N_K * i

print(mul_N // (mul_K * mul_N_K))
