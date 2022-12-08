# 완전탐색
# 9명 중 7명을 골라 그 합이 100
"""
조합을 활용한 방법
"""
from itertools import combinations

heights = [int(input()) for _ in range(9)]
for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
        break

"""
# 내가 풀었던 방법
# 일곱 난쟁이의 키의 합이 100
import sys 

height = []
no1 = 0
no2 = 0

for i in range(9):
    height.append(int(sys.stdin.readline()))

total = sum(height)

for i in range(9):
    for j in range(i+1, 9):
        if total - (height[i] + height[j]) == 100:
            no1 = height[i]
            no2 = height[j]

height.remove(no1)
height.remove(no2)
height.sort()

for i in range(7):
    print(height[i])
"""