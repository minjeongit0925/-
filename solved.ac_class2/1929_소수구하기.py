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
import math

M, N = map(int, sys.stdin.readline().split())
nums = []
for i in range(N-M+1):
    nums.append(M)
    M += 1

answer = []

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
for num in nums:
    if isPrime(num):
        print(num)

# 시간초과 해결 방법: 숫자의 제곱근까지만 검사하면 된다.