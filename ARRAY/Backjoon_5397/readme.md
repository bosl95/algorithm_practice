# [[5397]키로거](https://www.acmicpc.net/problem/5397)

## Array를 이용한 풀이

- 테스트 케이스 개수가 주어진다.
- 테스트 케이스별 L인 문자열이 주어진다. (`1 <= L의 길이 <= 1000000)`
- 백스페이스를 입력한 경우 👉 `-`가 주어지고, 글자가 있는 경우 글자를 지운다.
- 화살표 입력은 `<`와 `>`를 통해 커서의 위치를 이동한다.

### 예외 사항

- `-`가 제일 먼저 입력되는 경우
- 반례 : `a<-b`  👉 결과 `ba`