
## <코딩 테스트 + 알고리즘 공부 일지>
- 2018 시나공 정보처리기사 실기 책 알고리즘 문제 참조
- 백준(https://www.acmicpc.net/) 문제

### - day27(220603, 금) : 백준 1157_단어 공부
- 스스로 해결 실패 -> 블로그 참조 : https://ooyoung.tistory.com/70
- <배운 점>
  - upper(), count(), index() 메서드 
  - set 활용해야 하는 경우
- <소회>
  - 아스키 코드로 풀어야 할 줄 알았는데 아니었음
  - 기본적으로 워드 카운트 로직
    - MapReduce 할 때, 공부했었는데 다시 하려니 잘 안됨
    - 문자열, 인덱스, 카운트 등을 종합적으로 활용해야 함
  - 문제가 조금 복잡해지니, 어디서부터 사고를 해야할지 헤맴 -> 꾸준한 연습 필요!
- 문제 링크 : https://www.acmicpc.net/problem/1157

### - day26(220602, 목) : 백준 2908_상수
- 해결
- <배운 점>
  - input() 메서드는 '문자열'을 받는다!
  - 삼항연산자 활용
- <소회>
  - 삼항연산자가 일반 if문에 비해 훨씬 간결
  - 그런데 막상 결과를 보니, 미묘하지만 시간이 더 걸림
  - 자원 활용 및 코드의 간결성 측면에서 삼항연산자를 사용하는 것이 좋은가? 조금 의문
- 문제 링크 : https://www.acmicpc.net/problem/2908

### - day25(220601, 수) : 백준 10809_알파벳 찾기
- 스스로 해결하는 데 실패 -> 블로그 참조
- <배운 점>
  - 아스키 코드에 대한 이해
  - find() 메서드(+ index() 메서드와 비교)
- <소회>
  - 아스키 코드에 대한 이해가 거의 없어서, 문제를 직접 해결할 수 없었음
  - 이 기회로 아스키 코드에 대한 기본적인 개념 학습함
- <참조>
  - https://ooyoung.tistory.com/68
  - https://gururuglasses.tistory.com/88
  - https://j-remind.tistory.com/62

### - day24(220531, 화) : 백준 11720_숫자의 합
- 해결 완료
- <배운 점>
  - input()에 대한 이해
- <소회>
  - 공백없는 입력을 각각의 숫자로 처리하는 것이 핵심

### - day23(220530, 월) : 백준 4344_평균은 넘겠지
- 해결 완료
- <배운 점>
  - f 포멧팅 소숫점 자리 표현 방식 리마인드
  - 리스트 입력받아서, 필요한 변수로 나누기
- <소회>
  - 99.99% 혼자 풀어서 기분 좋음ㅋㅋㅋ
  - 간결한 코드 예시 : https://ooyoung.tistory.com/62

### - day22(220529, 일) : 백준 4673_셀프 넘버
- 스스로 해결하지 못함, 구글링을 통해 다른 블로그 참조
  - https://wook-2124.tistory.com/252
  - https://ooyoung.tistory.com/64
  - https://kbwplace.tistory.com/69
- <배운 점>
  - set 자료형 이해
  - 집합의 뺄셈 개념으로 로직 구성
  - or 함수 활용하여 로직 구성
- <소회>
  - 지금까지 풀었던 문제들이랑은 살짝 결이 달랐다는 느낌
  - 많은 문제를 접하고, 많이 고민하고, 많이 참조하자. 그리고 소화하자

### - day21(220528, 토) : 백준 10818_최소, 최대
- 해결 완료
- <배운 점>
  - 
- <소회>
  - 순수 로직으로 풀기 vs 기존 메서드 이용
  - 이 문제에서는 메모리, 시간 측면에서 그다지 차이가 없음 -> 궁금


### - day20(220527, 금) : 백준 10871_X보다 작은수
- 해결 완료
- <배운 점>
  - list(map(int, input().split())) 활용 : 입력받은 값을 리스트에 바로 삽입
- <소회>
  - 쉬운 문제
  - 지금까지의 문제는 입력값을 어떻게 받을 수 있냐가 관건이었음. 
  - 슬슬 로직 자체가 의미있는 문제를 풀어야 하나

### - day19(220526, 목) : 백준 10950_A+B-3
- 해결 완료
- <배운 점>
  - 언더스코어(_, underscore) 활용법
    - https://mingrammer.com/underscore-in-python/
    - 값을 무시하고 싶은 경우
- <소회>
  - 쉬운 문제
  - 튜플 언패킹하여 원하는 값만 취하고자 할 때, 언더스코어를 요긴하게 사용할 수 있을 것 같음

### - day18(220525, 수) : 백준 1110_더하기 사이클
- 해결 완료
- <배운 점>
  - 무한 루프 사용
  - while문 안의 if문 사용해서 break : break는 if문에 속해 있지만 while 루프 안에 존재한다.
  - 자릿수 뽑아내는 법 : % 활용
- <소회>
  - 오늘은 깔끔하게 해결한 듯!
  - 구글 찾아보니, 더 간결하게 표현은 했으나 기본적인 로직은 내 코드와 같음
    - 변수를 더 줄여서 작성되어 있음 : https://wook-2124.tistory.com/222

### - day17(220524, 화) : 백준 2480_주사위 세개
- 해결 완료
- 배운 점
  - 조건문을 더욱 세심하게
  - 리스트를 효과적으로 활용
  - 메모리 할당과 실행 시간에 대한 고민
- <소회>
  - 여러가지 방법을 고안해봤으나, 딱히 메모리나 실행 시간이 달라지지 않음
  - 연산 자체가 별로 없어서 그렇겠지만, 이 문제를 어떤 방식으로 접근해야 할지 감이 잡히지는 않음

### - day16(220523, 월) : 백준 2525_오븐 시계
- 해결 완료
- 배운점
  - 로직 조건의 미묘함을 경험적으로 배움
  - 오류가 났을 때, 디버깅하며 답을 찾아가는 과정이 중요함
- <소회>
  - 구글링 해보니, 훨씬 간단한 정답이 있음
  - 하지만 현재 내 실력으로는 당장 이와같이 짤 수는 없음
  - 참고해서 시야를 넓히자

### - day15(220521, 토) : 백준 1884_알람 시계
- 해결 완료
- 배운점
  - map 메서드 다시 깊이 이해
- <소회>
  - 결과적으로 최종 정답 코드는 굉장히 간단함
  - 하지만 이걸 도출해내기 위한 논리적 과정은 생각보다 간단하지 않았음
  - 문제 독해 능력과 조건을 나누는 능력을 배양할 필요

### - day14(220520, 금) : 백준 14681_사분면 고르기
- 해결 완료
- <소회>
  - 백준 문제
  - 일단 지나치게 쉬운 느낌이 없지 않지만, 차근차근...

### - day13(220519,목) : 수학 - 시험 성적 출력, 숫자 A, B 비교
- 해결 완료
- 배운점
  - input().split() 사용 방법
  - map 메서드 활용 방법
- <소회>
  - 기분 전환 차원에서 백준 문제 시도, 난이도 쉬운 문제
  - 백준 문제는 입출력이 있기 때문에 고민할 단계가 하나 더 있음
  - 이같은 형식이 코딩 테스트에 더 적합하므로, 병행해서 공부할 예정

### - day12(220518,수) : 수학 - 이진법 변환
- <문제> : 10진수를 2진수로 변환하기
- 해결 완료
- 배운점
  - while문 이해 심화
- <소회>
  - 머리로만 하니 한계를 느낌 -> 종이와 펜 필요!(바람직한 방향인가?)
  - 구글링 결과, 메서드가 따로 있음;;;
  - 효율적인 알고리즘 참고 : https://codeuniv.tistory.com/58

### - day11(220516,월) : 수학 - 소인수분해
- <문제> : 정수를 입력 받아, 소인수를 구해 출력하시오
- 해결 완료
- 배운점
  - 로직이 복잡해지니, 하나의 알고리즘으로 해결하기 힘듦
  - 따라서 문제 해결을 위한 사전 메서드를 만들어야 함
  - 이렇게 스텝을 밟아가는 과정을 잘 익히고, 기획하는 능력을 키워야 할듯
- <소회>
  - 구글링 결과, 더 효율적인 해결 방법들이 많음
  - 값이 작은 수를 판별할 때는, 효율성이 문제가 되지 않지만 숫자가 커지면 속도 차이가 엄청남
  - 지금부터도 이같은 관점으로 고민을 하고, 실력이 더 쌓이면 본격적으로 구현해보기

### - day10(220514,토) : 수학 - 약수 구하기
- <문제> : 정수를 입력 받아, 약수를 구해 출력
- 해결 완료
- 배운점
  - 리스트를 활용한 정답 출력
- <소회>
  - 구글링 해보니, '임의의 자연수 N의 약수들 중에서 두 약수의 곱이 N이 되는 약수 A와 약수 B는 반드시 존재한다'는 규칙을 활용한 효율적 문제풀이 방식이 있음
  - 고민해 보기
  - 그런데, 애초에 수학적 규칙을 모른다면 알고리즘을 짤 수 없을 듯

### - day09(220513,금) : 수학 - 최대공약수, 최소공배수
- <문제> : 두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 계산하여 출력
- 해결 완료
- 배운점
  - for문 더 깊이 이해
  - min, max 로직
- <소회>
  - 구글링 해보니, '유클리드 호제법'이란 방식이 있음
  - 추후 공부하기

### - day08(220512,목) : 수학 - 소수의 합 구하기
- <문제> : 임의의 정수를 입력 받아, 그 안에 포함된 소수의 합을 구하라
- 해결 완료
- 배운점
  - 이중 for문 스스로 고민해서 활용
  - isPrime 불린 변수를 실제로 이용 
- <소회>
  - day07 로직을 가져와, 확장하여 문제 해결

### - day07(220511,수) : 수학 - 소수 판별
- <문제> : 1보다 큰 임의의 정수를 입력받아 소수를 판별하라
- 해결 완료
- 배운점
  - for문 내, break 사용하여 리소스 낭비 방지
- <소회>
  - 가장 간단한 수학 알고리즘 문제

### - day06(220510,화) : 수열06 - 피보나치 수열
- <문제> : 1+1+2+3+5+8+13+...의 수열로 나열되는 피보나치 수열의 20번째 항까지의 합계
- 해결 완료
- 배운점
  - while문 활용 : 상황에 따라 판단하여, for문 vs while문 선택
  - temp 변수 활용
  - 주석 정렬 : 훨씬 깔끔해짐
    - 추후 내용적인 측면도 보완
- <소회>
  - 구글링 해보니, 리스트를 활용한 피보나치 수열 구현도 있음 -> 추후 **스스로** 고민

### - day05(220509,월) : 수열05
- <문제> : 1!+2!+3!+4!+5!+...+10!의 순서로 나열되는 수열의 10번째 항까지의 합계
- 해결 완료
- 배운점
  - 테스트부터 한단계 한단계 진행하며 최종 해결까지 진행
  - 주석을 작성함으로써 나뿐만 아니라, 타인이 볼때 쉽게 이해가도록 코드 작성
- <소회>
  - 차근차근 만들어 간다는 느낌으로 해야지 사고가 꼬이지 않음
  - 주석을 적절하게 활용하자
  - 변수명도 신경쓰자
  - 펙토리얼을 더 효율적으로 구현하는 로직이 많을테니, 추후 테스트 ex)재귀호출

### - day04(220507,토) : 수열04
- <문제> : 1+2+4+7+11+16+22+...의 순서로 나열되는 수열의 20번째 항까지의 합계
- 해결 완료
- 배운점
  - 알고리즘 짤때, 코드 순서에 대한 이해가 조금 깊어짐
  - 문제 해결을 위한 알고리즘은 무한히 많을 수 있겠다고 피부로 느낌
- <소회>
  - 금일 메인 문제에 딸린 추가 문제 못 품
  - 추후 꼭꼭 시도하기!

### - day03(220506,금) : 수열03
- <문제> : (1/2)+(2/3)-(3/4)+(4/5)-(5/6) ... -(99/100)의 합계
- 해결 완료
- 배운점
  - 소수점 처리 : round 메서드
  - 메서드 형태로 정답 출력
- <소회> : 양을 조금 늘려볼까?

### - day02(220505,목) : 수열02
- <문제> : 1-2+3-4+ ... +99-100의 합계
- 해결 완료
  - 확장 문제1 : 1-2+3-4+5-6+ ... +99 -> 해결
  - 확장 문제2 : (-1)×2×(-3)×4×(-5)× ··· ×100  -> 해결
- 배운점
  - 문자열 f-formatting 확실히 습득
  - 서식 지정자 자료형 확인 : https://dojang.io/mod/page/view.php?id=2305
- <소회> : 차근차근, 확실히

### - day01(220504,수) : 수열01, 
- <문제> : 1+2+3+...+100까지 합계
- 해결 완료
  - 확장 문제 : 1+3+5+7+...+99 -> 해결
  - 개선 필요 사항 : 정답을 '잘' 출력하는 방법도 고민 필요
- <소회> : 첫 스타트를 잘 끊었다.



