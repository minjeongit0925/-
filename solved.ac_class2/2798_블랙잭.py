# 문제
'''
    카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임
    N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
    딜러가 숫자 M을 크게 외친다.

    N장의 카드 중에서 3장의 카드를 골라야 한다.
    M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
    N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
'''

# 입력
'''
    N개의 카드, 숫자 M
    카드에 쓰여 있는 수
'''

# 출력
'''
    M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
'''

from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sumCombis = []

for combi in combinations(nums, 3):
    sumCombis.append(sum(combi))

sumCombis.sort()

while True:
    if sumCombis[-1] <= M:
        print(sumCombis[-1])
        break
    else:
        sumCombis.pop()

# 조합 사용함.