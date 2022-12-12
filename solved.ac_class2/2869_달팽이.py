# 문제
'''
    높이 V미터인 나무
    낮에 A미터 올라감.
    밤에 B미터 미끄러짐.
    정상에 올라가면 안미끄러짐.

    달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는가?
'''

# 입력
'''
    A, B, V
'''

# 출력
'''
    달팽이가 나무 올라가는데 며칠 걸리는가?
'''

"""
    # 첫 번째 시도 => 시간 초과 while문으로 계산을 하나하나 해주어야 하기 때문에 시간 초과가 발생한다.
    import sys

    A, B, V = map(int, sys.stdin.readline().split())

    count = 0
    while V > 0:
        V = V - A + B
        if V == 0:
            break
        count += 1

    print(count)

"""


"""
    # 두번째 시도 
    => 마지막엔 결국 A만큼 더 올라가야 하므로 그것을 빼준 높이 V - A
    => 달팽이가 올라가는 속도는 A - B
    높이를 속도로 나눈 나머지가 0이면 걸린 날짜는 높이를 속도로 나눈 몫.
    높이를 속도로 나눈 나머지가 0이 아니라면 높이를 속도로 나눈 몫 + 1 
    마지막에 + 1을 한번 더 해준 이유는 처음 높이에서 A를 빼서 그만큼 더 올라가야 하기 때문이다.
"""

import sys

A, B, V = map(int, sys.stdin.readline().split())

height = V - A
speed = A - B

if height % speed == 0:
    ans = int(height / speed)
else:
    ans = int(height / speed + 1)

print(ans + 1)
