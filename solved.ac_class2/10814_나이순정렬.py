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
    user.append([int(age), name]) # 이차원 배열 만들기

user.sort(key=lambda x:x[0])

for i in range(len(user)):
    print(user[i][0], user[i][1])


# 중요하게 가져가야 할 부분
'''
    user.sort(key=lambda x:x[0])
    이차원 배열일 경우, 나이를 기준으로 이 배열을 정렬하고 싶다면
    정렬하고자 하는 요소를 설정할 수 있다.

    lambda x:x[0]을 활용해서 이차원 배열의 0번째 요소인 '나이'를 활용해서
    이차원 배열을 정렬할 수 있다.
'''