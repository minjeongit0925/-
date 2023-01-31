# 문제
'''
    한번 입었던 옷들의 조합을 절대 다시 입지 않는다.
    해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
'''

# 입력
'''
    테스트 케이스
    의상의 수 n
    의상의 이름과 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
'''

# 출력
'''
    각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로
    의상을 입을 수 있는 경우를 출력하시오.
'''

import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):

    cloths = []
    items = []

    n = int(input())
    for _ in range(n):
        suits = list(input().split())
        cloths.append(suits[0])
        items.append(suits[1])
