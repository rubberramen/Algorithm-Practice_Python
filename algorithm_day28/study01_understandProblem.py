"""<day28_백준 9372_상근이의 여행>
# 문제
- 상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다.

- 하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.

- 이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.

- 상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.

## 입력
- 첫 번째 줄에는 테스트 케이스의 수 T(T ≤ 100)가 주어지고,

- 각 테스트 케이스마다 다음과 같은 정보가 주어진다.
    - 첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
    - 이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b)
    - 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

## 출력
- 테스트 케이스마다 한 줄을 출력한다.
    - 상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.

## 문제 링크
- https://www.acmicpc.net/problem/9372
"""

t = 2   # 테스트 케이스의 수

# 케이스1
n1 = 3   # 국가의 수
m1 = 3   # 비행기의 종류

# 1 2 : 1국과 2국을 연결하는 비행기가 있다.
# 2 3 : 1국과 2국을 연결하는 비행기가 있다.
# 1 3 : 1국과 3국을 연결하는 비행기가 있다.

# 케이스2
n2 = 5
m2 = 4

# 2 1 : 2국과 1국을 연결하는 비행기가 있다.
# 2 3 : 2국과 3국을 연결하는 비행기가 있다.
# 4 3 : 4국과 3국을 연결하는 비행기가 있다.
# 4 5 : 4국과 5국을 연결하는 비행기가 있다.

"""
<출력>
2   # 케이스1에서 상근이가 타야하는 비행기 종류의 최소 개수
4   # 케이스2에서 상근이가 타야하는 비행기 종류의 최소 개수
"""