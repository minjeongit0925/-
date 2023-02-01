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

    cloths = {}

    n = int(input())
    for _ in range(n):
        suits = list(input().split())
        if suits[1] in cloths:
            cloths[suits[1]].append(suits[0])
        else:
            cloths[suits[1]] = [suits[0]]
    cnt = 1

    for i in cloths:
        cnt *= (len(cloths[i]) + 1) # 옷을 고르는 공식 (a 종류수 + 1) * (b 종류수 + 1) * (c 종류수 + 1) .. - 1

    print(cnt - 1) # 모든 의상을 착용하지 않은 경우 제외
