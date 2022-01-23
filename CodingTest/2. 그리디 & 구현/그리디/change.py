#그리디 알고리즘
#문제 : 거스름 돈의 개수 세기 - 최적의 해를 구하기 위해서 가장 큰 화폐 단위부터 돈을 거슬러 준다.
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
