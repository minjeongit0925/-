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
    orders = sys.stdin.readline().split()

    if len(orders) == 1:
        order = orders[0]
    else:
        order, x = orders

    if order == "add":
        S.add(int(x))
        
    elif order == "remove":
        S.remove(int(x))
    
    elif order == "check":
        if int(x) in S:
            print(1)
        else:
            print(0)
    
    elif order == "toggle":
        if int(x) in S:
            S.remove(int(x))
        else:
            S.add(int(x))
    
    elif order == "all":
        S = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}
    
    elif order == "empty":
        S.clear()