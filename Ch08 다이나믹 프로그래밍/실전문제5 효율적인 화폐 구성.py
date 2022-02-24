# 효율적인 화폐 구성 (보텀업)

# 화폐 단위 개수와 만들어야 할 금액 입력 받기
n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

# DP 테이블 생성
d = [0] * (10000 + 1)

# 초기화
for i in money:
    d[i] = 1

# 나올 수 없는 금액 pass
for i in range(min(money), m + 1):
    for j in money:
        if i - j > 0 and d[i - j] > 0:
            if d[i] == 0:
                d[i] = d[i - j] + 1
            else:
                d[i] = min(d[i - j] + 1, d[i])

if d[m]:
    print(d[m])
else:
    print(-1)
