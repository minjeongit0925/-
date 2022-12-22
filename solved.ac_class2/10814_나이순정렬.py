# 문제
'''
    나이, 이름 순서대로 주어짐.
    나이가 증가하는 순으로,
    나이가 같으면 먼저 가입한 사람이 앞으로 정렬
'''

# 입력
'''
    회원의 수 N
    나이 이름
'''

# 출력
'''
    나이 순, 나이가 같으면 가입한 순으로 정렬
'''

N = int(input())
user = []
for i in range(N):
    age, name = map(str, input().split())
    user.append([int(age), name])

user.sort()
for i in range(len(user)):
    print(user[i][0], user[i][1])