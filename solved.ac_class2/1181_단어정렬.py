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

import sys

N = int(sys.stdin.readline())

words = []

for _ in range(N):
    words.append(input())

words_set = set(words) # 단어 중복 제거 => {}형으로 바뀜.

words = list(words_set) # {} => []

words.sort() # 알파벳 순으로 정렬
words.sort(key = len) # 단어 길이 순으로 정렬

for word in words:
    print(word)

# 메모리 35168KB
# 시간 820ms