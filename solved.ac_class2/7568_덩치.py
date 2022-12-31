# 문제
'''
    x kg, y cm (x, y)
    덩치 등수를 계산하여 출력해야 함.
    키와 몸무게가 모두 더 커야 덩치가 더 큰거임.
'''

# 입력
'''
    전체 사람의 수 N 
    x, y
'''

# 출력
'''
    덩치 등수 첫줄에 순서대로
'''
# x 비교 / y 비교 
# -> 둘다 크면 덩치 큼.
# -> 둘중에 하나만 크면 동점.

N = int(input())
big = []
number = []
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    big.append([x, y])

for i in range(N):
    cnt = 0
    for j in range(N):
        if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
            cnt += 1
    
    number.append(cnt + 1)

for i in number:
    print(i, end=" ")