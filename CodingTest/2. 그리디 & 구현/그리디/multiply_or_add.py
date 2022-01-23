# 그리디 알고리즘
# 문제 : 숫자로 이루어진 문자열을 입력받아 곱하기 또는 더하기를 하여 가장 큰 수를 만들어 출력

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
