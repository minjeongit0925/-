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
while True:
    if M > N:
        break
    for i in range(N-M+1):
        nums.append(M)
        M += 1
print(nums)
answer = []

'''
for num in nums:
    nonAns = 0
    if num > 1: # 숫자가 1보다는 커야함.
        for i in range(2, num): # 2부터 자기자신-1까지 나누기 시작함.
            if num % i == 0: # 나머지가 0 이면 약수가 1과 자기자신 외에 있는 것
                nonAns += 1 # 답이 아님.
        if nonAns == 0: # 몫이 없는 경우 이 숫자는 소수임.
            answer.append(num)
'''