# 문제
'''
    듣도 못한 사람의 명단과,
    보도 못한 사람의 명단이 주어질 때,
    듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
'''

# 입력
'''
    듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
    둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
    N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
'''

# 출력
'''
    듣보잡의 수와 그 명단을 사전순으로 출력한다.
'''

import sys

no_hear_list = set()
no_see_list = set()
cnt = 0

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    name_no_hear = sys.stdin.readline().strip()
    no_hear_list.add(name_no_hear)
for _ in range(M):
    name_no_see = sys.stdin.readline().strip()
    no_see_list.add(name_no_see)

result = sorted(list(no_hear_list & no_see_list))

print(len(result))
for i in result:
    print(i)