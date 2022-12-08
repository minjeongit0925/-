# N개의 수를 입력 받아서 두 수를 뽑아 합이 가장 클 때는?
"""
1. 정렬로 푼 방법 -> 시간 복잡도 O(NlogN)
"""
num = int(input())
nums = []
sumNum = []

for i in range(num):
    nums.append(int(input()))

numsSort = sorted(nums)

print(numsSort[-1]+numsSort[-2])


"""
2. 완전 탐색으로 푼 방법 -> 시간 복잡도 O(N^2)
즉, 시간 복잡도가 너무 커서 시간제한이 1초로 주어질 경우에는 실패함. N이 1,000,000까지일 경우

num = int(input())
nums = []
sumNum = []

for i in range(num):
    nums.append(int(input()))

for i in range(len(nums)):
    for j in range(1, len(nums)):
        sumNum.append(nums[i]+nums[j])

print(max(sumNum))
"""