# 문제
'''
    FIFO
    1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인한다.
    2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
       이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치한다. 
       그렇지 않다면 바로 인쇄를 한다.
'''

# 입력
'''
    테스트케이스의 수 
    문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M이 주어진다.
'''

# 출력
'''
    각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
'''
# 참고
'''
    https://hongcoding.tistory.com/42
'''

# N = 문서의 개수, importance = 문서의 중요도
# M = 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지
from collections import deque
testcase = int(input())

for _ in range(testcase):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    cnt = 0
    
    while importance:
        best = max(importance) # 현재의 최댓값 저장
        front = importance.popleft()
        M -= 1

        if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            importance.append(front)
            if M < 0:
                M = len(importance) - 1


    importance = []

