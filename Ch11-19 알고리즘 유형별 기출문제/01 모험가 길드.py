# 모험가의 수와 모험가의 공포도 입력받기
n = int(input())
n_list = list(map(int, input().split())) # 둘 다 괄호가 필요하다.

# 여행을 떠날 수 있는 그룹 수의 최댓값 출력

# 1. 정렬
n_list.sort() # 1 2 2 2 3
# 2. 그룹원 수 >= 공포도이면, result +1, 그렇지 않으면 그룹원 수 증가
g = 1 # 그룹원 수 1명으로 초기화
result = 0 # 그룹 개수
for i in n_list:
  if g >= i:
    result += 1
    g = 1
  else:
    g += 1

print(result)