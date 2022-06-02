"""<day26_백준 2908_상수>
# 문제
- 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다.
- 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
- 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

- 상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
- 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다.
- 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

- 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

## 입력
- 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

## 출력
- 첫째 줄에 상수의 대답을 출력한다.

## 문제 링크 :
- https://www.acmicpc.net/problem/2908
"""

# 테스트1 : 숫자 뒤집기 로직

n1 = 734
n2 = 893

n1_str = str(n1)                   # 뒤집기 위해, 문자열로 전환
n1_str_reverse = n1_str[::-1]      # 뒤집기 : 문자열 슬라이싱 이용
# n1_str_reverse
n1_reverse = int(n1_str_reverse)   # int로 전환
print(n1_reverse)

# 테스트2 : 숫자 뒤집는 메서드

def reverse(n):
    n_str = str(n)
    n_str_reverse = n_str[::-1]
    n_reverse = int(n_str_reverse)
    return n_reverse

print(reverse(734))

# 테스트3 : 두 개 숫자 int로 입력 받기
n1, n2 = map(int, input().split())
print(n1)
print(n2)
