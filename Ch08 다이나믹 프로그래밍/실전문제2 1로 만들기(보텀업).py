# 1로 만들기 보텀업 방식 (반복문)

n = int(input())

# DP 테이블 만들기
d = [0] * 100

# d[최종값] 구하기!
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])
    if i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i])

print(d[n])
