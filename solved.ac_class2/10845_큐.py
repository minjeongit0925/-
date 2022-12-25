# 문제
'''
    정수를 저장하는 큐를 구현
    push X, pop, size, empty, front, back
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
queue = []

N = int(sys.stdin.readline())

for _ in range(N):
    orders = sys.stdin.readline().split() # 두개를 입력받음.
    order = orders[0] # 앞에 요소를 받음.

    if order == "push":
        number = orders[1]
        queue.append(number)

    elif order == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0)) # pop(0)을 하면 첫번째 데이터를 제거할 수 있다.
        
    elif order == "size":
        print(len(queue))
    
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif order == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif order == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])