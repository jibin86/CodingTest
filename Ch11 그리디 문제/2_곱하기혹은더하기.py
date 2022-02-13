# 곱하기 혹은 더하기

# list(string) : 공백을 포함해서 문자열을 하나씩 쪼갬
# list_a = list(map(int,list_a)) : 리스트의 문자열을 int 형태로 변환

data = list(input())
data = list(map(int, data))
print(data)
result = data[0]    # 앞에서 계산된 결과물

for i in range(1,len(data)):
    if result <= 1 or data[i] <=1:
        result += data[i]
    else:
        result *= data[i]

print(result)
