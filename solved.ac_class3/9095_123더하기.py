# 문제
'''
    1을 1개 이상 사용해서 n을 1, 2, 3의 합으로 나타내는 방법의 수
'''

# 입력
'''
    테스트 케이스 수 T
    정수 n
'''

# 출력
'''
    각 테스트 케이스마다, 
    n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''

import sys
input = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

T = int(input())
for _ in range(T):
    print(cache[int(input())])

# n을 1, 2, 3 의 합으로 나타내는 방법
# ex) 6 = 1 + 2 + 3, 1 * 6, 2 + 2 + 2, 3 + 3, 1 * 3 + 3, 1 * 4 + 2 => 6개
# 숫자가 무조건 1개 이상.

# 1의 개수에 따라서 경우를 나눈다.
# 1이 들어간 합을 먼저 끝내고, 2가 들어간 합, 3이 들어간 합 순으로 진행한다.

