# 문제
'''
    해시 함수: 임의의 길이의 입력을 받아서 고정된 길이의 출력을 내보내는 함수
    a, b, c ... 고유 번호 부여 1, 2, 3 ...
    
    # 문제에서 주어진 해시 함수 -> 알파벳 * (31^0) + 알파벳 * (31^1) + 알파벳 * (31^2) + ...

    r = 31, M = 1234567891
'''

# 입력
'''
    문자열의 길이 L
    영문 소문자로만 이루어진 문자열
'''

# 출력
'''
    해시 값
'''

L = int(input())
str = input()

resultStr = []
ans = 0

# 알파벳마다 숫자에 대입
for i in str:
    resultStr.append(ord(i) - 96)  
    # 아스키코드 값이 'a' = 97 'b' = 98 ... ord(i)는 특정 문자의 아스키코드 값으로 변환

def Hash(resultStr):
    result = 0

    for i in range(len(resultStr)):
        ans = resultStr[i] * (31 ** i)
        result += ans
    return print(result % 1234567891)  # %1234567891을 안해서 50점 맞았음.

Hash(resultStr)