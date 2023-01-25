# 02 곱하기 혹은 더하기.py

# 문자열 입력받고 정수형 리스트로 만들기
s = list(map(int, input()))  # ['0', '2', '9', '8', '4']

result = 0  # 연산 결과

# 합을 먼저해야 큰 곱셈 연산을 할 수 있다.
s.sort()

# 0 또는 1이 나오거나 이전 결과가 0이면 더하고, 그렇지 않으면 곱한다.
for i in s:
  if i <= 1 or result <= 1:
    result += i
    print(result)
  else:
    result *= i
    print(result)

print(result)
