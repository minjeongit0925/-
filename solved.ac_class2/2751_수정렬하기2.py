# 문제
'''
    N개의 수가 주어졌을떄, 이를 오름차순으로 정렬
'''

# 입력
'''
    몇개인가 N <= 1,000,000
    N개의 숫자
'''

# 출력
'''
    오름차순으로 정렬
'''
import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)