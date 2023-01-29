# 문제
'''
    1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    2. X가 2로 나누어 떨어지면, 2로 나눈다.
    3. 1을 뺀다.

    정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
    연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

# 입력
'''
    첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
'''

# 출력
'''
    첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

if N == 1:
    print(0)
else:
    while N > 0:
        if N == 1:
            print(cnt)
            break

        if N > 1 and N % 3 != 0:
            N = N - 1
            cnt += 1
        elif N > 1 and N % 3 == 0:
            N = N // 3
            cnt += 1
        elif N > 1 and N % 2 == 0:
            N = N // 2
            cnt += 1
        
