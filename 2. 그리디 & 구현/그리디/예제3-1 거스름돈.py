# 그리디
# 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하기

N = int(input())
coin = [500,100,50,10]
count = 0
for i in coin:
    count += N // i
    N = N % i

print(count)
