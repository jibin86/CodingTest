# 모험가 길드
# 가장 공포도(x)가 적은 사람을 중심으로 그룹을 만든다.

n = int(input())    # n = 5
x = list(map(int, input().split()))     # x = [2, 3, 1, 2, 2]
x.sort()

count = 0   # 총 그룹 수
list = []   
index = 0

while True:
    if index >= n:
        break
    else:
        list.append(x[index])
        if len(list) == max(list):
            print(list)
            list = []
            count += 1
        index += 1

print(count)



#다른 방법
count = 0   # 총 그룹 수
num = 0

for i in x:
    num += 1
    if num >= i:
        count += 1
        num = 0
print(count)
