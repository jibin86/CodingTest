# 큰 수의 법칙 : 크기가 n인 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
#                단, 배열의 원소가 연속해서 k번 초과하여 더해질 수 없다.

# list(map(int, input().split())) : 입력 받고 한번에 공백으로 쪼개서 정수로 바꾸고 리스트로 묶음
# list.sort(reverse=True) : 내림차순으로 정렬

n, m, k = map(int,input().split())
data = list(map(int, input().split()))

list = []
count = k
data.sort(reverse=True)

while(len(list)!=m):
    if count == 0:
        list.append(data[1])
        count = k
    else:
        list.append(data[0])
        count -= 1
        
print(sum(list))
