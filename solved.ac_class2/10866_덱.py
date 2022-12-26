# 문제
'''
    정수를 저장하는 덱(Deque)을 구현한 다음, 입력으로 주어지는 명령 처리.
    push_front X, push_back X
    pop_front, pop_dack
    size, empty, front, back
'''

# 입력
'''
   첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
   둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
   주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
   문제에 나와있지 않은 명령이 주어지는 경우는 없다. 
'''

# 출력
'''
    출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''

import sys

N = int(sys.stdin.readline())

deque = []

for _ in range(N):
    orders = sys.stdin.readline().split()
    order = orders[0]

    if order == "push_front":
        X = orders[1]
        deque.insert(0, X) # 앞에 삽입
    
    elif order == "push_back":
        X = orders[1]
        deque.append(X) # 뒤에 삽입
    
    elif order == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0)) # 맨 앞 요소 뺌
    
    elif order == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop()) # 맨 뒷 요소 뺌
        
    elif order == "size":
        print(len(deque)) # 길이
    
    elif order == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif order == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0]) # 맨 앞 요소 출력
    
    elif order == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1]) # 맨 뒷 요소 출력