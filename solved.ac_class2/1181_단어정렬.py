# 문제
'''
    알파벳 소문자로 이루어진 N개의 단어
    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전순으로
'''

# 입력
'''
    단어의 개수 N개
    한줄에 단어 하나씩
'''

# 출력
'''
    조건에 따라 단어 정렬
    같은건 한번만 출력
'''

N = int(input())

words = []

for _ in range(N):
    words.append(input())

words.sort(key=len)

for i in range(len(words)):
    if i + 1 == len(words):
            break
    elif words[i] == words[i+1]:
        words.remove(words[i+1])

print(words)