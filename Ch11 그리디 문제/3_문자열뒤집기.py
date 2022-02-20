# 백준 1439번
#문자열 뒤집기

# 000110010 0과 1의 집단의 개수를 이용해서 집단의 개수가 적은 집단의 개수를 구하기

data = input()
dif = 0     # 0->1 또는 1->0 으로 바뀌는 횟수
for i in range(1, len(data)):
    if data[i-1] != data[i]:
        dif += 1

if data[0] == data[-1]:
    dif /= 2
else:
    dif = (dif + 1)/2

print(int(dif))
