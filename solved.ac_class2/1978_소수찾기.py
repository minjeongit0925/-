# 문제
'''
    주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램.
'''

# 입력
'''
    수의 개수 N
    N개의 수
'''

# 출력
'''
    소수의 개수
'''

N = int(input())
nums = list(map(int, input().split()))
answer = 0

# 소수 -> 약수가 1과 자기자신뿐인 수
for num in nums:
    nonAns = 0
    if num > 1: # 숫자가 1보다는 커야함.
        for i in range(2, num): # 2부터 자기자신-1까지 나누기 시작함.
            if num % i == 0: # 나머지가 0 이면 약수가 1과 자기자신 외에 있는 것
                nonAns += 1 # 답이 아님.
        if nonAns == 0: # 몫이 없는 경우 이 숫자는 소수임.
            answer += 1

print(answer)
