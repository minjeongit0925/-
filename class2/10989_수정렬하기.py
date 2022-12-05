# N개의 수 오름차순으로 정렬하기
# sort를 사용하면 메모리가 부족해서 해결되지 않는다.

# 모두 0인 배열을 만들고,
# index를 활용해서 배열을 정렬해준다.

import sys 

N = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] = nums[num] + 1 # index를 활용한 부분

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)