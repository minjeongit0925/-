# 문제
'''
    두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
'''

# 입력
'''
    두 개의 자연수
'''

# 출력
'''
    최대 공약수
    최소 공배수
'''

"""
# 첫 시도 => 시간 초과
    import sys

    A, B = map(int, sys.stdin.readline().split())

    for i in range(max(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            print(i)
            break

    for i in range(min(A, B), A * B + 1):
        if i % A == 0 and i % B == 0:
            print(i)
            break
"""

# 두 번째 시도
# 유클리드 호제법 + 최대공약수를 활용한 최소공배수
A, B = map(int, input().split())

def Max(A, B):
    while B != 0:
        mod = A % B
        (A, B) = (B, mod)
    return abs(A)

print(Max(A, B))

def Min(A, B):
    return print(int(A * B / Max(A, B)))

Min(A, B)