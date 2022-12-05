# N개의 수
num = int(input())
nums = []
sumNum = []

for i in range(num):
    nums.append(int(input()))

numsSort = sorted(nums)

print(numsSort[-1]+numsSort[-2])