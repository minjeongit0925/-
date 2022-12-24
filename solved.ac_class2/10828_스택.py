# 문제
'''
    정수를 저장하는 스택 구현.
    입력을 주어지는 명령을 처리하는 프로그램을 작성하시오.
    push, pop, size, empty, top
'''

# 입력
'''
    명령의 수 N
    명령이 하나씩 주어짐.
'''

# 출력
'''
    명령이 주어질 때마다, 한줄에 하나씩 출력
'''
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    orders = sys.stdin.readline().split() # 두개를 입력받음.
    order = orders[0] # 앞에 요소를 받음.

    if order == "push":
        number = orders[1] # 뒤에 요소를 받음.
        stack.append(number)

    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order == "size":
        print(len(stack))
    
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])