# 만들 수 없는 금액

# 리스트에 특정 값이 있는지 확인 : if item in list:
#                    없는지      :         not in

n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)

for i in range(n):
    if i not in data:

        for j in data:
            if i - j < 1:
                pass



for i in range(5,0,-1):
    print(i)
