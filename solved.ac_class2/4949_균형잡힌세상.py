# 문제
'''
    소괄호, 대괄호 균형을 이뤄야 한다.
    균형잡힌 문자열인지 아닌지를 판단해보자.
'''

# 입력
'''
    입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
'''

# 출력
'''
    각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
'''

while True:
    a = input()
    stack = []

    if a == ".": # 입력 종료 조건
        break
    for i in a:
        if i == '[' or i == '(': # 열림 괄호
            stack.append(i)
        elif i == ']': # 대괄호 닫힘 
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')