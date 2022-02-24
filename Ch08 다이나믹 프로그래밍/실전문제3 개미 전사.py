# 개미 전사 (보텀업 방식)

# 식량 창고의 개수, 식량 개수 입력 받기
n = int(input())
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행
d[0] = array[0]
d[1] = max(array[1], array[0])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n-1])
