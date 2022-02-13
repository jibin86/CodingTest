# 숫자 카드 게임 : 행을 입력 받고 각각의 행의 최솟값들의 최대값 구하기

# min(list) : 리스트의 최솟값
# max(list) : 리스트의 최댓값

n, m = map(int,input().split())
min_max = 0
for i in range(n):
    data = list(map(int,input().split()))
    if min_max < min(data):
        min_max = min(data)

print(min_max)
    
