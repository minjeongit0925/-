# 문제
'''
    N은 홀수
    1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
    2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
    N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램.
'''

# 입력
'''
    N, N은 홀수이다.
    N개의 줄에 정수들이 주어진다. 
'''

# 출력
'''
    산술평균. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    중앙값
    최빈값. 여러개일 경우 두 번째로 작은 값을 출력한다.
    범위
'''

import sys 
from collections import Counter

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
nums.sort()

# 산술평균
print(round(sum(nums)/N))

# 중앙값
print(nums[int(N//2)])

# 최빈값_N개의 수들 중 가장 많이 나타나는 값
def modefinder(numbers):
    count = Counter(numbers).most_common()
    if len(count) > 1 and count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
modefinder(nums)

# 범위
print(max(nums) - min(nums))