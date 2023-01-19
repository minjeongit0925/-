# 문제
'''
    포켓몬 도감을 완성해라.
    현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 
    포켓몬의 번호를 말하거나, 포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 해라.
'''

# 입력
'''
    포켓몬의 개수 N, 내가 맞춰야 하는 문제의 개수 M
    N개의 줄에 포켓몬 입력 모두 영어 

    M개의 줄에 맞춰야 하는 문제, 알파벳으로만 들어오면 포켓몬 번호를 말해야함.
    숫자로만 들어오면 번호에 해당하는 문자를 출력해야함.
'''

# 출력
'''
    문제에 대한 답을 말해줘라.
    입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을,
    문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력해라.
'''
import sys

poketmon = []

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    name = sys.stdin.readline()
    poketmon.append(name)

for _ in range(M):
    problem = input()
    if problem.isdigit(): # true 라고 해도 데이터타입은 str이므로 int로 변환후 연산해야함.
        # 숫자일 경우
        num = int(problem)
        print(poketmon[num-1])
    elif problem.isalpha():
        # 문자일 경우
        print(poketmon.index(problem)+1)
        