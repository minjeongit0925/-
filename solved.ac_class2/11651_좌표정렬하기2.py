# 문제
'''
    2차원 평면 위의 점 N개가 주어진다. 
    좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 
    출력하는 프로그램을 작성하시오.
'''

# 입력
'''
    점의 개수 N
    x, y -> N개의 줄
'''

# 출력
'''
    첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

import sys

N = int(sys.stdin.readline())
locations = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    locations.append([x, y])

locations.sort(key = lambda x: (x[1], x[0]))

for i in range(len(locations)):
    print(locations[i][0], locations[i][1])