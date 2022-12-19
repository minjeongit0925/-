# 문제
'''
    N개의 정수 A[1],A[2],...,A[N] 이 안에 X라는 정수가 존재하는가?
'''

# 입력
'''
    자연수 N
    A[1], A[2], A[3], ... A[N]
    M
    M개의 수들 -> A 안에 존재하는가
'''

# 출력
'''
    존재하면 1, 존재하지 않으면 0
'''

"""
# 첫번째 시도
    import sys

    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))

    for i in range(len(B)):
        if B[i] in A:
            print(1)
        else:
            print(0)
"""

# 두번째 시도

import sys

N = int(sys.stdin.readline())
A = set(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)

# 배열로 생각하지 말고 A를 정렬한 뒤, 안에 있는지 바로 판단하는 코드를 짜니 해결되었다.
# 이분 탐색으로 해결하는 방법도 있으니 읽어보자.
