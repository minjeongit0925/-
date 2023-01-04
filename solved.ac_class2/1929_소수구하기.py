# 문제
'''
    M이상 N이하의 소수를 모두 출력하는 프로그램
'''

# 입력
'''
    M, N 소수가 하나 이상 있는 입력만 주어진다.
'''

# 출력
'''
    한줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

import sys

M, N = map(int, sys.stdin.readline().split())
nums = []
for i in range(N-M+1):
    nums.append(M)
    M += 1

answer = []

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
for num in nums:
    if isPrime(num):
        print(num)