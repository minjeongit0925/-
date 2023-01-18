# 문제
'''
    비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
    add x: S에 x를 추가한다.
    remove x: S에서 x를 제거한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다.
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
    all: S를 {1, 2, ..., 20}으로 바꾼다.
    empty: S를 공집합으로 바꾼다. 
'''

# 입력
'''
    연산의 수 M
    M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
'''

# 출력
'''
    check 연산이 주어질 때마다, 결과를 출력한다.
'''

import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M):
    orders = sys.stdin.readline().strip().split()

    if len(orders) == 1:
        if orders[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
        continue

    else:
        order, x = orders[0], orders[1]
        num = int(x)

        if order == "add":
            S.add(num)
            
        elif order == "remove":
            S.discard(num) # 요소가 없어도 에러가 나지 않는 함수
        
        elif order == "check":
            if num in S:
                print(1)
            else:
                print(0)
        
        elif order == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
        